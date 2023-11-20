# Python Email Client Script

## Description

This script enables the sending and receiving of emails through Python. It utilizes the `smtplib` library for sending emails and `imaplib` for receiving them. The script is configured for a specific email service provider but can be adapted for others by changing the server details.

## Features

1. **Send Emails**: Uses `smtplib` to send emails. Specify the subject, body, and recipient.
2. **Receive Emails**: Uses `imaplib` to read emails from the inbox. It filters emails based on specific criteria (e.g., sender's address) and prints the email's content.

## Configuration

- `smtp_server`: SMTP server address for sending emails.
- `imap_server`: IMAP server address for receiving emails.
- `email_address`: Your email address.
- `password`: Your email account password.

## Functions

1. `send_email(subject, body, to)`: Sends an email with the specified subject, body, and recipient.
   
2. `get_inbox()`: Fetches and prints emails from the inbox, handling both multipart and non-multipart emails, and extracts the text content.

## Usage

- Update `smtp_server`, `imap_server`, `email_address`, and `password` with your details.
- Use `send_email()` to send an email.
- Use `get_inbox()` to view emails from your inbox.

## Notes

- This script is for educational purposes. Adapt it with proper security measures for practical use.
- Ensure necessary permissions and settings are enabled in your email account for SMTP and IMAP access.

