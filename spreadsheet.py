
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
            if value[1:].isdigit():
                result = int(value[1:])
            elif value[1:].startswith("'") and value.endswith("'"):
                result = value[2:-1]
            elif value[1:].isidentifier():
                result = self.evaluate(value[1:])
                if isinstance(result, str) and result.startswith("#"):
                    self._evaluating.remove(cell)
                    return result
            else:
                try:
                    result = eval(value[1:], {"__builtins__": None}, {k: self.evaluate(k) for k in self._cells if not self.evaluate(k).startswith("#")})
                    if isinstance(result, float) and not result.is_integer():
                        result = "#Error"
                except:
                    result = "#Error"
        else:
            if value.isdigit():
                result = int(value)
            elif value.startswith("'") and value.endswith("'"):
                result = value[1:-1]
            else:
                result = "#Error"
        self._evaluating.remove(cell)
        return result

