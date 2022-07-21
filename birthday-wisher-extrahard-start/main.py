##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib
data = pandas.read_csv('birthdays.csv')
now = dt.datetime.now()
today_tuple = (now.month, now.day)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# #birthday = data[data.month == 4]
# if now.month == int(birthday.month) and now.day == int(birthday.day):
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    PLACEHOLDER = "[NAME]"
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, birthday_person["name"])
        with smtplib.SMTP('smtp.gmail.com') as server:
            server.starttls()
            server.login('gen2proff@gmail.com', 'gen2;soul')
            server.sendmail(
                'gen2proff@gmail.com',
                birthday_person.email,
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
                    )





