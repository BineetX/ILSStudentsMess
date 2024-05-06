#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This program is created by Bineet Kumar Mohanta
# To generate readable and simplified stats for the students mess

# Insatlling and Importing Dependencies if needed
import pip
import argparse
from datetime import datetime
import time
import os
import getpass
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from googleapiclient.http import MediaFileUpload

import tempfile
import shutil

VEG_NONVEG_DICT = {
    "Monday": "None",
    "Tuesday": "Lunch",
    "Wednesday": "Lunch",
    "Thursday": "None",
    "Friday": "Lunch",
    "Saturday": "None",
    "Sunday": "Lunch"
}


class Response():

    def __init__(self):
        pass

    def get_time():
        # time = datetime.now().strftime("%d-%B-%Y-%H-%M-%p")
        time = datetime.now().strftime("%d-%B-%H-%p")
        return time

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

    def AnalyzeDay(self, habit,is_nv= True, not_sunday=True):
        habit = str(habit)
        tmp = {}
        
        if "Breakfast" in habit:
            tmp.update({"Breakfast": "✓"})
        else:
            tmp.update({"Breakfast": "OFF"})
        if "Lunch" in habit:
            tmp.update({"Lunch": "✓"})
        else:
            tmp.update({"Lunch": "OFF"})
        if ("Dinner" in habit) and not_sunday:
            tmp.update({"Dinner": "✓"})
        else:
            tmp.update({"Dinner": "OFF"})
        pref = habit.split(",")[-1]
        if is_nv:
            if "Non Veg" in pref:
                tmp.update({"Preference": "Non Veg"})
            else:
                tmp.update({"Preference": "Veg"})
        else:
            tmp.update({"Preference": "Base"})
        print(is_nv, tmp["Preference"])
        return tmp

    def IsNonVeg(day,VEG_NONVEG_DICT=VEG_NONVEG_DICT):
        if VEG_NONVEG_DICT[day] == 'None':
            return False
        else:
            return True
        

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

    def GenerateSheets(self, menu_response):
        menu_response_keyed = menu_response.set_index(
            "Registered Email Address")
        menu_response_keyed = menu_response_keyed[~menu_response_keyed.index.duplicated(
            keep='last')]
        for day in menu_response_keyed.columns:
            if day.startswith(" ["):
                sheet_name = day.replace(
                    " [", '').replace("]", "").replace("/", "-")
                final_dict = {}
                for user in menu_response_keyed.index:
                    user_dict = {}
                    
                    if "Sunday" in day:
                        isnv = Response.IsNonVeg("Sunday")
                        # print(isnv)
                        habit = str(menu_response_keyed.loc[user][day])
                        print("Sunday")
                        user_dict.update(self.AnalyzeDay(
                            habit,is_nv=isnv, not_sunday=False))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Monday" in day:
                        isnv = Response.IsNonVeg("Monday")
                        # print(isnv)
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,is_nv=isnv))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Tuesday" in day:
                        isnv = Response.IsNonVeg("Tuesday")
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,is_nv=isnv))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Wednesday" in day:
                        isnv = Response.IsNonVeg("Wednesday")
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,is_nv=isnv))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Thursday" in day:
                        isnv = Response.IsNonVeg("Thursday")
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,is_nv=isnv))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Friday" in day:
                        isnv = Response.IsNonVeg("Friday")
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,is_nv=isnv))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Saturday" in day:
                        isnv = Response.IsNonVeg("Saturday")
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,is_nv=isnv))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower(
                            ).title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)

                final_df = pd.DataFrame.from_dict(final_dict).T
                # final_df.index.name = "Name"
                final_df["Name"] = final_df.index

                final_df = final_df.sort_values("Name")
                final_df['Sl No'] = range(1, len(final_df)+1)
                final_df = final_df.set_index("Sl No")
                final_df.index.name = "Sl No"
                final_df = final_df[['Name', 'Breakfast',
                                     'Lunch', 'Dinner', 'Preference']]
                print(final_df)
                final_df.to_csv(f"{op_path}/Daywise_Sheets/{sheet_name}.csv")
                print(f"generate the Day Wise Sheet for {sheet_name}")
        print("\ngenerated the Bill for the term")

    def create_paths():  # ! Can Be Imporved
        maker_name = getpass.getuser()
        current_path = os.getcwd()
        path = Response.get_time()
        op_path = current_path + f"/Generated_by_{maker_name}_on_" + path

        try:
            os.mkdir(f"{op_path}")
            os.mkdir(f"{op_path}/Daywise_Sheets")
        except:
            print("Path already existed")
        # print(op_path)
        print(f"Created the directories at :{op_path}")
        return op_path

    def GenerateStats(op_path, reference_dict):
        files = os.listdir(f"{op_path}/Daywise_Sheets")
        files.sort()
        from_date = files[0].split(" - ")[0]
        to_date = files[-1].split(" - ")[0]
        with open(f"{op_path}/HeadCounts_{from_date}_to_{to_date}.csv", "w") as op:
            op.write("Date,Day,Breakfast,Lunch,Dinner,Veg-in-breakfast,Veg-in-Lunch,Veg-in-Dinner,NonVeg-in-breakfast,NonVeg-in-Lunch,NonVeg-in-Dinner")
            for i in files:
                file = pd.read_csv(f"{op_path}/Daywise_Sheets/{i}")
                name = i.replace(".csv", "")
                total_strength = len(file)
                total_breakfast_off = len(file[file["Breakfast"] == "OFF"])
                total_lunch_off = len(file[file["Lunch"] == "OFF"])
                total_dinner_off = len(file[file["Dinner"] == "OFF"])
                total_breakfast_on = total_strength - total_breakfast_off
                total_lunch_on = total_strength - total_lunch_off
                total_dinner_on = total_strength - total_dinner_off

                day = i.split(" - ")[1].split(".")[0]
                # print(day)
                if reference_dict[day] == "Lunch":
                    non_veg_in_lunch = len(
                        file[(file["Preference"] == "Non Veg") & (file["Lunch"] != "OFF")])
                    veg_in_lunch = total_lunch_on - non_veg_in_lunch
                    non_veg_in_dinner = 0
                    veg_in_dinner = total_dinner_on

                    non_veg_in_breakfast = 0
                    veg_in_breakfast = total_breakfast_on
                elif reference_dict[day] == "Dinner":
                    non_veg_in_lunch = 0
                    veg_in_lunch = total_lunch_on

                    non_veg_in_dinner = len(
                        file[(file["Preference"] == "Non Veg") & (file["Dinner"] != "OFF")])
                    veg_in_dinner = total_dinner_on - non_veg_in_dinner

                    non_veg_in_breakfast = 0
                    veg_in_breakfast = total_breakfast_on

                elif reference_dict[day] == "Breakfast":
                    non_veg_in_lunch = 0
                    veg_in_lunch = total_lunch_on

                    non_veg_in_dinner = 0
                    veg_in_dinner = total_dinner_on

                    non_veg_in_breakfast = len(
                        file[(file["Preference"] == "Non Veg") & (file["Breakfast"] != "OFF")])
                    veg_in_breakfast = total_breakfast_on - non_veg_in_breakfast
                else:
                    non_veg_in_lunch = 0
                    veg_in_lunch = total_lunch_on

                    non_veg_in_dinner = 0
                    veg_in_dinner = total_dinner_on

                    non_veg_in_breakfast = 0
                    veg_in_breakfast = total_breakfast_on

                name_parts = name.split(" - ")
                # print(name_parts)
                op.write(f"\n{name_parts[0]},{name_parts[1]},{total_breakfast_on},{total_lunch_on},{total_dinner_on},{veg_in_breakfast},{veg_in_lunch},{veg_in_dinner},{non_veg_in_breakfast},{non_veg_in_lunch},{non_veg_in_dinner}")
        print("Generated day wise required meal counts sheet for the mess members")


class Upload:
    def find_or_create_folder(service, parent_id, folder_name):

        query = f"name='{folder_name}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder'"
        results = service.files().list(q=query, fields='files(id, name)').execute()
        folders = results.get('files', [])

        if not folders:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_id]
            }
            folder = service.files().create(body=folder_metadata, fields='id').execute()
            return folder.get('id')
        return folders[0]['id']

    def upload_or_convert_to_sheets(service, folder_id, file_path, file_name, format_service):
        file_metadata = {
            'name': file_name.rsplit('.', 1)[0],
            'parents': [folder_id],
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        media = MediaFileUpload(os.path.join(
            file_path, file_name), mimetype='text/csv')

        query = f"name='{file_name.rsplit('.', 1)[0]}' and '{folder_id}' in parents and mimeType='application/vnd.google-apps.spreadsheet'"
        response = service.files().list(q=query, fields='files(id, name)').execute()
        files = response.get('files', [])

        if files:

            update_file = service.files().update(
                fileId=files[0]['id'],
                media_body=media,
                fields='id'
            ).execute()
            Upload.format_google_sheet(format_service, update_file['id'])
            print(f"Updated {file_name} with file ID: {update_file['id']}")
        else:

            file = service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            Upload.format_google_sheet(format_service, file['id'])
            print(
                f"Uploaded {file_name} and converted to Sheets with file ID: {file['id']}")
            
    def upload_to_headcounts(service, folder_id, file_path, file_name, format_service):
        file_metadata = {
            'name': file_name.rsplit('.', 1)[0],
            'parents': [folder_id],
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        media = MediaFileUpload(os.path.join(
            file_path, file_name), mimetype='text/csv')

        query = f"name='{file_name.rsplit('.', 1)[0]}' and '{folder_id}' in parents and mimeType='application/vnd.google-apps.spreadsheet'"
        response = service.files().list(q=query, fields='files(id, name)').execute()
        files = response.get('files', [])

        if files:

            update_file = service.files().update(
                fileId=files[0]['id'],
                media_body=media,
                fields='id'
            ).execute()
            print(f"Updated {file_name} with file ID: {update_file['id']}")
        else:

            file = service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print(
                f"Uploaded {file_name} and converted to Sheets with file ID: {file['id']}")
            
    def get_filled_range(service, spreadsheet_id, sheet_id_0):
        """Get the actual filled range in the sheet using the sheet name."""
 
        sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', [])
        sheet_name = None
        for sheet in sheets:
            if sheet['properties']['sheetId'] == sheet_id_0:
                sheet_name = sheet['properties']['title']
                break
        if not sheet_name:
            raise Exception("Sheet not found.")

    
        range_name = f"{sheet_name}!A1:Z1000"  #
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        if not values:
            return 0, 0  


        filled_rows = len(values)
        filled_columns = max((len(row) for row in values), default=0)  
        return filled_rows, filled_columns

    def format_google_sheet(service, spreadsheet_id):
        """Format the Google Sheet to adjust font size, apply bold, add borders, resize the first column,
        apply alternate row coloring, and format specific cells with value 'OFF'."""
        # Fetch metadata to determine the filled range and other properties
        sheet_metadata = service.spreadsheets().get(
            spreadsheetId=spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', [])
        if not sheets:
            raise Exception("No sheets found in the spreadsheet.")
        sheet = sheets[0]  # Assuming you want to format the first sheet
        sheet_id_0 = sheet['properties']['sheetId']
        # title = sheet['properties']['title']
        # grid_properties = sheet['properties']['gridProperties']
        # row_count = grid_properties['rowCount']
        # print(row_count)
        # column_count = grid_properties['columnCount']
        # print(column_count)
        row_count, column_count = Upload.get_filled_range(service, spreadsheet_id, sheet_id_0)


        # Prepare batch update body with multiple requests
        requests = [
            # Set borders and text formatting for all filled cells
            {
                'repeatCell': {
                    'range': {
                        'sheetId': sheet_id_0,
                        'startRowIndex': 0,
                        'endRowIndex': row_count,
                        'startColumnIndex': 0,
                        'endColumnIndex': column_count,
                    },
                    'cell': {
                        'userEnteredFormat': {
                            'textFormat': {'fontSize': 12, 'bold': True},
                            'horizontalAlignment': 'CENTER',
                            'borders': {
                                'top': {'style': 'SOLID', 'width': 1},
                                'bottom': {'style': 'SOLID', 'width': 1},
                                'left': {'style': 'SOLID', 'width': 1},
                                'right': {'style': 'SOLID', 'width': 1}
                            }
                        }
                    },
                    'fields': 'userEnteredFormat(textFormat, borders)'
                }
            },
            # Auto-resize the first column
            {
                'autoResizeDimensions': {
                    'dimensions': {
                        'sheetId': sheet_id_0,
                        'dimension': 'COLUMNS',
                        'startIndex': 0,
                        'endIndex': 2
                    }
                }
            },
            # Alternating row colors
            {
                'addConditionalFormatRule': {
                    'rule': {
                        'ranges': [{
                            'sheetId': sheet_id_0,
                            'startRowIndex': 1,  
                            'endRowIndex': row_count, 
                            'startColumnIndex': 0,
                            'endColumnIndex': column_count  
                        }],
                        'booleanRule': {
                            'condition': {
                                'type': 'CUSTOM_FORMULA',
                                'values': [{'userEnteredValue': '=ISEVEN(ROW())'}]
                            },
                            'format': {
                                'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}
                            }
                        }
                    },
                    'index': 1  
                }
            },
            # Format cells with "OFF" to orange background
            {
                'addConditionalFormatRule': {
                    'rule': {
                        'ranges': [{
                            'sheetId': sheet_id_0,
                            'startRowIndex': 0,
                            'endRowIndex': row_count,
                            'startColumnIndex': 0,
                            'endColumnIndex': column_count,
                        }],
                        'booleanRule': {
                            'condition': {
                                'type': 'TEXT_EQ',
                                'values': [{'userEnteredValue': 'OFF'}]
                            },
                            'format': {
                                'backgroundColor': {'red': 1.0, 'green': 0.6, 'blue': 0.0}
                            }
                        }
                    },
                    'index': 0
                }
            }
        ]
        body = {'requests': requests}
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body).execute()
        print("Formatted Google Sheet with custom styles.")

    def Execute(creds, op_path):
        service = build('drive', 'v3', credentials=creds)
        format_service = build('sheets', 'v4', credentials=creds)

        parent_folder_name = "2024"
        sub_folder_name = "May"
        weekly_responses_folder_name = "DayWiseSheets"
        weekly_headcounts_folder_name = "WeeklyHeadCounts"
        local_day_wise_sheets_path = f'{op_path}/Daywise_Sheets'
        local_head_counts_path = op_path

        parent_folder_id = Upload.find_or_create_folder(
            service, 'root', parent_folder_name)
        month_folder_id = Upload.find_or_create_folder(
            service, parent_folder_id, sub_folder_name)
        weekly_responses_folder_id = Upload.find_or_create_folder(
            service, month_folder_id, weekly_responses_folder_name)
        weekly_headCounts_folder_id = Upload.find_or_create_folder(
            service, month_folder_id, weekly_headcounts_folder_name)
        

        # Upload or replace all CSV files in the folder
        for file_name in os.listdir(local_day_wise_sheets_path):
            if file_name.endswith('.csv'):
                Upload.upload_or_convert_to_sheets(
                    service, weekly_responses_folder_id, local_day_wise_sheets_path, file_name, format_service)
                
        for hc_file_name in os.listdir(local_head_counts_path):
            if hc_file_name.endswith('.csv'):
                Upload.upload_to_headcounts(
                    service, weekly_headCounts_folder_id, local_head_counts_path, hc_file_name, format_service)
        


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


class initiate():

    def initiation():
        initiation = f"""{colors.fg.yellow}
███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████     ███    ███ ███████ ███████ ███████ \n██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██          ████  ████ ██      ██      ██      \n███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████     ██ ████ ██ █████   ███████ ███████ \n     ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██     ██  ██  ██ ██           ██      ██ \n███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████     ██      ██ ███████ ███████ ███████ \n\n                                                                                      
                                  {colors.bold}STATS GENERATION SCRIPT BY BINEET{colors.reset}                      {colors.reset}\n\n\nOperations\n----------
                                                                            
    """
        print(initiation)


help = f"""
This program was created by {colors.bold}Bineet Kumar Mohanta{colors.reset}
{colors.fg.blue}profile : https://bineetx.github.io
{colors.reset}
\nUses:
{colors.bg.green}python3 name_of_script.py mess_responses.csv{colors.reset}

"""


if __name__ == "__main__":
    start = time.time()
    initiate.initiation()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",
                        help="Path to Response CSV", default=None)
    parser.add_argument("-l", "--sheetlink",
                        help="Link of the response", default=None)
    parser.add_argument(
        "-u", "--upload", help="Link of the response", default=None)
    args = parser.parse_args()

    csv_path = args.filename
    link_path = args.sheetlink
    upload = args.upload

    creds = Response.load_credentials()

    if csv_path:
        data = pd.read_csv(csv_path)
    elif link_path:
        sheet_id = link_path.split("/d/")[1].split("/")[0]
        data = Response.fetch_sheet_data(creds, sheet_id)

    response = Response()
    op_path = Response.create_paths()
    # print(op_path)
    response.GenerateSheets(data)
    Response.GenerateStats(op_path=op_path, reference_dict=VEG_NONVEG_DICT)
    if upload == "yes":
        Upload.Execute(creds=creds, op_path=op_path)

    # final_stat = response.Total_finance(op_path)
    # response.GenerateTotalStat(final_stat)
    time_taken = round(time.time() - start, 2)
    # print(final_stat)
    print(f"{colors.fg.green}\n\n                        ---- GENERATED THE SHEETS IN {time_taken} SECONDS ----{colors.reset}\n\n                                        For help contact me at \n         {colors.fg.blue}     Ph: +918908241864 {colors.reset}| {colors.fg.green}WhatsApp: https://wa.me/918808241864 {colors.reset}| {colors.fg.cyan}Web: https://bineet.dev/")
