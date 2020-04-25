from typing import Optional


class SingletonMeta(type):
    _instance: Optional[object] = None

    def __call__(cls, *args, **kwargs) -> object:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
