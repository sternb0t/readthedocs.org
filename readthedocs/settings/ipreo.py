import os

from .dev import CommunityDevSettings


class IpreoSettings(CommunityDevSettings):

    ALLOW_PRIVATE_REPOS = True
    # DEBUG = False
    # TEMPLATE_DEBUG = False

    # HAYSTACK_CONNECTIONS = {
    #     'default': {
    #         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    #         'URL': 'http://127.0.0.1:9200/',
    #         'INDEX_NAME': 'readthedocs',
    #     },
    # }

    SLUMBER_API_HOST = 'http://ipreo-readthedocs.eastus.cloudapp.azure.com:8000'
    PRODUCTION_DOMAIN = 'ipreo-readthedocs.eastus.cloudapp.azure.com:8000'
    WEBSOCKET_HOST = 'ipreo-readthedocs.eastus.cloudapp.azure.com:8000'

    # DOCKER_ENABLED = True
    # DOCKER_IMAGE = "rtfd-build:base"
    # DOCKER_SOCKET = "/var/run/docker.sock"
    # DOCKER_VERSION = "1.23"
    # DOCKER_LIMITS = {}

IpreoSettings.load_settings(__name__)
