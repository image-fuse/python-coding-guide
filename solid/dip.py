from abc import ABC, abstractmethod

class MessageSender(ABC):
    """
    Abstract interface for message senders.
    """
    @abstractmethod
    def send_message(self, recipient: str, subject: str, message: str) -> None:
        """
        Send a message to the recipient with the specified subject and content.

        Parameters:
        recipient (str): The recipient's email address.
        subject (str): The subject of the message.
        message (str): The content of the message.

        Returns:
        None
        """
        pass

class EmailSender(MessageSender):
    def send_message(self, recipient: str, subject: str, message: str) -> None:
        """
        Send an email message to the recipient.

        Parameters:
        recipient (str): The recipient's email address.
        subject (str): The subject of the email.
        message (str): The content of the email.

        Returns:
        None
        """
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    def __init__(self, message_sender: MessageSender):
        """
        Initialize a NotificationService with a message sender.

        Parameters:
        message_sender (MessageSender): The message sender to use.

        Returns:
        None
        """
        self.message_sender = message_sender

    def send_notification(self, recipient: str, message: str) -> None:
        """
        Send a notification to the recipient using the assigned message sender.

        Parameters:
        recipient (str): The recipient's information.
        message (str): The content of the notification.

        Returns:
        None
        """
        self.message_sender.send_message(recipient, "Notification", message)

# Using the NotificationService to send a notification
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("ram@fusemachines.com", "Hello, this is a notification!")
