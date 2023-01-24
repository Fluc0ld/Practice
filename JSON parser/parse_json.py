import json
import os
from config.definitions import ROOT_DIR


def print_tree(json_obj: (str, dict), indent: int = 0, json_file: bool = True) -> dict:
    """
    json_file - is a flag for "with" command to not interfere the recursion.
    """

    if json_file is True:
        with open(json_obj, 'r') as file:
            json_obj = json.load(file)

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            print(" " * indent + str(key))
            print_tree(value, indent+4, json_file=False)
    elif isinstance(json_obj, list):
        for item in json_obj:
            print_tree(item, indent+4, json_file=False)
    else:
        print(" " * indent + str(json_obj))

    return json_obj


if __name__ == "__main__":

    JSON_FILE = os.path.join(ROOT_DIR, "resources", "def_eety_ALL_mig_v35__change_charging_strategy.json")

    print_tree(JSON_FILE)
