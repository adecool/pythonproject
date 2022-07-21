import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 6.503090
MY_LONG = 3.392960

def iss_isoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour <= sunrise and time_now.hour >= sunset:
        return True
while True:
    time.sleep(60)
    if iss_isoverhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as server:
            server.starttls()
            server.login('gen2proff@gmail.com', 'gen2;soul')
            server.sendmail(
                'gen2proff@gmail.com',
                'gen2proff@gmail.com',
                msg='SUBJECT:Look up\n\nThe ISS is above you in the sky'
            )



