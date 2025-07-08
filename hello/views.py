from django.shortcuts import render

from django.shortcuts import render, redirect
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN2 = os.getenv("TOKEN2")

def index(request):

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    import time
    

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1800, 1000)
    driver.get("https://www.pin880.com/en/standard/soccer/england-premier-league#period:0")
    time.sleep(15)
    ert=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/main/div/div/div[4]/div/div/div[2]/div[2]/div[1]/button/span').text

    
    from datetime import datetime
    current_datetime = str(datetime.now())
    b=current_datetime.split("-")
    c=b[0]
    d=b[1]
    e=b[2].split(" ")
    f=e[0]
    g=e[1]
    kl=g.split(".")
    io=kl[0]
    ty=io.replace(io[:2],str(int(io[:2])+3))
    date_new256=f+'.'+d+'.'+c+'  '+ty

    import pandas as pd
    ase=[[ert,date_new256]]


    header = ['run','end']
    df2 = pd.DataFrame(ase, columns=header)

   
    TOKEN1="440d864051de61f4b6463f10f8006898192b7420"
    TOKEN3="ash789@avid-stone-461407-q5.iam.gserviceaccount.com"
    TOKEN4 ="116197129399001621585"
    TOKEN5="https://www.googleapis.com/robot/v1/metadata/x509/ash789%40avid-stone-461407-q5.iam.gserviceaccount.com"

    credentials={
    "type": "service_account",
    "project_id": "avid-stone-461407-q5",
    "private_key_id": TOKEN1,
    "private_key": TOKEN2,
    "client_email": TOKEN3,
    "client_id": TOKEN4,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": TOKEN5,
    "universe_domain": "googleapis.com"
    }

    import gspread
    gc = gspread.service_account_from_dict(credentials)


    wks2 = gc.open("Test789").get_worksheet(2)
    list_of_lists = wks2.get_all_values()

    df5 = pd.DataFrame(list_of_lists)
    new_header = df5.iloc[0]
    df5 = df5[1:]
    df5.rename(columns=new_header, inplace=True)

    df7=pd.concat([df5,df2])
    wks2.update([df7.columns.values.tolist()]+df7.values.tolist())
    data = {"header": ert,"date":date_new256}



   
    return render(request, "index.html", context=data)

    