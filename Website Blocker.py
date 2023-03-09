import time
from datetime import datetime as dt

host_file_path="C:\Windows\System32\drivers\etc\hosts"
local_host="127.0.0.1"

websites_list=["www.facebook.com","facebook.com","instagram.com","www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,15,00)< dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,15,37):
        with open(host_file_path,"r+") as file:
            content=file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(local_host+" "+website+"\n")
        print("Websites have Blocked\n")
        break
    
    else:
        with open(host_file_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        
        print("Time is over and All Websites have unblocked")
        break



        




   




            
               

            







