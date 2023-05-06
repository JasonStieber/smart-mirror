from secret_keys import TENANT_ID, MS_CLIENT_ID, MS_CLIENT_SECRET

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
    access_token = get_access_token()

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
