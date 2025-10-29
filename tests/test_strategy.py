from __future__ import annotations

from src.strategy_pattern.strategy import UpperCaseStrategy, ReverseStrategy, Rot13Strategy, LeetStrategy
from src.strategy_pattern.context import TextTransformer


def test_uppercase():
    s = UpperCaseStrategy()
    assert s.transform('Abc 123') == 'ABC 123'


def test_reverse():
    s = ReverseStrategy()
    assert s.transform('abc') == 'cba'


def test_rot13():
    s = Rot13Strategy()
    assert s.transform('abc') == 'nop'
    # rot13 twice -> original
    assert s.transform(s.transform('Hello')) == 'Hello'


def test_leet():
    s = LeetStrategy()
    # 'T'->7, 'e'->3, 's'->5, 't'->7
    assert s.transform('Test') == '7357'


def test_context_switching():
    ctx = TextTransformer(UpperCaseStrategy())
    assert ctx.transform('a') == 'A'
    ctx.set_strategy(ReverseStrategy())
    assert ctx.transform('ab') == 'ba'
