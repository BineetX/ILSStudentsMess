#!/usr/bin/python3
# -*- coding: utf-8 -*-

#This program is created by Bineet Kumar Mohanta
#To generate readable and simplified stats for the students mess

import pip
import argparse
from datetime import datetime
import time
import os
try:
    import pandas as pd
except:
    pip.main(['install', "pandas"])





class Response():
    menu_schema = {
        "Monday":{"bf":"breakfast_base","l":"base","d":"base"},
        "Tuesday":{"bf":"breakfast_base","l":"egg","d":"base"},
        "Wednesday":{"bf":"breakfast_base","l":"fish","d":"base"},
        "Thursday":{"bf":"breakfast_base","l":"base","d":"base"},
        "Friday":{"bf":"breakfast_base","l":"chicken","d":"base"},
        "Saturday":{"bf":"breakfast_base","l":"base","d":"base"},
        "Sunday":{"bf":"breakfast_base","l":"special","d":"base"},
    }
    # breakfast_base = 30
    # base = 55
    # egg = 65
    # fish = 70
    # chicken = 80
    # special = 100
    
    
    # Test
    breakfast_base = 35
    base = 60
    egg = 70
    fish = 75
    chicken = 85
    special = 105
    
    menu_price = {
        "breakfast_base":breakfast_base,
        "base": base,
        "egg": egg,
        "fish": fish,
        "chicken": chicken,
        "special":special
    }
    
    def __init__(self,data,menu_schema=menu_schema,menu_price = menu_price):
        self.menu_schema = menu_schema
        self.data = data
        self.menu_price = menu_price
        # print("In response")
        
    def get_time():
        # time = datetime.now().strftime("%d-%B-%Y-%H-%M-%p")
        time = datetime.now().strftime("%d-%B-%H-%p")
        return time
    
    
    def create_paths():
        current_path = os.getcwd()
        path = Response.get_time()
        op_path = current_path + "/Generated_on" + path

        try:
            os.mkdir(f"{op_path}")
            os.mkdir(f"{op_path}/Daywise_Sheets")
        except:
            print("Path already existed")
            
        # print(op_path)
        print(f"Created the directories at :{op_path}")
        return op_path
    
    def decide_bills(menu_schema,menu_price,brk,lch,dnr,pre,day):
        num_brk = 0
        num_lnc = 0
        num_dnr = 0
        num_egg = 0
        num_fish = 0
        num_chicken = 0
        num_special = 0
        num_egg_eq = 0
        num_fish_eq = 0
        num_chicken_eq = 0
        
        menu = menu_schema[day]
        brk_price = menu_price[menu['bf']]
        lnc_price = menu_price[menu['l']]
        dnr_price = menu_price[menu['d']]
        
        if brk == "✓":
            num_brk = num_brk + 1
        if lch == "✓":
            num_lnc = num_lnc + 1
            if menu["l"] == "egg":
                if pre == "Non Veg":
                    num_egg = num_egg + 1
                else:
                    num_egg_eq = num_egg_eq + 1
            elif menu["l"] == "fish":
                if pre == "Non Veg":
                    num_fish = num_fish + 1
                else:
                    num_fish_eq = num_fish_eq + 1
            elif menu["l"] == "chicken":
                if pre == "Non Veg":
                    num_chicken = num_chicken + 1
                else:
                    num_chicken_eq= num_chicken_eq + 1
            elif menu["l"] == "special":
                num_special = num_special + 1
                
        if dnr == "✓":
            num_dnr = num_dnr + 1
            
        day_bill = (brk_price * num_brk) + (lnc_price * num_lnc) + (dnr_price * num_dnr)
        
        stat_day = {
            "num_brk":num_brk,
            "num_lnc":num_lnc,
            "num_dnr":num_dnr,
            "num_egg":num_egg,
            "num_fish":num_fish,
            "num_chicken":num_chicken,
            "num_special":num_special,
            "num_egg_eq":num_egg_eq,
            "num_fish_eq":num_fish_eq,
            "num_chicken_eq":num_chicken_eq,
            "day_bill":day_bill
            }
        return stat_day

    def GenerateTotalStat(self,total_stats):
        details = f"""
TOTAL STATS FOR REGISTERED MEMBERS
----------------------------------

Breakfasts Served       : {total_stats["breakfast_number"]}
Lunches Served          : {total_stats["lunch_number"]}
Dinners Served          : {total_stats["dinner_number"]}
        
Total Generated Bill    : {total_stats["Total_bill"]}
        """
        
        print(details)
        
        
    def GenerateSheets(self,op_path):
        menu_response = pd.read_csv(self.data)
        print("Reading the response sheet")
        # menu_response = menu_response.drop([" [01/05/2023 - Monday]"," [02/05/2023 - Tuesday]"],axis=1)
        menu_response_keyed = menu_response.set_index("Registered Email Address")
        menu_response_keyed = menu_response_keyed[~menu_response_keyed.index.duplicated(keep='last')]
        bill= {}

        # days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        for day in menu_response_keyed.columns:
            if day.startswith(" ["):
                sheet_name = day.replace(" [",'').replace("]","").replace("/","-")
                final_dict = {}
                
                for user in menu_response_keyed.index:
                    user_dict = {}
                    if user not in bill.keys():
                        name  = str(menu_response_keyed.loc[user]["Name"]).lower().title()
                        bill[user] = {"Name":name,"breakfast_number":0,"lunch_number":0,"dinner_number":0,"number_of_egg_meals":0,"number_of_fish_meals":0,"number_of_chicken_meals":0,"number_of_VEG_eqv_of_egg_meals":0,"number_of_VEG_eqv_of_fish_meals":0,"number_of_VEG_eqv_of_chicken_meals":0,"sumber_of_sunday_special":0,"Total_bill":0}
                    else:
                        pass
                    
                    if "Sunday" in day:
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "OFF"}
                        else:
                            din = {"Dinner": "OFF"}

                        pref = habit.split(",")[-1]
                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        
                        
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Sunday")
                        # print(day_stat)
                        # print(brk["Breakfast"])
                        
                            
                        
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                            
                    if "Monday" in day:
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "✓"}
                        else:
                            din = {"Dinner": "OFF"}
                            
                        pref = habit.split(",")[-1]
                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Monday")


                    
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                            
                    if "Tuesday" in day:
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "✓"}
                        else:
                            din = {"Dinner": "OFF"}

                        pref = habit.split(",")[-1]
                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Tuesday")
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                            
                            
                    if "Wednesday" in day:
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "✓"}
                        else:
                            din = {"Dinner": "OFF"}

                        pref = habit.split(",")[-1]
                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Wednesday")

                        
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                    
                    if "Thursday" in day:
                        
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "✓"}
                        else:
                            din = {"Dinner": "OFF"}
                            
                        pref = habit.split(",")[-1]
                        
                        # pre = {"Preference": "Base"}

                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Thursday")

                    
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)
                            
                    if "Friday" in day:
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "✓"}
                        else:
                            din = {"Dinner": "OFF"}

                        pref = habit.split(",")[-1]
                        # print(pref)
                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Friday")

                        
                        # try:
                        #     final_dict.update({final_ref_dict.loc[user]["Name"]: user_dict})
                        # except:
                        #     print(f"user {user} is not found in the registerd dict")
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(menu_response_keyed.loc[user])
                            
                    if "Saturday" in day:
                        habit = str(
                            menu_response_keyed.loc[user][day])
                        if "Breakfast" in habit:
                            brk = {"Breakfast": "✓"}
                        else:
                            brk = {"Breakfast": "OFF"}
                        if "Lunch" in habit:
                            lun = {"Lunch": "✓"}
                        else:
                            lun = {"Lunch": "OFF"}
                        if "Dinner" in habit:
                            din = {"Dinner": "✓"}
                        else:
                            din = {"Dinner": "OFF"}

                        pref = habit.split(",")[-1]
                        # # print(pref)
                        if "Non Veg" in pref:
                            pre = {"Preference": "Non Veg"}
                        else:
                            pre = {"Preference": "Veg"}
                        # pre = {"Preference": "Base"}
                            
                        user_dict.update(brk)
                        user_dict.update(lun)
                        user_dict.update(din)
                        user_dict.update(pre)
                        day_stat = Response.decide_bills(menu_price=self.menu_price,menu_schema=self.menu_schema ,brk=brk["Breakfast"],lch=lun["Lunch"],dnr=din["Dinner"],pre=pre["Preference"],day="Saturday")

                        
                        # try:
                        #     final_dict.update({final_ref_dict.loc[user]["Name"]: user_dict})
                        # except:
                        #     print(f"user {user} is not found in the registerd dict")
                        try:
                            name = menu_response_keyed.loc[user]["Name"].lower().title()
                            final_dict.update({name: user_dict})
                        except:
                            print(name)

                    bill[user]["breakfast_number"] = bill[user]["breakfast_number"] + day_stat["num_brk"]
                    bill[user]["lunch_number"] = bill[user]["lunch_number"]+  day_stat["num_lnc"]
                    bill[user]["dinner_number"] = bill[user]["dinner_number"]+  day_stat["num_dnr"]
                    bill[user]["number_of_egg_meals"] = bill[user]["number_of_egg_meals"] +  day_stat["num_egg"]
                    bill[user]["number_of_fish_meals"] = bill[user]["number_of_fish_meals"] + day_stat["num_fish"]
                    bill[user]["number_of_chicken_meals"] = bill[user]["number_of_chicken_meals"] +  day_stat["num_chicken"]
                    bill[user]["number_of_VEG_eqv_of_egg_meals"] = bill[user]["number_of_VEG_eqv_of_egg_meals"] + day_stat["num_egg_eq"]
                    bill[user]["number_of_VEG_eqv_of_fish_meals"] = bill[user]["number_of_VEG_eqv_of_fish_meals"] + day_stat["num_fish_eq"]
                    bill[user]["number_of_VEG_eqv_of_chicken_meals"] = bill[user]["number_of_VEG_eqv_of_chicken_meals"] + day_stat["num_chicken_eq"]
                    bill[user]["sumber_of_sunday_special"] = bill[user]["sumber_of_sunday_special"] + day_stat["num_special"]
                    bill[user]["Total_bill"] = bill[user]["Total_bill"] + day_stat["day_bill"]
                            
                    
                               
                            
                                    
                    
                # print(sheet_name)
                # print(bill)
                bill_df = pd.DataFrame.from_dict(bill).T
                # print(bill_df)
                final_df = pd.DataFrame.from_dict(final_dict).T
                final_df.index.name = "Name"
                final_df = final_df.sort_values("Name")
                bill_df = bill_df.sort_values("Name")
                bill_df.to_csv(f"{op_path}/Bill.csv")
                final_df.to_csv(f"{op_path}/Daywise_Sheets/{sheet_name}.csv")
                print(f"generate the Day Wise Sheet for {sheet_name}")
        print("\ngenerated the Bill for the term" )
    def Total_finance(self,op_path):
        bill = pd.read_csv(f"{op_path}/Bill.csv")
        bil_sum = bill.sum()
        return bil_sum
                    
    def GenerateStats(op_path,reference_dict):
        files = os.listdir(f"{op_path}/Daywise_Sheets")
        files.sort()
        with open(f"{op_path}/Day_wise_meal_counts.csv","w") as op:
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
                # total_veg = len(file[(file["Preference"]== "Veg") | (file["Preference"]=="Base")] )
                # veg_in_lunch = 0
                # veg_in_dinner = 0
                # non_veg_in_lunch  = 0
                # non_veg_in_dinner = 0
                
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


                # op = f"""


                # Day : {name}
                # ------------------------------------------------

                # Total Number of Breakfast : {total_breakfast_on}
                # Total Number of Lunch     : {total_lunch_on}
                # Total Number of Dinner    : {total_dinner_on}
                # Total Number of Veg       : {total_veg}
                # TotalNon Veg             : {total_non_veg}
                # """

                # print(op)
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


# Fill with Nonveg ref: None/Both/Dinner/Lunch/Breakfast
reference_veg_nonveg_dict = {
    "Monday":"None",
    "Tuesday":"Lunch",
    "Wednesday":"Lunch",
    "Thursday":"None",
    "Friday":"Lunch",
    "Saturday":"None",
    "Sunday":"Lunch"
}

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
    Response.GenerateStats(op_path=op_path,reference_dict=reference_veg_nonveg_dict)
    final_stat = response.Total_finance(op_path)
    response.GenerateTotalStat(final_stat)
    time_taken = round(time.time() - start,2)
    # print(final_stat)
    print(f"{colors.fg.green}\n\n                        ---- GENERATED THE STATS SUCCESSFULLY IN {time_taken} SECONDS ----{colors.reset}\n\n                                        For help contact me at \n         {colors.fg.blue}     Ph: +918908241864 {colors.reset}| {colors.fg.green}WhatsApp: https://wa.me/918808241864 {colors.reset}| {colors.fg.cyan}Web: https://bineetx.github.io/")

    