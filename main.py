from __future__ import print_function
from auth import auth
from sheets import raiseUsedDay
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

def main():
    creds = auth()
    raiseUsedDay(-0.3, "오경택", creds)
if __name__ == '__main__':
    main()