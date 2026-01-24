FROM apache/airflow:latest-python3.9
USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/airflow/dags /opt/airflow/logs && \
    chown -R airflow:root /opt/airflow && \
    chmod -R 755 /opt/airflow/logs

USER airflow

RUN pip install --no-cache-dir \
    apache-airflow-providers-github \
    apache-airflow-providers-amazon \
    apache-airflow-providers-mysql \
    apache-airflow-providers-mongo \
    apache-airflow[celery,redis] \
    pandas

COPY --chown=airflow:root dags/* /opt/airflow/dags/

ENV AIRFLOW__LOGGING__BASE_LOG_FOLDER=/opt/airflow/logs \
    AIRFLOW__LOGGING__WORKER_LOG_SERVER_PORT=8793 \
    AIRFLOW__LOGGING__LOGGING_LEVEL=INFO \
    AIRFLOW__LOGGING__LOG_FORMAT='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s' \
    AIRFLOW__LOGGING__SIMPLE_LOG_FORMAT='%(asctime)s %(levelname)s - %(message)s' \
    AIRFLOW__LOGGING__DAG_PROCESSOR_LOG_TARGET=file \
    AIRFLOW__LOGGING__TASK_LOG_READER=task \
    AIRFLOW__LOGGING__DAG_FILE_PROCESSOR_LOG_TARGET=/opt/airflow/logs/dag_processor_manager/dag_processor_manager.log \
    AIRFLOW__LOGGING__DAG_PROCESSOR_MANAGER_LOG_LOCATION=/opt/airflow/logs/dag_processor_manager/dag_processor_manager.log

ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags

RUN mkdir -p /opt/airflow/logs/scheduler \
            /opt/airflow/logs/web \
            /opt/airflow/logs/worker \
            /opt/airflow/logs/dag_processor_manager \
            /opt/airflow/logs/task_logs

USER root
RUN chown -R airflow:root /opt/airflow && \
    chmod -R 755 /opt/airflow
USER airflow

