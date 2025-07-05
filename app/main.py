from fastapi import APIRouter, FastAPI, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse
from .db import SessionLocal, engine, Base
from . import crud
from sqlalchemy.orm import Session
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def health_check():
    return {"status": "OK"}


router = APIRouter()

async def redirect(slug: str, request: Request, db=Depends(get_db)):
    link = crud.get_link_by_slug(db, slug)
    
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")

    crud.log_click(
        db,
        link_id=link.id,
        ip=request.client.host,
        referrer=request.headers.get("referer"),
        user_agent=request.headers.get("user-agent")
    )

    return RedirectResponse(link.destination_url)

@app.post("/api/links")
async def create_link(request: Request, db=Depends(get_db)):
    body = await request.json()
    dest_url = body.get("destination_url")
    if not dest_url:
        raise HTTPException(status_code=400, detail="Missing destination_url")
    link = crud.create_link(db, dest_url)
    return {"slug": link.slug, "url": f"/t/{link.slug}"}
