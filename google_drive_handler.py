import gdown
import csv
from .utils import format_result

class GoogleDriveHandler:
    def __init__(self):
        # Ссылка на файл EYEOFGOD.csv на Google Диске
        self.file_url = "https://drive.google.com/uc?id=1MQGnIKw5VKwc9gbOiPJvHNgEgVIQ-AGz"
        self.file_path = "/tmp/EYEOFGOD.csv"

    def download_file(self):
        gdown.download(self.file_url, self.file_path, quiet=False)

    def get_result(self, **kwargs):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            results = []
            for row in reader:
                result = format_result(row, ["id", "phone", "username", "first_name", "last_name"], **kwargs)
                if result:
                    results.append(result)
            return results
