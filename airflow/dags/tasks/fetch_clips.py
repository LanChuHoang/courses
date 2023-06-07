from airflow.providers.mongo.hooks.mongo import MongoHook

hook = MongoHook(conn_id="mongo_connection")
client = hook.get_conn()
db = client.get_database("v2")
movies_collection = db.get_collection("movies")


def fetch_movies(limit: int) -> list:
    try:
        movies = list(
            movies_collection.aggregate(
                [
                    {"$match": {"title": "Thor: Love and Thunder"}},
                    {
                        "$project": {
                            "_id": {"$toString": "$_id"},
                            "releaseDate": 1,
                            "reviewClips": 1,
                        }
                    },
                ]
            )
        )
        return movies
    except Exception as e:
        print(e)
        return []
