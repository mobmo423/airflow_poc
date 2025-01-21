FROM apache/airflow:2.9.0

# Install the Snowflake provider
RUN pip install --no-cache-dir apache-airflow-providers-snowflake

# Install dbt-snowflake in a virtual environment to avoid conflicts
USER root
RUN python -m venv /opt/airflow/dbt_env \
    && /opt/airflow/dbt_env/bin/pip install --no-cache-dir dbt-snowflake \
    && chown -R airflow: /opt/airflow/dbt_env

# Switch back to the airflow user
USER airflow

# Initialize the Airflow database
RUN airflow db init


