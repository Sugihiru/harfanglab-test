import logging
import os

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app import database
from app.routers import video_games
from app.tags_metadata import tags_metadata

app = FastAPI(title="VideoGameDB", openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["Content-Type", "Authorization"],
)

database.Base.metadata.create_all(bind=database.engine)

# Setup logging
# setting = Settings()
# if setting.environment == "production":
#     setup_logging()
#     app.add_middleware(LoggingMiddleware)
# else:
#     logger.setLevel(logging.DEBUG)


# Add logs on HTTP 422 Unprocessable Entity
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"Body: {exc.body} / Error: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


# Setup routers
for router in (video_games.router,):
    app.include_router(router)
