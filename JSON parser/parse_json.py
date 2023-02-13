import json
import os
from pprint import pprint
from config.definitions import ROOT_DIR


def print_tree(json_obj: (str, dict), indent: int = 0, json_file: bool = True) -> dict:
    """
    json_file - is a flag for "with" command to not interfere the recursion.
    """

    if json_file is True:
        with open(json_obj, 'r') as file:
            json_obj = json.load(file)

    if isinstance(json_obj, dict):
        if json_obj.get("chargingStrategy"):
            json_obj["chargingStrategy"] = ["OCS_BALANCE", "PAYMENT_LEGACY", "PAYMENT"]
        for key, value in json_obj.items():
            print(" " * indent + str(key))
            print_tree(value, indent+4, json_file=False)
    elif isinstance(json_obj, list):
        for item in json_obj:
            print_tree(item, indent+4, json_file=False)
    else:
        print(" " * indent + str(json_obj))

    return json_obj

def create_json(json_obj: (str, dict), json_file: bool = True) -> dict:

    if json_file is True:
        with open(json_obj, 'r') as file:
            json_obj = json.load(file)

    if isinstance(json_obj, dict):
        if json_obj.get("chargingStrategy"):
            json_obj["chargingStrategy"] = {"channels": ["OCS_BALANCE", "PAYMENT_LEGACY", "PAYMENT"]}
        for key, value in json_obj.items():
            create_json(value, json_file=False)
    elif isinstance(json_obj, list):
        for item in json_obj:
            create_json(item, json_file=False)
    else:
        pass

    return json_obj


if __name__ == "__main__":

    JSON_FILE = os.path.join(ROOT_DIR, "def_eety_ALL_mig_v39_remove_channels_spezial.json")

    a = create_json(JSON_FILE)
    pprint(a)
    with open("def_eety_ALL_mig_v40_changing_of_chargingStrategy.json", 'w', encoding='utf-8') as file2:
        json.dump(a, file2, indent=4)

    # create_json(JSON_FILE)
