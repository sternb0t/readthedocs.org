import os

from .dev import CommunityDevSettings


class IpreoSettings(CommunityDevSettings):

    ALLOW_PRIVATE_REPOS = True
    DEBUG = False
    TEMPLATE_DEBUG = False

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'readthedocs',
        },
    }

IpreoSettings.load_settings(__name__)
