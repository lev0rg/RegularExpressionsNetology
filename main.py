from pprint import pprint
import re

import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for contact in contacts_list:
    name_parts = contact[0].split(" ")
    if len(name_parts) == 1:
        contact[0] = name_parts[0]
        contact[1] = ""
        contact[2] = ""
    elif len(name_parts) == 2:
        contact[0] = name_parts[0]
        contact[1] = name_parts[1]
        contact[2] = ""
    else:
        contact[0] = name_parts[0]
        contact[1] = name_parts[1]
        contact[2] = name_parts[2]

phone_pattern = r"(\+?\d{1,2})?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}\s?(?:доб\.?\s?\d+)?"
for contact in contacts_list:
    phone = contact[5]
    match = re.match(phone_pattern, phone)
    if match:
        formatted_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
        if match.group(6):
            formatted_phone += f" доб.{match.group(6)}"
        contact[5] = formatted_phone

unique_contacts = {}
for contact in contacts_list:
    key = (contact[0], contact[1])
    if key not in unique_contacts:
        unique_contacts[key] = contact
    else:
        existing_contact = unique_contacts[key]
        for i in range(3, len(contact)):
            if contact[i]:
                existing_contact[i] = contact[i]

contacts_list = list(unique_contacts.values())

with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

pprint(contacts_list)