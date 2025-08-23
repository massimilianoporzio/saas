import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def home_view(request, *args, **kwargs):
    my_title = "Home Page2"
    my_context = {"page_title": my_title, "request": request}
    logger.debug("Home view accessed")
    # Assuming you have a template named 'home.html' in your templates directory
    html_file = "home.html"
    return render(request, html_file, my_context)
