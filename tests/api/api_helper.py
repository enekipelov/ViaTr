import json


def get_username_from_file(path_to_file):
    with open(path_to_file, "r") as jsonFile:
        data = json.load(jsonFile)

    return data["username"]
