from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class TextStrategy(ABC):
    """Абстрактная стратегия для преобразования текста.

    Контракт:
    - transform(text: str) -> str
    - не меняет состояние (stateless)
    - выбрасывает ValueError для None
    """

    @abstractmethod
    def transform(self, text: str) -> str:
        if text is None:
            raise ValueError("text must not be None")


class UpperCaseStrategy(TextStrategy):
    def transform(self, text: str) -> str:
        super().transform(text)
        return text.upper()


class ReverseStrategy(TextStrategy):
    def transform(self, text: str) -> str:
        super().transform(text)
        return text[::-1]


class Rot13Strategy(TextStrategy):
    def transform(self, text: str) -> str:
        super().transform(text)
        def rot13_char(c: str) -> str:
            o = ord(c)
            if 65 <= o <= 90:
                return chr((o - 65 + 13) % 26 + 65)
            if 97 <= o <= 122:
                return chr((o - 97 + 13) % 26 + 97)
            return c

        return ''.join(rot13_char(c) for c in text)


class LeetStrategy(TextStrategy):
    """Простая реализация 'leet' преобразования для демонстрации."""

    _MAP: Dict[str, str] = {
        'a': '4', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
        't': '7', 'T': '7',
    }

    def transform(self, text: str) -> str:
        super().transform(text)
        return ''.join(self._MAP.get(c, c) for c in text)
