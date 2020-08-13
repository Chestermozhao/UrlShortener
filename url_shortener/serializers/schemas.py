from pydantic import BaseModel, HttpUrl


class UrlShortenersOut(BaseModel):
    id: int
    short_path: str
    origin_url: HttpUrl
    created_at: str


class UrlShortenerOut(BaseModel):
    id: int
    status: int
    short_link: str
    origin_url: HttpUrl
    created_at: str

    class Config:
        orm_mode = True


class UrlShortenerIn(BaseModel):
    origin_url: HttpUrl

    class Config:
        orm_mode = True
