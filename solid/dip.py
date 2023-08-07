# Abstractions should not depend upon details. Details should depend upon abstractions.

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, subject, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    def __init__(self, message_sender):
        self.message_sender = message_sender

    def send_notification(self, recipient, message):
        self.message_sender.send_message(recipient, "Notification", message)

# Using the NotificationService to send a notification
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("ram@fusemachines.com", "Hello, this is a notification!")
