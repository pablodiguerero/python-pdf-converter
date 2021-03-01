from application.fastapi import app

from routes import chrome

app.include_router(chrome, tags=["Chrome"])
