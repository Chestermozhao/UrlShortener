import os
import random
from url_shortener.libs.const import BASIC_CHARS, PATH_LENGTH
from url_shortener.libs.sqls import query_pattern
from url_shortener.database import database
from sqlalchemy import inspect


async def get_data(query_field, query_item):
    query = query_pattern.format(query_item=query_item, query_field=query_field)
    result = await database.fetch_one(query=query)
    return result


async def create_short_path():
    short_path = _create_short_path()
    while await get_data("short_path", short_path):
        short_path = _create_short_path()
    return short_path


def _create_short_path():
    return "".join([random.choice(BASIC_CHARS) for _ in range(PATH_LENGTH)])


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def get_short_link(request, short_path):
    schema = request.scope.get("scheme")
    host_tuple = request.scope.get("server")
    host_name = os.getenv("HOST_HOSTNAME") or host_tuple[0]
    host = "{host}:{port}".format(host=host_name, port=host_tuple[1])
    short_path = "{schema}://{host}/{short_path}".format(
        schema=schema, host=host, short_path=short_path
    )
    return short_path
