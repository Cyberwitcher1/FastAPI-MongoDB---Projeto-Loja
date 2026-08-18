from fastapi import FastAPI, HTTPException
from routes.route import router
app = FastAPI()
app.include_router(router)

