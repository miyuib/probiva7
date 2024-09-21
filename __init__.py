from .csv_handler import CSVHandler
from .google_drive_handler import GoogleDriveHandler

class Probiva7:
    def __init__(self):
        self.csv_handler = None
        self.source_type = None

    def set_csv_origin(self):
        self.source_type = "origin"
        self.csv_handler = GoogleDriveHandler()
        self.csv_handler.download_file()

    def set_csv_local(self, directory, schema):
        self.source_type = "local"
        self.csv_handler = CSVHandler(directory, schema)

    def set_directory(self, directory):
        if self.source_type == "local":
            self.csv_handler.set_directory(directory)
        else:
            raise ValueError("Directory can only be set for local CSV.")

    def get_result(self, **kwargs):
        if not self.csv_handler:
            raise ValueError("CSV source is not set.")
        return self.csv_handler.get_result(**kwargs)
