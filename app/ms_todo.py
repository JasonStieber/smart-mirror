from config.secret_keys import MS_CLIENT_ID, MS_CLIENT_SECRET
from config.settings import TENANT_ID
import requests

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]
ENDPOINT = "https://graph.microsoft.com/v1.0/me/todo/lists"

def get_access_token():
    app = ConfidentialClientApplication(
        MS_CLIENT_ID, authority=AUTHORITY, client_credential=MS_CLIENT_SECRET
    )
    result = app.acquire_token_for_client(SCOPE)
    return result["access_token"]

def get_default_task_list_id(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        ENDPOINT,
        headers=headers,
    )
    response.raise_for_status()

    lists = response.json()["value"]
    default_list = next((lst for lst in lists if lst["displayName"] == "Tasks"), None)

    if default_list:
        return default_list["id"]
    else:
        raise Exception("Default task list not found.")

def get_tasks_from_todo_list(list_id=None):
    #access_token = get_access_token()
    access_token= "EwB4A8l6BAAUAOyDv0l6PcCVu89kmzvqZmkWABkAAaYEHQvK0HylqJzZGRi7fTEqeudt/poD1i0G5GVM5+mtjXhEbHFgmPKvELFMP9SLGBrEMQbQxh2SVJm4+dINxvJEIioueimQ1TABTOjXo6nl61nJRetmMLguu9N3TLNwJWtvIqPNPbDvDSpwI5MKTaD1HFFSUL1K0XqX0AtXP3A3J9dDkp9xXMi1aK+d+oZaHuVz7Eudp33LPm7wHZS//0SUC40etZku9P+X+5E502VFCqc//x6s5rO7V12cgFC8GFa6peYVKkLx0mvnVYuyDNof+/aHlMk4cFqWCJiVb1GJ0n6rU97cBcdF3GTko9vRO4IiJlSiq9nKgQtw9Sn0NU0DZgAACLArc6tKfgIWSAIljMrE7LgMgGfrIS/DSofoGf0h4podpJd/EvkZbOfN1I0SK6ESVL1CqVjuOdeGridp5Rg/ECX+3edbtHVcjKDHzuZi5lIeFbBsdA99euooSmGfSUE5s6N9rqS4HcUV17tiI08kGhuZWgF/8wiWxmTY88beh3herSHv1wYZpB/VRJbi3wBxW0SUf1bJKJvQVIqLC+CjQOCTmHDnr65c3HDrvtmJ5i9T3OsTgsO+KDeFWlj1SOj8OP52KQ6G1BGIJLy/lqKCQ0BgT1rfOWn2VBqsvW8ioEAIxkpMqMmrY3rbSQW0fRTiDHxaE+hSpqKPunI0at7LNIZytIpSWEzZCcST4aE1DtnyuizQEVZ/jrgUDE2I+U+w+QXrLVKzTrS7RE0swRAOPXpgmytolH8z8d6YCTlxWr/bGyHHRpLCKqQusA9T/Tp6ad1bFYNyjV1/cpHGWT+7qo/J1QZoNY5Rp5hEmCaszBIewczmc546WacWYO6SHpS6D2t/0LdjpP3h3XgN4N6wJbmdmMGQiOoCK8E4kgg9A8TvTNQAwvdXTas569ELTWTpAVkmyswLOeb64yC9e484noyAWDTkSkxilok7iNz603a1qftW0tRqqWuY9ythOE8NXn81mvremDi0el4n0kHVibRGGU/fZTYw+B/2k4ONedJOVCLHYn4+nsHEiGaxeiYS8JZpuyWysuAsP9Krfrt1nIl7qo9PPmOpx1/jdPcZGyr4AwPfSL1jGckhxBAIpv0jC6V0PsfFuE4g4ss0Duan98zASX4C"
    if list_id is None:
        # Get the default Task list
        list_id = get_default_task_list_id(access_token)

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(
        f"{ENDPOINT}/{list_id}/tasks",
        headers=headers,
    )
    response.raise_for_status()

    return response.json()["value"]


def add_task_to_todo_list(task_name, list_id=None):
    access_token = get_access_token()

    if list_id is None:
        # Get the default Task list
        list_id = get_default_task_list_id(access_token)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
        "subject": task_name,
    }

    response = requests.post(
        f"{ENDPOINT}/{list_id}/tasks",
        headers=headers,
        json=data,
    )
    response.raise_for_status()

    return response.json()
