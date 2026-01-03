from email_client import EmailClient
from logger import setup_logger

def main():
    logger = setup_logger()

    recipients = [
        "test1@gmail.com",
        "test2@gmail.com"
    ]

    message_body = (
        "Hello,\n\n"
        "This is an automated message generated for testing purposes.\n\n"
        "Regards,\n"
        "Python Email Bot"
    )

    client = EmailClient(logger)

    client.send_bulk(
        recipients=recipients,
        body=message_body,
        repeat=3
    )

if __name__ == "__main__":
    main()
