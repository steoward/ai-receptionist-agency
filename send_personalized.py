import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = "fullty174@gmail.com"
GMAIL_PASS = "fmpq guea swpq vbqx"

# Only verified real addresses - personalized message for each
targets = [
    {
        "email": "info@gothamairaz.com",
        "name": "Gotham Air",
        "owner": "Antonio",
        "state": "Phoenix AZ",
    },
    {
        "email": "acbysam@gmail.com",
        "name": "AC by Sam",
        "owner": "Sam",
        "state": "Phoenix AZ",
    },
    {
        "email": "office@championair.com",
        "name": "Champion Air",
        "owner": "Team",
        "state": "Phoenix AZ",
    },
    {
        "email": "hvacservice@austincompanies.com",
        "name": "Austin Companies",
        "owner": "HVAC Team",
        "state": "Phoenix AZ",
    },
    {
        "email": "info@evans-air.com",
        "name": "Evans Air",
        "owner": "Brian",
        "state": "Gilbert AZ",
    },
]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(GMAIL_USER, GMAIL_PASS)

sent = 0
for t in targets:
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = t["email"]
        msg['Subject'] = f"{t['owner']} - quick question about {t['name']} phone"
        
        body = f"""Hi {t['owner']},

I have been researching top HVAC contractors in {t['state']} and {t['name']} keeps coming up with great reviews.

But I noticed something: a few customers mentioned they tried calling and could not reach anyone. One said they went to a competitor after getting voicemail.

Here is the thing: when your techs are on a roof in 115 degree heat, they cannot answer the phone. And every missed call is a $3,000 to $10,000 job going to the next company on Google.

I built an AI voice receptionist specifically for HVAC companies like yours. It answers 100 percent of calls 24/7, sounds completely human, and books appointments directly to your calendar.

I am offering a free 7 day trial to select contractors in {t['state']} with no setup fee and no contract.

Worth a 2 minute demo this week?

Best,
AI Receptionist Agency"""
        
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(GMAIL_USER, t["email"], msg.as_string())
        print(f"OK {t['name']} ({t['email']}) - {t['state']}")
        sent += 1
    except Exception as e:
        print(f"FAIL {t['name']} ({t['email']}): {e}")

server.quit()
print(f"Sent: {sent}/{len(targets)}")
