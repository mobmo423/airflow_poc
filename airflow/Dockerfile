FROM apache/airflow:2.9.0

RUN pip install --no-cache-dir apache-airflow-providers-snowflake

# Install dbt-snowflake in a virtual environment to avoid conflict
USER root
ENV PIP_USER=false
RUN python -m venv /usr/local/airflow/dbt_env
RUN /usr/local/airflow/dbt_env/bin/pip install --no-cache-dir dbt-snowflake
ENV PIP_USER=true

USER airflow

# Initialize the Airflow database
RUN airflow db init


