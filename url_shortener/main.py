from fastapi import FastAPI
from starlette.responses import RedirectResponse
from url_shortener.database import database
from url_shortener.utils.config import cfg, env
from url_shortener.views.v1 import router as v1_router


app = FastAPI(
    title=cfg.project.name.format(env=env),
    description="Url Shorten Service",
    openapi_url="/api/v1/openapi.json",
)
app.include_router(v1_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
