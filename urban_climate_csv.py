import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


class DataSource:

    def read(self, **kwargs):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(kwargs['file_name'])) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                hour = datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour
