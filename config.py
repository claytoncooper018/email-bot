import os

class Config:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    DEFAULT_SUBJECT = "Automated Message"
    RATE_LIMIT_SECONDS = 2

    @classmethod
    def validate(cls):
        if not cls.SENDER_EMAIL or not cls.EMAIL_PASSWORD:
            raise EnvironmentError(
                "Missing environment variables: SENDER_EMAIL or EMAIL_PASSWORD"
            )
