# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path
import pickle
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import post, get

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
            print(creds)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    d = datetime.utcnow().date()
    tomorrow = datetime(d.year, d.month, d.day, 10) + timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()
    body = {
        "summary": "Hello there, Automating calendar",
        "description": "Google calendar with python",
        "start": {"dateTime": start, "timeZone": "America/Sao_Paulo"},
        "end": {"dateTime": end, "timeZone": "America/Sao_Paulo"},
    }
    SUBJECT = "user-1@company.com"
    event = service.events().insert(calendarId=SUBJECT, body=body).execute()

    if not events:
        print("No upcoming events found.")
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])


def get_access_token():

    response = post(
        url="https://www.googleapis.com/oauth2/v4/token",
        data={
            "client_id": "262074736566-6hi4f9cq5ujuogfef28urm7nvsnmihsc.apps.googleusercontent.com",
            "client_secret": "jL54jrvPROhlmKqDbYt7zMDE",
            # 'refresh_token': 'REFRESH_TOKEN',
            # 'grant_type': 'refresh_token',
        },
        headers={"Content-Type": "application/x-www-form-urlencoded", },
    )
    response.raise_for_status()
    print(response.json().get("access_token"))


def get_calendar_id():
    ACCESS_TOKEN = \
        "ya29.a0AfH6SMDFya2gGGf9fzJx_cJ10r0eCJSKjHb9LkxPnGimE3a_HPgY5O0hq5iHjb0jXOcHEwLa9IQu71YYypWsSBx2sSpKw7KdeRlC" \
        "gBby77ZfGEmjbm_iBQIWQ_QjTl5pREs1HdtZuLIR-uUjF1kgOcch5aaJpaPc0T8"
    response = get(
        url="https://www.googleapis.com/calendar/v3/users/me/calendarList",
        headers={"Authorization": f"Bearer {ACCESS_TOKEN}", },
    )
    response.raise_for_status()

    calendar_id = None
    for calendar in response.json().get("items"):
        if calendar["summary"] == "CALENDAR_NAME":
            calendar_id = calendar["id"]
            break

    print(calendar_id)


def create_new_event():

    response = post(
        url="https://www.googleapis.com/calendar/v3/calendars/CALENDAR_ID/events/quickAdd",
        data={"text": "EVENT_TEXT", },
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer ACCESS_TOKEN",
        },
    )
    response.raise_for_status()
    print(response.json())


def teste():
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    SERVICE_ACCOUNT_FILE = (
        "credentials.json"  # You should make it an environment variable
    )
    SUBJECT = "user-1@company.com"
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    delegated_credentials = credentials.with_subject(SUBJECT)
    service = build("calendar", "v3", credentials=delegated_credentials)

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)
    now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    events = (
        service.events()
        .list(
            calendarId=SUBJECT,
            timeMin=now,
            maxResults=10,
            orderBy="startTime",
            singleEvents=True,
        )
        .execute()
    )
    print(events)


if __name__ == "__main__":
    # main()
    teste()
    # create_new_event()
    # get_calendar_id()
    # get_access_token()
