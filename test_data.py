import csv
import json

def test_csv_has_12_columns():
    with open('profiles1.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert len(header) == 12, f"CSV har {len(header)} kolumner, förväntade 12"

def test_csv_has_over_900_rows():
    with open('profiles1.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) > 900, f"CSV har {len(rows)} rader, förväntade >900"

def test_json_has_all_properties():
    with open('data.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
        required = ["id", "name", "age", "address", "city", "zipcode", "phone", "email", "company", "job", "income", "gender"]
        for item in data:
            for key in required:
                assert key in item, f"JSON saknar fält: {key}"

def test_json_has_over_900_rows():
    with open('data.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
        assert len(data) > 900, f"JSON har {len(data)} rader, förväntade >900"