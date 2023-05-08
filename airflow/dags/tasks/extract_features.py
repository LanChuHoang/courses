import json
import os
import subprocess
from types import SimpleNamespace

from airflow.decorators import task
from joblib import load

CUR_DIR = os.path.abspath(os.path.dirname(__file__))


@task()
def extract_features(json_comments):
    print(CUR_DIR)

    result = subprocess.run(['ls'], stdout=subprocess.PIPE)
    print(result.stdout)

    # vectorizer = load('f"{CUR_DIR}/model/tfidf_vectorizer.joblib"')
    # comments = json.loads(
    #     json_comments, object_hook=lambda d: SimpleNamespace(**d))
    # for comment in comments:
    #     comment.feature = vectorizer.transform([comment.cleaned_content])
    # featured_json_comments = json.dumps([ob.__dict__ for ob in comments])
    # return featured_json_comments
