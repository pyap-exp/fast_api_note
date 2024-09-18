from fastapi import FastAPI

from .routers import notes, tags, users

app = FastAPI(dependencies=[])

@app.get("/health")
async def health():
    return {"message": "Your application is working"}

app.include_router(notes.router)
app.include_router(tags.router)
app.include_router(users.router)
