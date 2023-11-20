Python Email Client Script
Description
This script enables the sending and receiving of emails through Python. It utilizes the smtplib library for sending emails and imaplib for receiving them. The script is configured for a specific email service provider but can be adapted for others by changing the server details.

Features
Send Emails: Uses smtplib to send emails. You can specify the subject, body, and recipient of the email.
Receive Emails: Uses imaplib to access and read emails from the inbox. It filters emails based on specific criteria (e.g., sender's address) and prints the email's content.
Configuration
smtp_server: SMTP server address for sending emails.
imap_server: IMAP server address for receiving emails.
email_address: The user's email address.
password: The password for the email account.
Functions
send_email(subject, body, to): Send an email with the specified subject, body, and recipient.

get_inbox(): Fetch and print emails from the inbox, filtering based on predefined criteria. It handles both multipart and non-multipart emails and extracts the text content.

Usage
To use this script:

Update the smtp_server, imap_server, email_address, and password with your own details.
Call send_email() to send an email.
Call get_inbox() to print emails from your inbox.
Notes
This script is for educational purposes and should be adapted with proper security measures for practical use.
Ensure that you have the necessary permissions and settings enabled in your email account for SMTP and IMAP access.
