# Send emails via Gmail SMTP
# Run this script with your Gmail app password

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body, from_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    print(f"Email sent to {to_email}")

# Recipients
recipients = [
    ("info@gothamairaz.com", "Gotham Air"),
    ("acbysam@gmail.com", "AC by Sam LLC"),
    ("contact@sapperhvac.com", "Sapper HVAC")
]

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

print("Email script ready. Provide Gmail credentials to send.")
print(f"Recipients: {[r[0] for r in recipients]}")
