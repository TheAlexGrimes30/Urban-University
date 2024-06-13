import os


class PriceListManager:
    def __init__(self, directory: str):
        self.directory = directory
        self.data = []

    def load_prices(self):
        for filename in os.listdir(self.directory):
            if 'price' in filename:
                self._load_file(os.path.join(self.directory, filename))

    def _load_file(self, filepath: str):
        pass
