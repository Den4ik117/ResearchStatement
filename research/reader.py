from csv import DictReader
from typing import Iterator


def csv_reader(filename: str) -> Iterator[dict[str, str]]:
    with open(filename, mode='r') as file:
        reader = DictReader(file)
        for row in reader:
            yield row
