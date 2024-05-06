#### BILL FILES MERGERS BY BINEET V2


import pandas as pd
import os

def clean_data():
    path = os.getcwd()
    files = os.listdir(f"{path}/Final_sheets")
    output = []
    for file in files:
        file_path = os.path.join(path,f"Final_sheets/{file}")
        clean = pd.read_csv(file_path).set_index("Registered Email Address")

        clean = clean[~clean.index.duplicated(keep='last')]
        clean_days = clean[only_keep_days(clean)]
        
        output.append(clean_days)
    return output

def only_keep_days(df):
    days = []
    for column in df.columns:
        if column.startswith(" ["):
            days.append(column)
        
    return(days)
        

initial = pd.read_csv("/home/bineet/StudentsMess/FinalScripts/Active_Members_new.csv").set_index("Registered Email Address")
closed_memers = list(set(pd.read_csv("/home/bineet/StudentsMess/FinalScripts/Closed_Members.csv").set_index("Registered Email Address").index))
initial_mebres = list(initial.index)

print(closed_memers)
dup = {x for x in initial_mebres if initial_mebres.count(x) > 1}
print(dup)

op = clean_data()
# print(len(op))
feed = [initial]

feed.extend(op)
print(len(feed))


final  = pd.concat(feed,axis=1)
dates_to_be_ignored = []
closed_memers = list(set(closed_memers) - {'j12mishra@gmail.com', 'ajmuktaj917@gmail.com', 'c.sanchari1712@gmail.com', 'debojyoti.d@ils.res.in', 'jsahoo390.liki1997@gmail.com', 'aradhanamishrasep17@gmail.com', 'abesanamangng333@gmail.com', 'ashirbadsaikatde@gmail.com', 'madhuri@ils.res.in', 'sonalighosal@ils.res.in', 'jyotisao21@gmail.com', 'priyapranati2001@gmail.com', 'bidisha@ils.res.in', 'vishakha22@iiserbpr.ac.in', 'sahidurrahaman815@gmail.com', 'bimal@ils.res.in'})

final = final.drop(dates_to_be_ignored,axis=1)
final = final.drop(closed_memers)
print(final)
# print(final.to_csv("/home/bineet/StudentsMess/Outputs/Total_attendance.csv"))
# print(sorted(list(final.columns)))
# without_name = final[final["Name"].isna()]
# print(without_name)
print(final.to_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Calc/AprilFinalMerged.csv"))
# print(final.to_csv("June_sheet.csv"))



