#Whatsapp Update sender By Bineet for Students Mess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import os
from selenium.webdriver.common.keys import Keys


#data
data = pd.read_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Bill Sender/AprilFinalBillCalculation - AprilFinalBillCalculation.csv").set_index("Unnamed: 0")
phone_numbers = pd.read_csv("/home/bineet/StudentsMess/Codes/Bill_calculation/Bill Sender/PhoneDirectory.csv",dtype={"Phone Number":str}).set_index("Registered Email Adress")

def join_and(items):
    return '%0a'.join(items[:-1]) + ' , and%0a'+items[-1]


breakfast = 35
regular= 60
chicken = 85
paneer = 75
mushroom = 85
egg = 80
fish = 75
sunday_meal =105
prawn =120
mutton = 190
veg_super_special = 120
veg_special =90
chicken_special = 90


menu_price = {
    

"Regular Meal":regular,
"Breakfast": breakfast,
"Dinner": regular,


"Paneer Meal": paneer,
"Mushroom Meal":mushroom,
"Egg Meal":egg,
"Chicken Meal":chicken,
"Fish Meal":fish,

"Paneer Butter Masala Meal": paneer,
"Paneer Masala Meal": paneer,
"Matar Paneer Meal":paneer,
"Paneer Curry Meal": paneer,
"Palak Paneer Meal": paneer,
"Paneer Chole Meal": paneer,
"Paneer Tikka Masala Meal":veg_super_special,
"Paneer Kadhai Meal":paneer,
"Paneer Lababdar Meal":paneer,
"Kadhai Paneer Meal":paneer,
"Chenna Kofta Meal": mushroom,
"Ram Navami Special Meal":veg_special,


"Mix Veg Korma Meal": paneer,
"Mix Veg Kofta Meal": paneer,
"Mix Veg Meal": paneer,
"Veg Kofta Meal": paneer,
"Porwal Korma Meal":paneer,
"Palak Kofta Meal":veg_special,
"Parwal Korma Meal":paneer,
"Cauliflower Curry Meal":paneer,
"Dhoka Curry Meal":paneer,

"Mushroom Masala Meal": mushroom,
"Chilly Mushroom Meal": mushroom,
"Mushroom Curry Meal":mushroom,
"Mushroom Besara Meal":mushroom,
"Kadhai Mushroom Meal":mushroom,
"Mushroom Kadhai Meal":mushroom,

"Navaratna Korma Meal": veg_special,
"Malai Kofta Meal": paneer,
"Pulao-Palak Paneer Meal":veg_special,

"Kathal Masala Meal":paneer,

"Chicken Kasa Meal": chicken,
"Chicken Masala Meal": chicken,
"Chicken Butter Masala Meal": chicken,
"Chicken Curry Meal": chicken,
"Chicken Afgani Meal":chicken,
"Lahori Chicken Meal":chicken,
"Kolhapuri Chicken Meal":chicken,
"Chicken Hyderabadi Meal":chicken,
"Chicken Punjabi Meal":chicken,

"Egg Curry Meal": egg,
"Egg Masala Meal": egg,
"Egg Korma Meal": egg,
"Egg Makhani Meal":egg,
"Egg Omelette Curry Meal":egg,

"Fish Curry Meal": fish,
"Fish Besara Meal": fish,
"Fish Pohala Meal": fish,
"Fish Do-Pyaza Meal": fish,
"Fish Kasa Meal": fish,
"Fish Masala Meal": fish,
"Fish Kalia Meal":fish,
"Pohala Meal":fish,
"Katla Kalia Meal":fish,
"Chilly Fish Meal":fish,


"Veg Biriyani": sunday_meal,
"Egg Chicken Biriyani": sunday_meal,
"Chilly Chicken Meal":sunday_meal,
"Pulao Chicken Kasa":sunday_meal,
"Pulao Kadhai Paneer":sunday_meal,

"Prawn Curry Meal":prawn,
"Mutton Kasa Meal":mutton,
"Baby Corn Curry Meal":mushroom,

}


def generate_message(test):
    printable = [""]
    print(test.index)
    for i in sorted(test.index):
        print(i)
        if i in ["Name","bill","Corrected_bill"]:
            pass
        else:
            if test[i] > 0:
                if test[i] == 1:
                    printable.append(f"- *{int(test[i])} {i}*  _[Rs.{menu_price[i]}]_",)
                else:
                    printable.append(f"- *{int(test[i])} {i}s*  _[Rs.{menu_price[i]}]_",)
            else:
                pass
        
    return join_and(printable)

# for i in data.index:
#     try:
#         print(phone_numbers.loc[i])
#     except:
#         print("-------------------------------------",i)



#
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


message = "Bineet is awesome"
print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)

# message = quote(message)
# infomation_dict = {"8908241864":{"name":"Bineet","num_l":90,"total_bill":6000},"9632491363":{"name":"Sudeshna","num_l":90,"total_bill":4000},"9439386943":{"name":"Madhu","num_l":80,"total_bill":4000}}

# numbers = ["8908241864","9439386943","8249418538","9632491363"]

# total_number=len(numbers)
delay = 30
print("Installing the latest driver")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Firefox(executable_path="/home/bineet/StudentsMess/Essentials/drivers/geckodriver")
driver = webdriver.Chrome("/home/bineet/StudentsMess/Codes/Bill_calculation/Bill Sender/ChromeDriver/chromedriver-linux64/chromedriver", options=options)
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "Log in to whatsapp and press enter" + style.RESET)

not_send = []


print(data.columns)
for i in data.index:
    
    try:
        print("Doing good")
        number = phone_numbers.loc[i]["Phone Number"]
        name = data.loc[i]["Name"]
        # total_number_of_breakfasts = data.loc[i]['num_breakfast']
        # total_number_of_lunch = data.loc[i]['num_lunch']
        # total_number_of_dinner = data.loc[i]['num_dinner']
        
        # total_base_meals = data.loc[i]['base_lunch_meals']
        # total_number_of_checken = data.loc[i]['chicken_lunch_meals']
        # total_number_of_fish = data.loc[i]['fish_lunch_meals']
        # total_number_of_egg = data.loc[i]['egg_lunch_meals']
        # total_sunday_meals = data.loc[i]['sunday_meal']
        
        final_bill = data.loc[i]['Corrected_bill']
        print("Yo")
        
        # feast = data.loc[i]['special_diet']
        # if feast == 55:
        #     feast_data = "This%20time%20you%20only%20had%20Lunch%20on%20the%20feast%20day."
        # if feast == 180:
        #     feast_data = "This%20time%20you%20had%20Breakfast%20and%20Dinner%20on%20the%20feast%20day."
        # if feast == 235:
        #     feast_data = "This%20time%20you%20had%20Breakfast,%20Lunch%20and%20Dinner%20on%20the%20feast%20day."
        # if feast == 150:
        #     feast_data = "This%20time%20you%20only%20had%20Dinner%20on%20the%20feast%20day."
        # if feast == 85:
        #     feast_data = "This%20time%20you%20only%20had%20Lunch%20on%20the%20feast%20day."
        # if feast == 0:
        #     feast_data = "Sadly%20we%20missed%20the%20feast%20day%20this%20time."
        
        
# sudeshna.datta@ils.res.in,Sudeshna Datta,12,1795,17,5,8,1,2,3,3,180,1975,1975
# rakeshmohapatra516@gmail.com,Rakesh Mohapatra,13,3420,26,25,14,3,3,5,1,205,3625,3625
# sharadsingh1406@gmail.com,Sharad Singh,23,3305,29,12,14,3,3,5,4,205,3510,3510
# prustysubhasish.09@gmail.com,Subhasish Prusty,13,2790,24,15,12,3,3,4,2,235,3025,3025
        # message ="Sadly%20we%20missed%20the%20feast%20day%20this%20time."
        
        # message= f"Hello%20{name},%0a%0aThanks%20for%20avaling%20Students'%20Mess%20for%20the%20month%20of%20july.%20Hope%20you%20are%20doing%20well.%20%0a%0aSummary%20for%20the%20month%20of%20July%202023%0a---------%0a%0aThis%20month%20you%20had%20{total_number_of_breakfasts}%20breakfasts,%20{total_number_of_lunch}%20lunchs%20and%20{total_number_of_dinner}%20dinners.%20%0aThe%20lunch%20includes,%0a{total_base_meals}%20regular%20meals,%0a{total_number_of_checken}%20chicken%20or%20equivallent%20veg%20meals,%0a{total_number_of_fish}%20fish%20or%20equivallent%20veg%20meals,%0a{total_number_of_egg}%20egg%20or%20equivallent%20veg%20meals,%0a{total_sunday_meals}%20sunday%20meals.%0a%0aAlong%20with%20this%20we%20also%20had%20a%20Feast%20this%20month.{feast_data}%20So%20for%20this%20month%20your%20monthly%20bill%20is%20of%20*Rs.{final_bill}*%2F-.%0a%0aPlease%20pay%20the%20bill%20of%20*Rs.{final_bill}*%20on%20or%20before%203rd%20August%20for%20a%20smoother%20running%20of%20the%20mess.%0a%0aUPI%20-%208908241864@kotak%0a%0a%0a%0a%0a(This%20is%20an%20experimental%20feature%20still%20in%20development)"
        Food_eaten = generate_message(data.loc[i])
        print("yes doing good")
        # message = f"Hello {name},%0a%0a Thanks for availing students mess for the month of september. Hope you are doing well. %0a%0a This month you have eaten {Food_eaten} which made you total bill of {final_bill} rupees"
        message = f'''Hello *{name}*,%0a%0a

Thanks for availing Students' Mess for the month of April. Hope you are doing well.

%0a%0aSummary for the month of April%0a
-----------------------------%0a%0a

This month you had : {Food_eaten}.%0a%0a


So for this month your monthly bill is of *Rs.{final_bill}*%2F-.

Please pay this bill of *Rs.{final_bill}* on or before 4th May for the smooth running of the mess.%0a%0a
%0a%0a*For any issue related to the bill please contact Mess Committee at studentsmess.ils@gmail.com or Students Affairs Committee at studentsaffairs.ils@gmail.com.*
%0a%0a> _Developed with \U0001F49B by Bineet_
'''
        print(style.YELLOW + f'{number}' + style.RESET)
        # message = "Bineet is awesome"
        print("Yup going good")
        try:
            url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
            sent = False
            print(url)
            print("Initializing")
            for i in range(2):
                if not sent:
                    print("Gooing good")
                    driver.get(url)
                    try:
                        print("Happening")
                        # click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))click_btn = WebDriverWait(driver, 35).until(
                        click_btn = WebDriverWait(driver, delay).until(
                        # EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx'))
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
        
                        )
        
# //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button
                    except Exception as e:
                        print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/2)")
                        print("Check the interet connection if its persists"+ style.RESET)
                        not_send.append(i)
                    else:
                        sleep(2)
                        click_btn.click()
                        sent=True
                        sleep(2)
                        print(style.GREEN + 'Message sent to: ' + number + style.RESET)
        except Exception as e:
            print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
            not_send.append(i)
            
    except:
        print("May be Improper allocation of names")
        pass
driver.close()

print(not_send)
#         message = "Hello"
#         # message= f"Hello%20{name},%0a%0aThanks%20for%20avaling%20Students'%20Mess.%20Hope%20you%20are%20doing%20well.%20%0a%0aSummary%20of%20the%20month%20of%20July%202023%0a---------%0a%0aThis%20month%20you%20had%20{total_number_of_breakfasts}%20breakfasts,%20{total_number_of_lunch}%20lunchs%20and%20{total_number_of_dinner}%20dinners.%20%0aThe%20lunch%20includes,%0a{total_base_meals}%20regular%20meals,%0a{total_number_of_checken}%20chicken%20or%20equivallent%20veg%20meals,%0a{total_number_of_fish}%20fish%20or%20equivallent%20veg%20meals,%0a{total_number_of_egg}%20egg%20or%20equivallent%20veg%20meals,%0a{total_sunday_meals}%20sunday%20meals.%0a%0aAlong%20with%20this%20we%20also%20had%20a%20Feast%20this%20month.{feast_data}%20So%20for%20this%20month%20your%20monthly%20bill%20is%20of%20Rs.{final_bill}%2F-.%0a%0aTo%20pay%20this%20bill%20please%20click%20on%20this%20link%20below.%20%0a%0aupi:%2F%2Fpay?pa=8908241864@kotak&pn=Bineet%20Kumar%20Mohanta&am={final_bill}&cu=INR%0a%0a%0a%0a%0a(This%20is%20a%20test%20run%20of%20a%20progam%20developped%20by%20Bineet.%20Please%20tell%20if%20we%20can%20implement%20it%20this%20time%20or%20not)"
#         # message = f"Hello {name},%0a        %0aThanks for avaling Students' Mess. Hope you are doing well.%0a%0aSummary of the month of July 2023%0a---------%0a%0aThis month you had {total_number_of_breakfasts} breakfasts, {total_number_of_lunch} lunchs and {total_number_of_dinner} dinners.%0aThe lunch includes,%0a{total_base_meals} regular meals, %0a{total_number_of_checken} chicken or equivallent veg meals,%0a{total_number_of_fish} fish or equivallent veg meals,%0a{total_number_of_egg} egg or equivallent veg meals,%0a{total_sunday_meals} sunday meals.%0a%0aAlong with this we also had a Feast this month.{feast_data}%0a%0a%0a%0aSo for this month your monthly bill is of Rs.{final_bill}/-%0a%0aTo pay this bill please click on this link below.%0a%0aupi://pay?pa=8908241864@kotak&pn=Bineet%20Kumar%20Mohanta&am={final_bill}&cu=INR%0a%0a%0a%0a(This is a test run of a progam developped by Bineet. Please tell if we can implement it this time or not)"
# #         message = f"""Hello {name},
        
# # Thanks for avaling Students' Mess. Hope you are doing well.

# # Summary of the month of July 2023
# # ---------

# # This month you had {total_number_of_breakfasts} breakfasts, {total_number_of_lunch} lunchs and {total_number_of_dinner} dinners.
# # The lunch includes,
# # {total_base_meals} regular meals, 
# # {total_number_of_checken} chicken or equivallent veg meals,
# # {total_number_of_fish} fish or equivallent veg meals,
# # {total_number_of_egg} egg or equivallent veg meals,
# # {total_sunday_meals} sunday meals.

# # Along with this we also had a Feast this month.{feast_data}



# # So for this month your monthly bill is of Rs.{final_bill}/-

# # To pay this bill please click on this link below.

# # upi://pay?pa=8908241864@kotak&pn=Bineet%20Kumar%20Mohanta&am={final_bill}&cu=INR
# # %0a = Line Breake
# # %20 = sapce
# upi://pay?pa=8250568935@kotak&pn=Surajit%20Gandhi&am=250&cu=INR

# # (This is a test run of a progam developped by Bineet. Please tell if we can implement it this time or not)
# #         """
        
#         # print(message)
#         url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
#         print(url)
        
#         sent = False
        
#         for i in range(3):
#             if not sent:
#                 driver.get(url)
#                 try:
#                     click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
#                 except Exception as e:
#                     print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                    
#             else:
#                 sleep(1)
#                 click_btn.click()
#                 sent=True
#                 sleep(3)
#                 print(style.GREEN + 'Message sent to: ' + number + style.RESET)
#     except Exception as e:
#         print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
        
# driver.close()
              
              
              
              
              
                    
            
					
					
					
					
					
        
        
        
        
        

		
		
		
			
				

				
	
		
