from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title="Rectifex Analyzer API",
    version="3.0.0"
)

# Create a router for the API endpoints to keep them separate
api_router = APIRouter(prefix="/api/v1")

@api_router.get("/health", tags=["Status"])
def get_health():
    """
    Gibt den Systemstatus zurück.
    """
    return {"status": "ok"}

# Include the API router in the main app
app.include_router(api_router)

# Hier werden später die weiteren API-Routen (Router) eingebunden.

# --- Static Files Mount for Frontend ---
# This serves the compiled React frontend. It's designed for the production/Flatpak build.
# The `flatpak-builder` will copy the frontend's `dist` directory to '/app/static'.
# We use an absolute path to ensure it's found correctly within the Flatpak sandbox.
# The StaticFiles middleware will then serve index.html for any path that is not an API route.
# We check for the directory's existence to avoid errors during development when it's not present.
static_dir = "/app/static"  # Use absolute path for Flatpak
if os.path.isdir(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="app")