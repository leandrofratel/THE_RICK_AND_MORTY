import json
import re
from pathlib import Path

md_defs = json.loads(Path('measure_defs_md.json').read_text(encoding='utf-8'))
model_path = Path(r'c:\Users\Leandro-Fratel\AppData\Roaming\Code\User\workspaceStorage\ab0f2c40f38250d1a158ba9135d38b0c\GitHub.copilot-chat\chat-session-resources\246b4b7a-a42d-48da-bc86-e2322b6573f7\call_46crMsoGp5m0BB8QR97olMpa__vscode-1781673238800\content.json')
model = json.loads(model_path.read_text(encoding='utf-8'))

# Normalization removing diacritics and lowercasing
import unicodedata

def normalize(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
    return text.lower().strip()

model_map = {}
for item in model['results']:
    name = item['data']['name']
    norm = normalize(name)
    if norm not in model_map:
        model_map[norm] = {
            'origName': name,
            'table': item['data']['tableName'],
            'displayFolder': item['data']['displayFolder'],
        }

move_defs = []
update_defs = []
missing = []
for m in md_defs:
    norm = normalize(m['name'])
    if norm not in model_map:
        missing.append(m['name'])
        continue
    current = model_map[norm]
    if current['table'] != '_Medidas':
        move_defs.append({
            'name': current['origName'],
            'currentTableName': current['table'],
            'destinationTableName': '_Medidas',
        })
    display_folder = f"{m['page']}"
    expression = (m['comment'] + '\n' + m['expression']).strip() if m['comment'] else m['expression']
    update_defs.append({
        'tableName': '_Medidas',
        'name': current['origName'],
        'expression': expression,
        'displayFolder': display_folder,
    })

Path('measure_move_defs.json').write_text(json.dumps(move_defs, ensure_ascii=False, indent=2), encoding='utf-8')
Path('measure_update_defs.json').write_text(json.dumps(update_defs, ensure_ascii=False, indent=2), encoding='utf-8')
Path('measure_update_summary.json').write_text(json.dumps({
    'moveCount': len(move_defs),
    'updateCount': len(update_defs),
    'missing': missing,
}, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'move_defs={len(move_defs)} update_defs={len(update_defs)} missing={len(missing)}')
if missing:
    print('Missing models:')
    for mm in missing:
        print(' -', mm)
