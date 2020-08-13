import arrow
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./url_shorten.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

urlshorteners = sqlalchemy.Table(
    "urlshortener",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("origin_url", sqlalchemy.String),
    sqlalchemy.Column("short_path", sqlalchemy.String, unique=True),
    sqlalchemy.Column(
        "created_at", sqlalchemy.String, server_default=arrow.now().format("YYYYMMDD")
    ),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
