# Python Email Automation Bot

A modular Python application for sending automated emails via SMTP.
Built to demonstrate clean architecture, secure configuration, and professional engineering practices.

# Features

SMTP email sending (Gmail supported)

Bulk / repeated email delivery

Environment-variable based secrets

Centralized logging

Rate limiting

Clean, extensible design

# Project Structure
email_bot/
├── main.py          # Entry point
├── email_client.py  # Email logic
├── config.py        # Configuration
├── logger.py        # Logging

# Setup
Windows (PowerShell)

setx SENDER_EMAIL "your_email@gmail.com"
setx EMAIL_PASSWORD "your_app_password"

# Usage

Configure recipients and message in main.py, then run:

python main.py

# Notes

Designed for learning and authorized email automation

Credentials are never hardcoded

Easily extendable for templates, CLI usage, or third-party email services