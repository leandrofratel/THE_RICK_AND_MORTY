import json
import re
from pathlib import Path

md_path = Path('MEDIDAS_DAX_RICK_AND_MORTY.md')
text = md_path.read_text(encoding='utf-8')
pattern = re.compile(r'###\s+(.*?)\r?\n```dax\r?\n(.*?)\r?\n```', re.S)

measures = []
for m in pattern.finditer(text):
    name = m.group(1).strip()
    block = m.group(2).strip()
    comment_match = re.search(r'/\*(.*?)\*/', block, re.S)
    comment = comment_match.group(0).strip() if comment_match else ''
    body = re.sub(r'/\*.*?\*/', '', block, flags=re.S).strip()
    if '=' in body:
        expression = body.split('=', 1)[1].strip()
    else:
        expression = body
    page = 'General'
    if comment:
        page_match = re.search(r'Página:\s*(.*)', comment)
        if page_match:
            page = page_match.group(1).strip()
    measures.append({
        'name': name,
        'comment': comment,
        'expression': expression,
        'page': page,
    })

with open('measure_defs_md.json', 'w', encoding='utf-8') as f:
    json.dump(measures, f, ensure_ascii=False, indent=2)
print(f'Wrote {len(measures)} measures to measure_defs_md.json')
