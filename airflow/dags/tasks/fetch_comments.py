import json
import logging

import requests
from airflow.decorators import task


class Comment:
    def __init__(self, id, videoId, content, author_name, author_profile_image_url, like_count, published_at, updated_at):
        self.id, self.videoId, self.content, self.author_name, self.author_profile_image_url, self.like_count, self.published_at, self.updated_at = id, videoId, content, author_name, author_profile_image_url, like_count, published_at, updated_at


@task()
def fetch_comments():
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    video_id = 'ZOfPPHcAa7E'
    params = {
        'key': 'AIzaSyAfAh6Ie5gu8GW53WhQsUNSb3suTh_M3GM',
        'videoId': 'ZOfPPHcAa7E',
        'part': 'id,snippet',
        'order': 'relevance',
        'maxResults': 100,
    }
    response = requests.get(url, params).json()
    comments_json = response['items']

    comments = []
    for comment_json in comments_json:
        id = comment_json['id']
        video_id = comment_json['snippet']['videoId']
        detail = comment_json['snippet']['topLevelComment']['snippet']
        content = detail['textOriginal']
        author_name = detail['authorDisplayName']
        author_profile_image_url = detail['authorProfileImageUrl']
        like_count = detail['likeCount']
        published_at = detail['publishedAt']
        updated_at = detail['updatedAt']
        comment = Comment(id, video_id, content, author_name,
                          author_profile_image_url, like_count, published_at, updated_at)
        comments.append(comment)
    logging.info(f'Fetched {len(comments)} comments of video {video_id}')

    json_comments = json.dumps([ob.__dict__ for ob in comments])
    return json_comments


fetch_comments()
