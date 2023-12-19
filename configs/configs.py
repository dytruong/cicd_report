import json

CRED_PATH = "./configs/.credentials.json"


def get_configs(file_path):
    with open(file_path, "r") as json_file:
        res = json.load(json_file)
    return res


bot_token = get_configs(CRED_PATH)["bot_token"]
chat_id = get_configs(CRED_PATH)["chat_id"]
