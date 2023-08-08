from abc import ABC, abstractmethod

# Product Interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Concrete Products
class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(f"File Logger: {message}\n")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Logger: {message}")

class DatabaseLogger(Logger):
    def log(self, message):
        # Simulating database interaction
        print(f"Database Logger: {message} (Saved to database)")

# Creator (Factory)
class LoggerFactory:
    @staticmethod
    def create_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type")

# Example usage
if __name__ == "__main__":
    logger_type = input("Enter logger type (file/console/database): ")
    logger = LoggerFactory.create_logger(logger_type)

    message = input("Enter log message: ")
    logger.log(message)
