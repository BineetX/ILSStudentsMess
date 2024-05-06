#!/usr/bin/python3
# -*- coding: utf-8 -*-

#This program is created by Bineet Kumar Mohanta
#To generate readable and simplified stats for the students mess

#Insatlling and Importing Dependencies if needed
import pip
import argparse
from datetime import datetime
import time
import os
import getpass
try:
    import pandas as pd
except:
    pip.main(['install', "pandas"])
    

VEG_NONVEG_DICT = {
    "Monday":"None",
    "Tuesday":"Lunch",
    "Wednesday":"Lunch",
    "Thursday":"None",
    "Friday":"Lunch",
    "Saturday":"None",
    "Sunday":"Lunch"
}

class Response():
    def __init__(self,data):
        self.data = data
        
    def get_time():
        # time = datetime.now().strftime("%d-%B-%Y-%H-%M-%p")
        time = datetime.now().strftime("%d-%B-%H-%p")
        return time
    def create_paths(): #! Can Be Imporved
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
    def AnalyzeDay(self,habit,not_sunday=True):
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
        if "Non Veg" in pref:
            tmp.update({"Preference": "Non Veg"})
        else:
            tmp.update({"Preference": "Veg"})
            
        return tmp
    
    def GenerateSheets(self,op_path):
        menu_response = pd.read_csv(self.data)
        menu_response_keyed = menu_response.set_index("Registered Email Address")
        menu_response_keyed = menu_response_keyed[~menu_response_keyed.index.duplicated(keep='last')]
        for day in menu_response_keyed.columns:
            if day.startswith(" ["):
                sheet_name = day.replace(" [",'').replace("]","").replace("/","-")
                final_dict = {}
                for user in menu_response_keyed.index:
                    user_dict = {}
                    
                    if "Sunday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit,not_sunday=False))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Monday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Tuesday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Wednesday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Thursday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Friday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    if "Saturday" in day:
                        habit = str(menu_response_keyed.loc[user][day])
                        user_dict.update(self.AnalyzeDay(habit))
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                
                final_df = pd.DataFrame.from_dict(final_dict).T
                final_df.index.name = "Name"
                final_df = final_df.sort_values("Name")
                final_df.to_csv(f"{op_path}/Daywise_Sheets/{sheet_name}.csv")
                print(f"generate the Day Wise Sheet for {sheet_name}")
        print("\ngenerated the Bill for the term" )
    
    def GenerateStats(op_path,reference_dict):
        files = os.listdir(f"{op_path}/Daywise_Sheets")
        files.sort()
        with open(f"{op_path}/HeadCounts.csv","w") as op:
            op.write("Date,Day,Breakfast,Lunch,Dinner,Veg-in-breakfast,Veg-in-Lunch,Veg-in-Dinner,NonVeg-in-breakfast,NonVeg-in-Lunch,NonVeg-in-Dinner")
            for i in files:
                file= pd.read_csv(f"{op_path}/Daywise_Sheets/{i}")
                name = i.replace(".csv","")
                total_strength = len(file)
                total_breakfast_off = len(file[file["Breakfast"]=="OFF"])
                total_lunch_off = len(file[file["Lunch"]=="OFF"])
                total_dinner_off = len(file[file["Dinner"]=="OFF"])
                total_breakfast_on = total_strength - total_breakfast_off
                total_lunch_on = total_strength - total_lunch_off
                total_dinner_on = total_strength - total_dinner_off
                
                day = i.split(" - ")[1].split(".")[0]
                # print(day)
                if reference_dict[day] == "Lunch":
                    non_veg_in_lunch = len(file[(file["Preference"]== "Non Veg") & (file["Lunch"]!="OFF")] )
                    veg_in_lunch = total_lunch_on - non_veg_in_lunch
                    non_veg_in_dinner = 0
                    veg_in_dinner = total_dinner_on
                    
                    non_veg_in_breakfast = 0
                    veg_in_breakfast = total_breakfast_on
                elif reference_dict[day] == "Dinner":
                    non_veg_in_lunch = 0
                    veg_in_lunch = total_lunch_on
                    
                    non_veg_in_dinner = len(file[(file["Preference"]== "Non Veg") & (file["Dinner"]!="OFF")] )
                    veg_in_dinner = total_dinner_on - non_veg_in_dinner
                    
                    non_veg_in_breakfast = 0
                    veg_in_breakfast = total_breakfast_on
                    
                elif reference_dict[day] == "Breakfast":
                    non_veg_in_lunch = 0
                    veg_in_lunch = total_lunch_on
                    
                    non_veg_in_dinner = 0
                    veg_in_dinner = total_dinner_on
                    
                    non_veg_in_breakfast = len(file[(file["Preference"]== "Non Veg") & (file["Breakfast"]!="OFF")] )
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
        initiation =f"""{colors.fg.yellow}
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




if __name__== "__main__":
    start = time.time()
    initiate.initiation()
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='csv_path', help=help)
    args = parser.parse_args()
    csv_path = args.csv_path
    
    response = Response(csv_path)
    op_path = Response.create_paths()
    # print(op_path)
    response.GenerateSheets(op_path)
    Response.GenerateStats(op_path=op_path,reference_dict=VEG_NONVEG_DICT)
    # final_stat = response.Total_finance(op_path)
    # response.GenerateTotalStat(final_stat)
    time_taken = round(time.time() - start,2)
    # print(final_stat)
    print(f"{colors.fg.green}\n\n                        ---- GENERATED THE SHEETS IN {time_taken} SECONDS ----{colors.reset}\n\n                                        For help contact me at \n         {colors.fg.blue}     Ph: +918908241864 {colors.reset}| {colors.fg.green}WhatsApp: https://wa.me/918808241864 {colors.reset}| {colors.fg.cyan}Web: https://bineet.dev/")


                            
                    
