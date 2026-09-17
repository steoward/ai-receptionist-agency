#!/usr/bin/env python3
"""
Send emails via Gmail SMTP.
Run this script to send outreach emails to HVAC/plumbing companies.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

# Email configuration - UPDATE THESE
GMAIL_USER = "fullty174@gmail.com"
# You need to generate an App Password from your Google Account:
# https://myaccount.google.com/apppasswords
# Or enable "Less secure app access" (not recommended)

# Recipients
recipients = [
    ("info@gothamairaz.com", "Gotham Air LLC"),
    ("acbysam@gmail.com", "AC by Sam LLC"),
]

# Email content
subject = "Quick question about your phone"

body = """Hi there,

I noticed your company while researching top HVAC contractors in Phoenix. Your Google reviews are solid — but I noticed a few customers mentioned trouble reaching you by phone.

I help HVAC companies answer 100% of inbound calls — even after hours, on weekends, and during busy season. No more sending customers to voicemail.

It's an AI voice receptionist that sounds completely human, books appointments directly to your calendar, and follows up with leads automatically.

I'm offering a free 7-day trial to select contractors in Phoenix — no setup fee, no contract.

Worth a 2-minute demo this week?

Best,
AI Receptionist Agency
"""

def send_emails():
    password = getpass.getpass(f"Enter Gmail password for {GMAIL_USER}: ")
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_USER, password)
    
    sent = 0
    for email, name in recipients:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server.sendmail(GMAIL_USER, email, msg.as_string())
        print(f"✓ Sent to {name} ({email})")
        sent += 1
    
    server.quit()
    print(f"\nTotal sent: {sent} emails")

if __name__ == "__main__":
    send_emails()
