from __future__ import annotations

from typing import Optional
from .strategy import TextStrategy


class TextTransformer:
    """Контекст, использующий стратегию для преобразования текста.

    Простой и понятный интерфейс:
    - set_strategy(strategy)
    - transform(text) -> str
    """

    def __init__(self, strategy: Optional[TextStrategy] = None):
        self._strategy = strategy

    def set_strategy(self, strategy: TextStrategy) -> None:
        if strategy is None:
            raise ValueError("strategy must not be None")
        self._strategy = strategy

    def transform(self, text: str) -> str:
        if self._strategy is None:
            raise RuntimeError("No strategy set")
        return self._strategy.transform(text)
