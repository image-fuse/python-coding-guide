from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """
    Abstract interface for payment processors.
    """
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Process a payment of the specified amount.

        Parameters:
        amount (float): The amount to be processed.

        Returns:
        None
        """
        pass

class RefundProcessor(ABC):
    """
    Abstract interface for refund processors.
    """
    @abstractmethod
    def process_refund(self, amount: float) -> None:
        """
        Process a refund of the specified amount.

        Parameters:
        amount (float): The amount to be refunded.

        Returns:
        None
        """
        pass

class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount: float) -> None:
        """
        Process an online payment of the specified amount.

        Parameters:
        amount (float): The amount of the payment.

        Returns:
        None
        """
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount: float) -> None:
        """
        Process a refund of the specified amount.

        Parameters:
        amount (float): The amount to be refunded.

        Returns:
        None
        """
        print(f"Processing refund of ${amount}")

class PaymentHandler:
    def __init__(self, payment_processor: PaymentProcessor):
        """
        Initialize a PaymentHandler with a payment processor.

        Parameters:
        payment_processor (PaymentProcessor): The payment processor to use.

        Returns:
        None
        """
        self.payment_processor = payment_processor

    def handle_payment(self, amount: float) -> None:
        """
        Handle a payment using the assigned payment processor.

        Parameters:
        amount (float): The amount to be handled.

        Returns:
        None
        """
        self.payment_processor.process_payment(amount)

class RefundHandler:
    def __init__(self, refund_processor: RefundProcessor):
        """
        Initialize a RefundHandler with a refund processor.

        Parameters:
        refund_processor (RefundProcessor): The refund processor to use.

        Returns:
        None
        """
        self.refund_processor = refund_processor

    def handle_refund(self, amount: float) -> None:
        """
        Handle a refund using the assigned refund processor.

        Parameters:
        amount (float): The amount to be handled.

        Returns:
        None
        """
        self.refund_processor.process_refund(amount)

if __name__ == "__main__":
    online_payment_processor = OnlinePaymentProcessor()
    
    payment_handler = PaymentHandler(online_payment_processor)
    payment_handler.handle_payment(100)
    
    refund_handler = RefundHandler(online_payment_processor)
    refund_handler.handle_refund(50)
