import pendulum
from airflow.decorators import dag
from tasks.fetch_comments import fetch_comments
from tasks.store_comments import bulk_insert


@dag(
    schedule=None,
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def youtube():
    comments = fetch_comments()
    bulk_insert(index="test_comments", docs=comments)


youtube()
