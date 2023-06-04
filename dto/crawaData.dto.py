from database.database import database

urls = database.get_collection("crawler-data")

def crawl_helper(crawler) -> dict:
    return {
        "id": str(crawler["id"]),
        "siteId": str(crawler["url"]),
        "url": str(crawler["userID"]),
        "data":dict(crawler['data'])
    }