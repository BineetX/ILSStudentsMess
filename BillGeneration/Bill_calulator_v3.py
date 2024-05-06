#with_veg_options
import pandas as pd

file = pd.read_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Calc/AprilFinalMerged_corrected.csv")
schema = pd.read_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Calc/April_final_menu_schema.csv").set_index("Day")
active_members = pd.read_csv("/home/bineet/StudentsMess/FinalScripts/Active_Members_new.csv")#.index("Registered Email Address")
active_members = active_members.set_index("Registered Email Address")
# print(schema)

final_bill = {}

menu = {
    "breakfast":35,
    
    "regular_lunch":60,
    "regular_dinner":60,
    
    "chicken":85,
    "chicken_special":90,
    "egg":80,
    "fish":75,
    "prawn":120,
    "mutton": 190,
    
    "veg_special":90,
    "paneer":75,
    "mushroom":85,
    "veg_super_special":120,
    
    "sunday_lunch":105,
    "off":0
}


# breakfast_base = 35
# base = 60
# egg = 70
# fish = 75
# chicken = 85
# special = 105
# feast = 150
# off = 0

# def calculate_day_wise_price(i,preference):

    

def calcluate_day_wise_price(date,userResponse,preference,menu=menu,schema= schema):
    #Preference = Veg/nonveg
    #userResponse = Response string
    #menu = price dictionary
    # print("in the calclualtiom")
    ItemsList = []
    lunch_price=0
    breafast_price = 0
    dinner_price = 0
    if "Lunch" in userResponse:
        
        if preference == 'veg':
            lunch_price = menu[schema.loc[date]["lunch_veg"]]
            ItemsList.append(schema.loc[date]["Veg_item_name"])
        elif preference == 'nonveg':
            lunch_price = menu[schema.loc[date]["lunch_nonveg"]]
            ItemsList.append(schema.loc[date]["Nonveg_item_name"])
    if "Breakfast" in userResponse:
        breafast_price = menu["breakfast"]
        ItemsList.append("Breakfast")
    if "Dinner" in userResponse:
        dinner_price = menu[schema.loc[date]["dinner"]]
        if dinner_price == 0:
            pass
        else:
            ItemsList.append("Dinner")
        
        
        
    day_price = lunch_price + breafast_price + dinner_price
    # print(day_price)
    # print("Finished Calculation")
    return day_price, ItemsList
    
            





menu_response_keyed = file.set_index("Registered Email Address")
menu_response_keyed = menu_response_keyed[~menu_response_keyed.index.duplicated(keep='last')]
# print(menu_response_keyed)
mother_bill = {}
for member_email in menu_response_keyed.index:
    member_bill =0
    Total_eaten = []
    for i in menu_response_keyed.columns:
        if i.startswith("["):
            print(i)
        # 
            user_response = str(menu_response_keyed.loc[member_email][i])
            if "Non Veg" in user_response:
                preference = "nonveg"
            else:
                preference = "veg"
            print("Still working")
            
            
            day_price, ItemsEaten = calcluate_day_wise_price(date=i,userResponse=user_response,preference=preference)
            print("Bill calculation working")
            member_bill = member_bill + day_price
            Total_eaten.extend(ItemsEaten)
            # DO it tomorrow
    final_user_bill = {"Name":active_members.loc[member_email]["Name"].title(),"bill":member_bill}
    items_eaten_dict  = {}
    for item in Total_eaten:
        items_eaten_dict[item] = items_eaten_dict.get(item,0)+1
        
    final_user_bill.update(items_eaten_dict)

    
    mother_bill.update({member_email:final_user_bill})
    
# print(mother_bill)
Bill = pd.DataFrame.from_dict(mother_bill).T
Bill = Bill.fillna(0)
print(Bill.to_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Calc/AprilFinalBillCalculation2.csv"))
# print(active_members)       
            
        # breakfast,lunch,dinner,lunch_type = calcluate_day_wise_price(i)
#         # print(breakfast,lunch,dinner)
        
#             if member_email not in final_bill.keys():
#                 final_bill[member_email] = {"Name":menu_response_keyed.loc[member_email]["Name"],"num_breakfast":0,"bill":0,"num_lunch":0,"num_dinner":0,"base_lunch_meals":0,"chicken_lunch_meals":0,"egg_lunch_meals":0,"fish_lunch_meals":0,"sunday_meal":0}
#             day_bill = 0
#             responce = str(menu_response_keyed.loc[member_email][i])
#             # print(responce)
#             if "Breakfast" in responce:
#                 day_bill = day_bill + breakfast
#                 final_bill[member_email]["num_breakfast"] = final_bill[member_email]["num_breakfast"] + 1
#             if "Lunch" in responce:
#                 day_bill = day_bill + lunch
#                 final_bill[member_email]["num_lunch"] = final_bill[member_email]["num_lunch"] + 1
#                 final_bill[member_email][lunch_type] = final_bill[member_email][lunch_type] + 1
#             if "Dinner" in responce:
#                 if "Sunday" not in i:
#                     day_bill = day_bill + dinner
#                     final_bill[member_email]["num_dinner"] = final_bill[member_email]["num_dinner"] + 1
#             # if(member_email == "bineetkumarmohanta@gmail.com"):
#             #     print(responce)
#             #     print(day_bill)
#             #     print(schema.loc[i])
            
#             final_bill[member_email]["bill"] = final_bill[member_email]["bill"] + day_bill
                
# final_df = pd.DataFrame.from_dict(final_bill).T
# print(final_df.to_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Sept/Sept17daysBill.csv"))
            

