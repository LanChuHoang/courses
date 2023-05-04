from elasticsearch import Elasticsearch

es = Elasticsearch(
    "http://localhost:9200"
)


def get_all_docs(index):
    return es.search(index="test_comments", query={"match_all": {}})


def bulk_insert(index, docs):
    body = []
    operation = {"create": {"_index": index}}
    for doc in docs:
        body.append(operation)
        body.append(doc)

    resp = es.bulk(body=body)
    print(resp)


bulk_insert(index="test_comments", docs=[{'name': 'doc1'}, {'name': 'doc2'}])
