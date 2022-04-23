#!/usr/bin/env python3

import os, sys
from datetime import date
from reports import generate_report
from emails import generate as generate_email, send as send_email

def report_formatter(file):
    with open(file) as item:
        lines = item.readlines()
    name = "name: " + lines[0].strip('\n')
    weight = "weight: " + lines[1].strip('\n')
    return "{}<br/>{}<br/><br/>".format(name, weight)

def main(argv):
    fruits_desc = "supplier-data/descriptions/"
    fruits_desc_files = [fruits_desc + f for f in os.listdir(fruits_desc)]
    report_body = ""
    for file in fruits_desc_files:
        report_body += report_formatter(file)
    attachment = "/tmp/processed.pdf"
    todays_date = date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(todays_date)
    generate_report(attachment, title, report_body)
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    mesg = generate_email("automation@example.com", "{}@example.com".format(os.environ.get('USER')), email_subject, email_body, attachment) 
    send_email(mesg)
    
if __name__ == "__main__":
      main(sys.argv)
