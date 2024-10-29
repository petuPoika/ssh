
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.isdigit():
            return int(value)
        elif value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        elif value.startswith("='") and value.endswith("'"):
            return value[2:-1]
        elif value.startswith("="):
            return value[1:]
        else:
            try:
                float(value)
                return "#Error"
            except ValueError:
                return "#Error"

