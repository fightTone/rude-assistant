import json

def get_creds(platform):
    with open("credentials.json", "r") as file:
        credentials = json.load(file)
        if platform == "chatgpt":
            return credentials["chatgpt"]
        elif platform == "youtube":
            return credentials["youtube"]