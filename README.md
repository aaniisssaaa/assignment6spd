# Assignment 6 — Strategy Pattern Implementation

## Overview
This project demonstrates the Strategy design pattern through a text transformation CLI application implemented in Python 3.8+.

## Implementation Details
The implementation follows the classic Strategy pattern structure:
- **Strategy Interface**: `TextStrategy` with abstract method `transform(text: str) -> str`
- **Concrete Strategies**: Four different text transformation algorithms
- **Context**: `TextTransformer` class that delegates transformation to the current strategy
- **Clean Code Principles**: Single responsibility, clear naming conventions, proper error handling

## Project Structure
```
src/strategy_pattern/
├── __init__.py          # Package initialization
├── strategy.py          # Strategy interface and concrete implementations
├── context.py           # Context class (TextTransformer)
└── cli.py              # Command-line interface demonstration

tests/
└── test_strategy.py     # Unit tests

uml/
└── diagram.puml         # UML class diagram
```

## Concrete Strategies
1. **UpperCaseStrategy** - Converts text to uppercase
2. **ReverseStrategy** - Reverses string characters
3. **Rot13Strategy** - Caesar cipher with 13-character shift
4. **LeetStrategy** - Substitutes letters with similar-looking numbers

## Installation and Usage
1. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

2. Run tests:
```bash
python -m pytest -q
```

3. CLI usage example:
```bash
python -m src.strategy_pattern.cli --strategy upper "hello world"
```

## UML Diagram
The UML class diagram is available in `uml/diagram.puml` and can be rendered using PlantUML tools or online services.

## Key Design Benefits
- **Extensibility**: New strategies can be added without modifying existing code
- **Runtime flexibility**: Strategies can be changed dynamically
- **Testability**: Each strategy is independently testable
- **Clean separation**: Algorithm implementation is decoupled from client code
