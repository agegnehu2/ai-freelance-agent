import os
import urllib.request
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(job_details):
    # Email configuration
    sender_email = "agegnehushibiru7@gmail.com"
    receiver_email = "agegnehushibiru7@gmail.com"
    
    # Your generated 16-character Google App Password
    app_password = "gtpr ydhf wlof qiga" 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"🚀 AI Agent: New Opportunity Found!"

    body = f"Hello Agegnehu,\n\nYour AI Freelance Agent has discovered a new opportunity:\n\n{job_details}\n\nBest regards,\nYour AI Agent"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("[+] Email notification sent successfully!")
    except Exception as e:
        print(f"[-] Failed to send email: {e}")

def main():
    user_name = "Agegnehu Shibiru"
    payout_wallet = "8muWk4hcw1v3GwtAKEF2nDrvVBBbvorky8NJ6kfDjSH"
    
    print(f"[+] AI Agent for {user_name} has started!")
    
    # Sample real-structured job to trigger email
    title = "Solana Smart Contract Review"
    reward = 500
    token = "USDC"
    
    proposal = (
        f"Job: {title}\nBudget: {reward} {token}\n\n"
        f"Generated Proposal:\n"
        f"\"Hello! I am {user_name}. I noticed your project '{title}' on Superteam. "
        f"With my skills in JavaScript, Python, Web3, and AI, I can deliver this perfectly. "
        f"Please send updates to my wallet: {payout_wallet}.\""
    )
    
    print(f"\n[Processing] Sending details to email...")
    send_email_notification(proposal)

if __name__ == "__main__":
    main()
    
