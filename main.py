from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
)


@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    return JSONResponse(
        {
            "schema_version": "v1",
            "name_for_human": "ChatGPT plugin template",
            "name_for_model": "template",
            "description_for_human": "Template to build awesome ChatGPT plugins.",
            "description_for_model": "Template to build awesome ChatGPT plugins.",
            "auth": {"type": "none"},
            "api": {
                "type": "openapi",
                "url": "http://localhost:8000/openapi.json",
                "is_user_authenticated": False,
            },
            "logo_url": "http://localhost:8000/logo.png",
            "contact_email": "legal@example.com",
            "legal_info_url": "http://example.com/legal",
        }
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.mount("/", StaticFiles(directory="public"), name="static")
