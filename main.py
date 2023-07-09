##################### Extra Hard Starting Project ######################

import random
import smtplib
import pandas
import datetime as dt

# 1. Update the birthdays.csv
birthdays = pandas.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
birthday_people = birthdays[(birthdays["day"] == day) & (birthdays['month'] == month)]

my_email = "testingsmtplib@email.com"
password = "QWERTY"


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

letter_files = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
letters = [open(file, 'r').read() for file in letter_files]

# 4. Send the letter generated in step 3 to that person's email address.

if not birthday_people.empty:
    for index, birthday_person in birthday_people.iterrows():
        random_letter = random.choice(letters)
        random_letter = random_letter.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy birthday!\n\n{random_letter}"
        )
