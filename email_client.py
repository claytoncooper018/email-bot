import smtplib
import time
from email.message import EmailMessage
from typing import List

from config import Config

class EmailClient:
    def __init__(self, logger):
        self.logger = logger
        Config.validate()

    def _connect(self):
        self.logger.debug("Connecting to SMTP server")
        server = smtplib.SMTP_SSL(Config.SMTP_SERVER, Config.SMTP_PORT)
        server.login(Config.SENDER_EMAIL, Config.EMAIL_PASSWORD)
        return server

    def send_email(self, recipient: str, subject: str, body: str):
        msg = EmailMessage()
        msg["From"] = Config.SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            with self._connect() as server:
                server.send_message(msg)
                self.logger.info(f"Email sent to {recipient}")
        except Exception as e:
            self.logger.error(f"Failed to send email to {recipient}: {e}")
            raise

    def send_bulk(
        self,
        recipients: List[str],
        body: str,
        subject: str = Config.DEFAULT_SUBJECT,
        repeat: int = 1
    ):
        self.logger.info("Starting bulk email job")

        for r in range(repeat):
            self.logger.info(f"Round {r + 1}/{repeat}")

            for recipient in recipients:
                self.send_email(recipient, subject, body)
                time.sleep(Config.RATE_LIMIT_SECONDS)

        self.logger.info("Bulk email job completed")
