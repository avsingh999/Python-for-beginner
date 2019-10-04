# Current time

import datetime

def current_time():
    x = datetime.datetime.now()
    print(x)



def time_conversion(i):
    
    if i==a:
        x = datetime.datetime(2018, 6, 1)

        print(x.strftime("%d-%m-%Y"))
    if i==b:
        x = datetime.datetime(2018, 6, 1)

        print(x.strftime("%d/%m/%Y"))



# Timedelta function demonstration  

print("Enter which date you want past/future")
def timedelta(i):
        # Using current time 
        ini_time_for_now = datetime.datetime.now() 

        # printing initial_date 
        print ("initial_date", str(ini_time_for_now)) 
        
        
        
        # Calculating past dates 
        if i == "past": 
                d = int(input("No. of Days in past    : "))
                w = int(input("No. of Weeks in past   : "))
                h = int(input("No. of hours in past   : "))
                m = int(input("No. of minutes in past : "))
                s = int(input("No. of seconds in past : "))
                def past_date(d,w,h,m,s):

                        past_date_before = ini_time_for_now - datetime.timedelta(days = d, minutes=m, hours=h, weeks=w,seconds=s) 

                        # printing calculated past_dates 
                        print('past_date_before_2yrs:', str(past_date_before)) 
                past_date(d,w,h,m,s)
        # date in future
        
        if i == "future": 
                d = int(input("No. of Days in future    : "))
                w = int(input("No. of Weeks in future   : "))
                h = int(input("No. of hours in future   : "))
                m = int(input("No. of minutes in future : "))
                s = int(input("No. of seconds in future : "))
                def future_date(d,w,h,m,s):

                        future_date_before = ini_time_for_now + datetime.timedelta(days = d, minutes=m, hours=h, weeks=w,seconds=s) 

                        # printing calculated past_dates 
                        print('past_date_before_2yrs:', str(future_date_before)) 
                future_date(d,w,h,m,s)