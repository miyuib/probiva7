import csv
from .utils import format_result

class CSVHandler:
    def __init__(self, directory, schema):
        self.directory = directory
        self.schema = schema

    def set_directory(self, directory):
        self.directory = directory

    def get_result(self, **kwargs):
        with open(self.directory, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            results = []
            for row in reader:
                result = format_result(row, self.schema, **kwargs)
                if result:
                    results.append(result)
            return results
