from abc import ABC, abstractmethod

class ANotification(ABC):
    @abstractmethod
    def send(self, text: str) -> None:
        pass

class EmailClient(ANotification):
    def __init__(self, email: str) -> None:
        self.email = email

    def send(self, text: str) -> None:
        print(f"[EMAIL to={self.email}] {text}")


class SmsClient(ANotification):
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def send(self, text: str) -> None:
        print(f"[SMS to={self.phone_number}] {text}")


class NotificationService:
    def __init__(self, notifications: list[ANotification]) -> None:
        self.notifications = notifications

    def notify(self, text: str) -> None:
        for notification in self.notifications:
            notification.send(text)
