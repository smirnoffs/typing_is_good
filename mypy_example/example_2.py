from typing import Iterable, List


class Collector:
    def __init__(self):
        self._container: List[int] = []

    def add(self, el: int):
        self._container.append(el)

    def even(self) -> Iterable[int]:
        return tuple(el for el in self._container if el % 2 == 0)


if __name__ == "__main__":
    collector = Collector()
    for i in range(0, 100):
        collector.add(i * 0.3)
    print(collector.even())
