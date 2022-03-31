import airflow.utils.dates as dates


from airflow import DAG
from airflow.operators.bash import BashOperator



# travel dag
travel_dag = DAG(
    dag_id="travel_reviews_uci",
    description="Download travel reviews from UCI ml repo",
    start_date=dates.days_ago(14),
    schedule_interval="@daily"
)

# bash operator to download data 
download_travel_reviews = BashOperator(
    task_id="download_travel_reviews",
    bash_command="curl -o /tmp/tripadvisor_review.csv -L https://archive.ics.uci.edu/ml/machine-learning-databases/00484/tripadvisor_review.csv",
    dag = travel_dag
)

# notify bash operator
travel_notify = BashOperator(
    task_id="travel_notify",
    bash_command='echo "There is now $(ls /tmp) file."',
    dag=travel_dag
)
