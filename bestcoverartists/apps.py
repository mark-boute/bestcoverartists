import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class BCAWebsiteConfig(AppConfig):
    name = "bestcoverartists"
