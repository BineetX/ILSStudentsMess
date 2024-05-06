import pandas as pd
import bineet.files as bf
import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from googleapiclient.http import MediaFileUpload
import argparse

def load_credentials():
        if os.path.exists('reqs/token.pickle'):
            with open('reqs/token.pickle', 'rb') as token:
                creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    raise Exception("No valid credentials provided.")
            return creds
        else:
            raise FileNotFoundError("Token.pickle file not found.")

def fetch_sheet_data(creds, spreadsheet_id):

        service = build('sheets', 'v4', credentials=creds)

        sheet_metadata = service.spreadsheets().get(
            spreadsheetId=spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', '')
        title = sheets[0]['properties']['title']  # Assuming the first sheet
        grid_properties = sheets[0]['properties']['gridProperties']
        row_count = grid_properties['rowCount']
        column_count = grid_properties['columnCount']

        range_name = f"{title}!A1:{chr(64 + column_count)}{row_count}"

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            df = pd.DataFrame(values)
            df.columns = df.iloc[0]  # Set the first row as header
            # df = df[1:]  # Remove the header row from data
            # # Optionally, drop rows and columns where all elements are NaN
            # df.dropna(how='all', axis=1, inplace=True)
            # df.dropna(how='all', axis=0, inplace=True)
            return df

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--sheetlink",
                        help="Link of the response", default=None)
args = parser.parse_args()
link_path = args.sheetlink

creds = load_credentials()
spreadsheet_id = link_path.split("/d/")[1].split("/")[0]
list_temp = list(fetch_sheet_data(creds, spreadsheet_id)["Registered Email Address"])
our_dict = pd.read_csv("/home/bineet/StudentsMess/FinalScripts/Active_Members_new.csv")
closed_dict = pd.read_csv("/home/bineet/StudentsMess/FinalScripts/Closed_Members.csv")

# print(list_temp)
our_dict = our_dict.set_index("Registered Email Address")
closed_dict = closed_dict.set_index("Registered Email Address")
# print(our_dict.index)

for i in our_dict.index:
    if (i not in list_temp) and (i not in closed_dict.index.to_list()):
        print(our_dict.loc[i]["Name"].title())