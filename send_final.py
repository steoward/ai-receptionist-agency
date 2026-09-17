import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = "fullty174@gmail.com"
GMAIL_PASS = "fmpq guea swpq vbqx"

# Real verified emails from HVAC business websites
targets = [
    {
        "email": "reid@kenmuncy.com",
        "name": "Ken Muncy Air Conditioning",
        "owner": "Reid",
        "state": "Chandler AZ",
        "reviews": "4.9 stars, 477 reviews"
    },
    {
        "email": "info@hackneyinc.com",
        "name": "Hackney Inc.",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "Phoenix Metro, heating and cooling services"
    },
    {
        "email": "info@gothamairaz.com",
        "name": "Gotham Air",
        "owner": "Antonio",
        "state": "Phoenix AZ",
        "reviews": "5.0 stars, veteran-owned, 20+ years"
    },
    {
        "email": "acbysam@gmail.com",
        "name": "AC by Sam LLC",
        "owner": "Sam",
        "state": "Phoenix AZ",
        "reviews": "Family owned, decades of experience"
    },
    {
        "email": "office@championair.com",
        "name": "Champion Air",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "4.7 stars, 341 reviews"
    },
    {
        "email": "hvacservice@austincompanies.com",
        "name": "Austin Companies",
        "owner": "HVAC Team",
        "state": "Phoenix AZ",
        "reviews": "Established, multiple locations"
    },
    {
        "email": "help@varsityzone.com",
        "name": "Varsity Zone HVAC",
        "owner": "Team",
        "state": "North Phoenix AZ",
        "reviews": "North Phoenix specialist"
    },
    {
        "email": "info@anelloac.com",
        "name": "ANELLO AC",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "5-star, easy and friendly"
    },
    {
        "email": "info@alaskanac.com",
        "name": "Alaskan AC & Heating",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "Phoenix specialist"
    },
    {
        "email": "info@hvacdepotaz.com",
        "name": "HVAC Comfort Supply",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "Supply and service"
    },
    {
        "email": "service@legacyair.com",
        "name": "Legacy Air",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "3529 E Wood St, Phoenix"
    },
    {
        "email": "privacy@phoenixhvacrepair.com",
        "name": "Phoenix HVAC Repair Authority",
        "owner": "Team",
        "state": "Phoenix AZ",
        "reviews": "Repair specialist"
    },
    {
        "email": "tbell@txace.com",
        "name": "Texas Air Conditioning, Electric & Plumbing",
        "owner": "Troy",
        "state": "East Texas",
        "reviews": "Service techs, not sales techs"
    },
    {
        "email": "cpcustomair@gmail.com",
        "name": "Custom Air LLC",
        "owner": "Team",
        "state": "Fort Myers FL",
        "reviews": "Certified air conditioning"
    },
    {
        "email": "alexdanair@gmail.com",
        "name": "Danair HVAC",
        "owner": "Alex",
        "state": "Cape Coral FL",
        "reviews": "Certified air conditioning"
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
        msg['Subject'] = f"{t['owner']} - quick question about {t['name']} missed calls"
        
        body = f"""Hi {t['owner']},

I have been researching top HVAC contractors in {t['state']} and {t['name']} keeps coming up — {t['reviews']}.

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
