from database.database import database

urls = database.get_collection("urls")

def url_helper(url) -> dict:
    return {
        "id": str(url["id"]),
        "url": str(url["url"]),
        "userID": str(url["userID"]),
    }