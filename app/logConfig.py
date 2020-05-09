LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard_formatter": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "standard_handler": {
            "level": "DEBUG",
            "formatter": "standard_formatter",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/serverlog.log",
            "mode": "a",
            "maxBytes": 1024,
            "backupCount": 1,
        },
        "error_handler": {
            "level": "ERROR",
            "formatter": "standard_formatter",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "app": {
            "handlers": ["standard_handler", "error_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
