"""Простой CLI для демонстрации использования Strategy pattern.

Запуск:
python -m src.strategy_pattern.cli --strategy upper "hello world"
"""

from __future__ import annotations

import argparse
from typing import Dict

from .strategy import UpperCaseStrategy, ReverseStrategy, Rot13Strategy, LeetStrategy
from .context import TextTransformer


STRATEGIES: Dict[str, type] = {
    'upper': UpperCaseStrategy,
    'reverse': ReverseStrategy,
    'rot13': Rot13Strategy,
    'leet': LeetStrategy,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='text-transformer')
    parser.add_argument('--strategy', '-s', choices=STRATEGIES.keys(), required=True,
                        help='Выберите стратегию преобразования')
    parser.add_argument('text', help='Входной текст', nargs='+')

    args = parser.parse_args(argv)
    text = ' '.join(args.text)

    strategy_cls = STRATEGIES[args.strategy]
    transformer = TextTransformer(strategy_cls())
    result = transformer.transform(text)
    print(result)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
