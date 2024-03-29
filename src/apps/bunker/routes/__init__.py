from fastapi import APIRouter

from src.apps.bunker.routes.status_routes import register as register_status_routes
from src.apps.bunker.routes.log_routes import register as register_log_routes


def register_routes(router: APIRouter):
    register_status_routes(router)
    register_log_routes(router)
