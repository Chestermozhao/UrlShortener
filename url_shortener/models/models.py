from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import URLType

Base = declarative_base()


class UrlShortener(Base):
    __tablename__ = "urlshortener"

    id = Column(Integer, primary_key=True, index=True)
    origin_url = Column(URLType, unique=True)
    short_path = Column(String(5), index=True, unique=True)
    created_at = Column(String(8))
