import json


class IO:
    """Save to and load from a given file, for JSON-formatted/serializable data."""
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(filename, 'w') as file:
            print('Saving')
            json.dump(data, file)

    def load(self):
        with open(filename, 'r') as file:
            print('Loading')
            data = json.load(file)
            return data

