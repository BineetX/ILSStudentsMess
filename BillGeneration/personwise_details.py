import pandas as pd
file = pd.read_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/AUgust/August_sheet_final_test2.csv")
file = file.set_index("Registered Email Address")
print(file.loc["poojaarchana.54@gmail.com"])