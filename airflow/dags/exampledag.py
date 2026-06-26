"""
# Example DAG for THE_RICK_AND_MORTY project

Este DAG demonstra como criar um simples fluxo de trabalho Airflow usando a
API de TaskFlow. Ele roda diariamente e contém duas tarefas de exemplo:

1. **echo_hello** – imprime uma mensagem de boas‑vindas.
2. **print_timestamp** – mostra a data e hora da execução.

O DAG pode ser usado como ponto de partida para adicionar tarefas
personalizadas ao seu projeto.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import datetime

# Definição básica do DAG
default_args = {
    "owner": "leandro",
    "retries": 1,
    "catchup": False,
}

with DAG(
    dag_id="example_rick_and_morty",
    description="DAG de exemplo para o projeto THE_RICK_AND_MORTY",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    default_args=default_args,
    tags=["example", "rick_and_morty"],
) as dag:

    def echo_hello():
        """Tarefa simples que imprime uma saudação."""
        print("Hello from THE_RICK_AND_MORTY DAG!")

    def print_timestamp():
        """Mostra a data/hora atual da execução do DAG."""
        from datetime import datetime as dt
        print(f"Current execution time: {dt.utcnow().isoformat()}Z")

    # Operadores Python
    hello_task = PythonOperator(
        task_id="echo_hello",
        python_callable=echo_hello,
    )

    timestamp_task = PythonOperator(
        task_id="print_timestamp",
        python_callable=print_timestamp,
    )

    # Definir ordem: hello_task >> timestamp_task
    hello_task >> timestamp_task
