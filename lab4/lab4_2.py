# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        data = [row for row in csv_reader]
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_f:
        json.dump(data, json_f, indent=4)


if __name__ == '__main__':

    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
