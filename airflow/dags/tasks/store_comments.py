import json

from airflow.decorators import task
from elasticsearch import Elasticsearch

es = Elasticsearch(
    "http://172.17.0.1:9200"
)


@task()
def bulk_insert(index, docs):
    body = []
    json_docs = json.loads(docs)
    operation = {"create": {"_index": index}}
    for doc in json_docs:
        body.append(operation)
        body.append(doc)

    resp = es.bulk(body=body)
    print(resp)
