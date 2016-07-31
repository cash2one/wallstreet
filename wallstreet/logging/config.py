from __future__ import absolute_import
import os
from wallstreet import base
from wallstreet import config

LOG_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../logs")
base.wise_mk_dir(LOG_ROOT)

CELEY_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'socket': {
            'class': 'logging.handlers.SocketHandler',
            'level': 'DEBUG',
            'host': config.get("log_server", "host"),
            'port': config.get_int("log_server", "port")
        }
    },
    'loggers': {
        'wallstreet.tasks.stock_history_tasks': {
            'handlers:': ['socket']
        },
        'wallstreet.tasks.stock_storage_tasks': {
            'handlers:': ['socket']
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'normal': {
                'format': '[%(asctime)s]%(levelname)s,%(funcName)s,%(lineno)d,%(message)s'
            },
        },
    'handlers': {
        'console': {
            'formatter': 'normal',
            'class': 'logging.StreamHandler',
            'level': 'DEBUG'
        },
        'root': {
            'formatter': 'normal',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': "DEBUG",
            'filename': os.path.join(LOG_ROOT, "default.log"),
            'when': "D",
            'interval': 1
        }
    },
    'loggers': {
        'default': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG'
        }
    }
}