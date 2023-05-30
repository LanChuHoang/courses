import json
import os
import socket
import subprocess
from types import SimpleNamespace

import pandas as pd
from airflow.decorators import task
from joblib import load


@task()
def extract_features(json_comments):
    AIRFLOW_HOME = os.getenv("AIRFLOW_HOME")
    base_file_path = AIRFLOW_HOME + "/dags/tasks/model"
    vect_file_path = base_file_path + "/tfidf_vectorizer.joblib"
    model_file_path = base_file_path + "/movie_review_sa_v1.joblib"
    vectorizer = load(vect_file_path)
    model = load(model_file_path)
    comments = json.loads(json_comments, object_hook=lambda d: SimpleNamespace(**d))

    for comment in comments:
        feature_matrix = vectorizer.transform([comment.cleaned_content])
        sentiment = model.predict(feature_matrix)[0]
        comment.sentiment = sentiment

    featured_json_comments = json.dumps([ob.__dict__ for ob in comments])
    return featured_json_comments
