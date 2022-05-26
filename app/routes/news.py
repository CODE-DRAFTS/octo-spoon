'''
file for routes relating to news

//routes
//@router.get("/")               --to get all news articles stored in db
//@router.post("/")              --to create a news article in db
//@router.get("/{news_id}")      --to get a single news article
//@router.put("/{news_id}")      --to update a news article
//@router.delete("/{news_id}")   --to delete a news article
'''

from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/news",
)

@router.get("/")
async def get_all_news():
    return {"all news items"}

@router.post("/")
async def create_news_article():
    return {"created a new news article"}

@router.get("/{news_id}")
async def get_news_item( news_id:str):
    return {f" news article {news_id} looks fun"}

@router.put("/{news_id}")
async def delete_news_item(news_id: str):
    return {f"updates news article {news_id}"}

@router.delete("/{news_id}")
async def delete_news_item(news_id: str):
    return {"deleted news article"}


