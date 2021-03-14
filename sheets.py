import os
from pprint import pprint

from googleapiclient import discovery
from google.oauth2.credentials import Credentials
from env import VALUE_COLUMN_INDEX, SHEET_ID, REAL_NAME_COLUMN_INDEX, RANGE

def findRow(rows:list, real_name:str)->list:
    for row in rows:
        if row[REAL_NAME_COLUMN_INDEX] == real_name:
            return row
    raise Exception("일치하는 행이 없습니다.")

def raiseUsedDay(days: float, real_name: str, credentials):
    service = discovery.build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = SHEET_ID
    range_ = RANGE

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_)
    response = request.execute()
    row = findRow(response["values"], real_name)
    value = row[VALUE_COLUMN_INDEX]

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range="I4", valueInputOption="USER_ENTERED", body={"values": [[str(float(value) + days)]]}
    ).execute()
    pprint(result)

