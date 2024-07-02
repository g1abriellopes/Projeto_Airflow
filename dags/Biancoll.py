from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
from plugins.Scripts.Salvar_Excel import Imbaud

def cubo_financeiro():
    print("Correto")

with DAG(
    'Biancoll',
    start_date=pendulum.datetime(2024, 5, 9, tz="UTC"),
    schedule_interval='@daily',
    catchup=False  # Evitar execuções atrasadas
) as dag:

    tarefa_executar_cubo_financeiro = PythonOperator(
        task_id='Executar_Cubo',
        python_callable=cubo_financeiro
    )

    tarefa_executar_cubo_financeiro
