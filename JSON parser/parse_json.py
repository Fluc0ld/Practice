import json
import os
from pprint import pprint
from config.definitions import ROOT_DIR


def list_json(json_obj):
    with open(json_obj, 'r') as file:
        json_obj = json.load(file)
    pprint(json_obj, sort_dicts=False)

def create_json(json_obj: (str, dict), json_file: bool = True) -> dict:
    """
    json_file - is a flag for "with" command to not interfere the recursion.
    """
    if json_file is True:
        with open(json_obj, 'r') as file:
            json_obj = json.load(file)

    if isinstance(json_obj, dict):
        if json_obj.get("chargingStrategy"):
            json_obj["chargingStrategy"] = {"channels": ["test1", "test2", "test3"]}
        for key, value in json_obj.items():
            create_json(value, json_file=False)
    elif isinstance(json_obj, list):
        for item in json_obj:
            create_json(item, json_file=False)

    with open("def_eety_ALL_mig_v40_changing_of_chargingStrategy.json", 'w', encoding='utf-8') as file2:
        json.dump(json_obj, file2, indent=4)

    return json_obj


if __name__ == "__main__":

    JSON_FILE = os.path.join(ROOT_DIR, "resources", "def_eety_ALL_mig_v35__change_charging_strategy.json")

    create_json(JSON_FILE)
    # list_json(JSON_FILE)
