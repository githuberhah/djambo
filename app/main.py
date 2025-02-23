from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from scraper import scrape_books
from database import save_books, init_db

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
init_db()

@app.get("/api/books")
def get_books():
    books = scrape_books()
    save_books(books)
    return books

@app.post("/api/update")
def update_books():
    books = scrape_books()
    save_books(books)
    return {"status": "updated", "count": len(books)}