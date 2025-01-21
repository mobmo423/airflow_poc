# Use the official Apache Airflow base image
FROM apache/airflow:2.9.0

# Install Airflow Snowflake provider
RUN pip install --no-cache-dir apache-airflow-providers-snowflake

# Install dbt-snowflake in a virtual environment to avoid conflicts
USER root
ENV PIP_USER=false
RUN python -m venv /usr/local/airflow/dbt_env
RUN /usr/local/airflow/dbt_env/bin/pip install --no-cache-dir dbt-snowflake
ENV PIP_USER=true

# Switch back to the airflow user
USER airflow

# Set necessary environment variables for Airflow
ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# Expose the webserver port
EXPOSE 8080

# Set the entrypoint and default command
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["webserver"]
