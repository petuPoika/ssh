
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        value = self.get(cell)
        if value.startswith("="):
            if value.startswith("='") and value.endswith("'"):
                result = value[2:-1]
            elif value[1:].isdigit():
                result = int(value[1:])
            elif value[1:].isidentifier():
                result = self.evaluate(value[1:])
            elif value[1:].replace('+', '').replace('-', '').replace('*', '').replace('/', '').isdigit():
                result = eval(value[1:])
            else:
                result = "#Error"
        elif value.isdigit():
            result = int(value)
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        else:
            result = "#Error"
        self._evaluating.remove(cell)
        return result

