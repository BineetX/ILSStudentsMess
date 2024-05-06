import pandas as pd

final_sheet = pd.read_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Calc/AprilFinalMerged_corrected.csv")
initial = final_sheet.columns
final = sorted([elem for elem in initial if elem not in ['Registered Email Address', 'Name']])
print(final)


regular_days = ["Monday","Thursday"]

with open("/home/bineet/StudentsMess/Codes/Bill_calculation/Calc/April_final_menu_schema.csv","w") as f:
    f.write("Day,breakfast,lunch_veg,lunch_nonveg,dinner,Veg_item_name,Nonveg_item_name\n")
    for i in final:
        
        if "Monday" in i:
            f.write(f"{i},breakfast,regular_lunch,regular_lunch,regular_dinner,Regular Meal,Regular Meal\n")
        if "Tuesday" in i:
            f.write(f"{i},breakfast,paneer,egg,regular_dinner,Veg Meal,Egg Meal\n")
        if "Wednesday" in i:
            f.write(f"{i},breakfast,paneer,fish,regular_dinner,Veg Meal,Fish Meal\n")
        if "Thursday" in i:
            f.write(f"{i},breakfast,regular_lunch,regular_lunch,regular_dinner,Regular Meal,Regular Meal\n")
        if "Friday" in i:
            f.write(f"{i},breakfast,mushroom,chicken,regular_dinner,Veg Meal,Chicken Meal\n")
        if "Saturday" in i:
            f.write(f"{i},breakfast,regular_lunch,regular_lunch,regular_dinner,Regular Meal,Regular Meal\n")
        if "Sunday" in i:
            f.write(f"{i},breakfast,sunday_lunch,sunday_lunch,off,Veg Biriyani,Egg Chicken Biriyani\n")
        # else:
        #     f.write(f"{i},breakfast,regular_lunch,regular_lunch,regular_dinner,Regular Meal,Regular Meal\n")
            
            