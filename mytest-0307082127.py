from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "mytest-0307082127",
}

dag = DAG(
    "mytest-0307082127",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.3.0.dev0 pipeline editor using `mytest.ipynb`.",
    is_paused_upon_creation=False,
)


# Operator source: mytest.ipynb
op_0ced1eb7_17d8_4433_8617_55f8cc4d90d6 = KubernetesPodOperator(
    name="mytest",
    namespace="default",
    image="continuumio/anaconda3:2020.07",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://host.docker.internal:9000 --cos-bucket elyra-tesst --cos-directory 'mytest-0307082127' --cos-dependencies-archive 'mytest-0ced1eb7-17d8-4433-8617-55f8cc4d90d6.tar.gz' --file 'mytest.ipynb' "
    ],
    task_id="mytest",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mytest-0307082127-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)
