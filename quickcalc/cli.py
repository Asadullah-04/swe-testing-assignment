import sys
from typing import List

from quickcalc.core import evaluate_sequence


def main(argv: List[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    if not argv:
        print("Quick-Calc CLI")
        print('Usage: python -m quickcalc.cli "5 + 3 ="')
        return 1

    expr = " ".join(argv)
    tokens = expr.split()
    print(evaluate_sequence(tokens))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())