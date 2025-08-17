from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home_view(request, *args, **kwargs):
    logger.debug("Home view accessed")
    logger.info("Rendering home page")
    logger.warning("Potential issue detected")
    logger.error("Error occurred while processing request")
    logger.critical("Critical issue occurred")
    return HttpResponse("<h1>Welcome to the Home Page</h1>")
