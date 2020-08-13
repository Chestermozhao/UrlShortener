from typing import List
import aiohttp

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from url_shortener.serializers.schemas import (
    UrlShortenersOut,
    UrlShortenerOut,
    UrlShortenerIn,
)
from url_shortener.database import database, urlshorteners
from url_shortener.libs.get_short_path import (
    get_data,
    create_short_path,
    get_short_link,
)

router = APIRouter()


@router.get("/shortener/", response_model=List[UrlShortenersOut])
async def show_shorten_urls():
    query = urlshorteners.select()
    return await database.fetch_all(query)


@router.post("/shortener/", response_model=UrlShortenerOut)
async def create_shorten_urls(shorten: UrlShortenerIn, request: Request):
    origin_url = shorten.origin_url
    # get or create
    result = await get_data("origin_url", origin_url)
    if result is not None:
        short_link = get_short_link(request, result["short_path"])
        return {**result, "short_link": short_link, "status": 0}
    short_path = await create_short_path()
    query = urlshorteners.insert().values(
        origin_url=shorten.origin_url, short_path=short_path
    )
    shorten_id = await database.execute(query)
    result = await get_data("id", shorten_id)
    short_link = get_short_link(request, result["short_path"])
    return {**result, "short_link": short_link, "status": 0}


@router.get("/{short_path}")
async def show_origin_page(short_path: str):
    result = await get_data("short_path", short_path)
    if result is None:
        return {"status": -1, "errMsg": "no this short path"}

    origin_url = result["origin_url"]
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(origin_url) as response:
                html_content = await response.content.read()
                if html_content:
                    return HTMLResponse(content=html_content, status_code=200)
    except Exception:
        return {"status": -1, "errMsg": "request origin url failed"}

    return {"status": -1, "errMsg": "there is no html response"}
