import csv
import json

def test_json_has_all_properties():
    with open('data.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
        required = [
            "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
        ]
        for item in data:
            for key in required:
                assert key in item, f"JSON saknar fält: {key}"
