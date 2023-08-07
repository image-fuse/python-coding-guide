# Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

class PaymentHandler:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def handle_payment(self, amount):
        self.payment_processor.process_payment(amount)

class RefundHandler:
    def __init__(self, refund_processor):
        self.refund_processor = refund_processor

    def handle_refund(self, amount):
        self.refund_processor.process_refund(amount)

if __name__ == "__main__":
    online_payment_processor = OnlinePaymentProcessor()
    
    payment_handler = PaymentHandler(online_payment_processor)
    payment_handler.handle_payment(100)
    
    refund_handler = RefundHandler(online_payment_processor)
    refund_handler.handle_refund(50)
