class EvenNumbersIterator:
    def __init__(self, start=0, end=1):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            even_number = self.current
            self.current += 2
            return even_number
        else:
            raise StopIteration


iterator = EvenNumbersIterator(10, 25)
for i in iterator:
    print(i)
