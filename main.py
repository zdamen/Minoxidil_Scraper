from dotenv import load_dotenv
import traceback
from Scraping_Functions import *
import requests
import time
import json
from operator import *
from twilio.rest import Client
import logging
import os

load_dotenv()  # Load the environment variables from the .env file

logging.basicConfig(level=logging.INFO)


# pre req info serving size
# 1 month of minoxidil foam = 60ml
# 1 month of minoxidil solution = 60g
# 1 month of finasteride = 30 1mg tabs

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
your_phone_number = os.getenv('YOUR_PHONE_NUMBER')

def send_twilio_message(body):
    print(f'Account SID: {account_sid}\nAuth Token: {auth_token}')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=your_phone_number
    )
    logging.info(f'Message sent: {message.sid} with the message {body}')


if __name__ == "__main__":
    data = {'MinoxidilFoam': {}, 'MinoxidilSolution': {}, 'Finasteride': {}}
    sleeptime = 5
    while True:
        logging.info(time.asctime())
        time.sleep(sleeptime)
        logging.info(time.asctime())
        try:
            GetAllPrices(data)
        except Exception as e:
            tb = traceback.extract_tb(e.__traceback__)
            last_call = tb[-1]
            send_twilio_message(f"Exception caught in function: {last_call.name}\n Error message: {e} \n sleeping for 5 hours")
            time.sleep(4*sleeptime)
            continue

        data['MinoxidilFoam'] = sorted(data['MinoxidilFoam'].items(), key=itemgetter(1))
        data['MinoxidilSolution'] = sorted(data['MinoxidilSolution'].items(), key=itemgetter(1))
        data['Finasteride'] = sorted(data['Finasteride'].items(), key=itemgetter(1))

        logging.info(data)
        api_endpoint = 'https://minoxidilscraperapi.azurewebsites.net/UpdateData'
        response = requests.post(api_endpoint, json=data)

        if response.status_code == 200:
            logging.info('Data was posted successfully')
        else:
            logging.error('Error posting data')
        data = {'MinoxidilFoam': {}, 'MinoxidilSolution': {}, 'Finasteride': {}}
        logging.info(f'i emptied the data{data}')


