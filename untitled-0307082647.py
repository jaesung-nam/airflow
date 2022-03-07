from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "untitled-0307082647",
}

dag = DAG(
    "untitled-0307082647",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.3.0.dev0 pipeline editor using `untitled.pipeline`.",
    is_paused_upon_creation=False,
)


# Operator source: mytest.ipynb
op_7a81c133_835b_4891_b05b_3f20ef8c796a = KubernetesPodOperator(
    name="mytest",
    namespace="default",
    image="continuumio/anaconda3:2020.07",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://host.docker.internal:9000 --cos-bucket elyra-tesst --cos-directory 'untitled-0307082647' --cos-dependencies-archive 'mytest-7a81c133-835b-4891-b05b-3f20ef8c796a.tar.gz' --file 'mytest.ipynb' "
    ],
    task_id="mytest",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled-0307082647-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: work/mytest2.ipynb
op_23ba9298_93a5_4eeb_b14d_4064d3e12ec6 = KubernetesPodOperator(
    name="mytest2",
    namespace="default",
    image="continuumio/anaconda3:2020.07",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://host.docker.internal:9000 --cos-bucket elyra-tesst --cos-directory 'untitled-0307082647' --cos-dependencies-archive 'mytest2-23ba9298-93a5-4eeb-b14d-4064d3e12ec6.tar.gz' --file 'work/mytest2.ipynb' "
    ],
    task_id="mytest2",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled-0307082647-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_23ba9298_93a5_4eeb_b14d_4064d3e12ec6 << op_7a81c133_835b_4891_b05b_3f20ef8c796a
