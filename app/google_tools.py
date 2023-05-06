import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_credentials():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = Credentials.from_authorized_user_info(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/jason/Documents/projects/smart_mirror/app/config/google_client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds.to_json(), token)
    return creds

def get_events_today(credentials):
    service = build('calendar', 'v3', credentials=credentials)
    calendar_id = 'primary'

    now = datetime.utcnow()
    start_of_day = datetime.combine(now.date(), time(0, 0)).isoformat() + 'Z'
    end_of_day = datetime.combine(now.date(), time(23, 59, 59)).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=start_of_day,
        timeMax=end_of_day,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])


print(get_events_today(get_credentials()))