class EventIdGenerator:

    def __init__(self):
        self._counter = 0

    def generate(self) -> str:
        self._counter += 1
        return f"evt_{self._counter:06d}"