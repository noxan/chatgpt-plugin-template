import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
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


class Payload(BaseModel):
    query: str


@app.post("/wikipedia")
def wikipedia_post(payload: Payload):
    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "titles": payload.query,
            "prop": "extracts",
            "redirects": True,
            "exintro": True,
            "explaintext": True,
        },
    ).json()
    page = next(iter(response["query"]["pages"].values()))
    return JSONResponse({"result": page["extract"]})


app.mount("/", StaticFiles(directory="public"), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
