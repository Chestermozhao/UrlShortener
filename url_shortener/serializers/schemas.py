from pydantic import BaseModel


class UrlShortenersOut(BaseModel):
    id: int
    short_path: str
    origin_url: str
    created_at: str


class UrlShortenerOut(BaseModel):
    id: int
    short_link: str
    origin_url: str
    created_at: str

    class Config:
        orm_mode = True


class UrlShortenerIn(BaseModel):
    origin_url: str

    class Config:
        orm_mode = True
