
import smtplib
import imaplib
import email
from email.mime.text import MIMEText

# Email settings
smtp_server = "smtp.poczta.onet.pl" #server for sending emails smtp
imap_server = "imap.poczta.onet.pl"#server for receiving emails imap
email_address = "email_adresse"#email adresse
password = "password_of_email_adresse"#password of email adresse

# Sending an email
def send_email(subject, body, to): #subject, body, to -> def function for sending email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to

    with smtplib.SMTP_SSL(smtp_server, 465) as server:
        server.login(email_address, password)
        server.sendmail(email_address, to, msg.as_string())

# Receiving emails
def get_inbox():#def function for receiving emails
    with imaplib.IMAP4_SSL(imap_server) as mail:
        mail.login(email_address, password)
        mail.select('inbox')

        typ, data = mail.search(None, 'ALL')
        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            if  "women@forbes.pl" in msg['From']:
                print("Found the test email!")
                print(f"Raw email:\n{raw_email}\n")
                print("------------------------------------------")
            print(f"From: {msg['from']}")
            print(f"Subject: {msg['subject']}")

            # Check if the email message is multipart
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    # Extract text content from email
                    if "attachment" not in content_disposition and content_type in ["text/plain", "text/html"]:
                        text = part.get_payload(decode=True).decode()
                        #print(f"Content:\n{text}\n")
            else:
                # Extract content from non-multipart email
                text = msg.get_payload(decode=True).decode()
                #print(f"Content:\n{text}\n")
# Example usage
if __name__ == "__main__":
    #send_email("Test Subject", "Hello, this is a test email.", "receiver_email@gmail.com")
    get_inbox()
