import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from db import db, engine
from routes.api import router as api_router

from src.dependencies import database


db.metadata.create_all(bind = engine)

app = FastAPI(dependencies=[Depends(database.get_db)])

origins = ["http://localhost:8086"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8086, log_level="info", reload=True)
    print("running")
