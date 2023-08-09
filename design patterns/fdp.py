"""
This script demonstrates the Factory Design Pattern for creating different types of loggers.
"""

from abc import ABC, abstractmethod

# Product Interface
class Logger(ABC):
    """
    Abstract interface for loggers.
    """
    @abstractmethod
    def log(self, message):
        """
        Log a message.

        Parameters:
        message (str): The message to be logged.

        Returns:
        None
        """
        pass

# Concrete Products
class FileLogger(Logger):
    """
    Concrete logger class that logs messages to a file.
    """
    def log(self, message):
        """
        Log a message to a file.

        Parameters:
        message (str): The message to be logged.

        Returns:
        None
        """
        with open('log.txt', 'a') as file:
            file.write(f"File Logger: {message}\n")

class ConsoleLogger(Logger):
    """
    Concrete logger class that logs messages to the console.
    """
    def log(self, message):
        """
        Log a message to the console.

        Parameters:
        message (str): The message to be logged.

        Returns:
        None
        """
        print(f"Console Logger: {message}")

class DatabaseLogger(Logger):
    """
    Concrete logger class that logs messages to a database (simulated).
    """
    def log(self, message):
        """
        Log a message to the database.

        Parameters:
        message (str): The message to be logged.

        Returns:
        None
        """
        # Simulating database interaction
        print(f"Database Logger: {message} (Saved to database)")

# Creator (Factory)
class LoggerFactory:
    """
    Factory class for creating different types of loggers.
    """
    @staticmethod
    def create_logger(logger_type):
        """
        Create and return a logger instance based on the logger type.

        Parameters:
        logger_type (str): The type of logger to create.

        Returns:
        Logger: An instance of the specified logger type.
        """
        if logger_type == 'file':
            return FileLogger()
        if logger_type == 'console':
            return ConsoleLogger()
        if logger_type == 'database':
            return DatabaseLogger()

        raise ValueError("Invalid logger type")

# Example usage
if __name__ == "__main__":
    logger_type = input("Enter logger type (file/console/database): ")
    logger = LoggerFactory.create_logger(logger_type)

    message = input("Enter log message: ")
    logger.log(message)
