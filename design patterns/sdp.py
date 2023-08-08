class ConfigurationManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance
    
    def load_config(self):
        # Simulate loading configuration from a file
        self.config = {}
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                self.config[key] = value
    
    def get_config(self, key):
        return self.config.get(key)
    
# Demonstration
config_manager1 = ConfigurationManager()
config_manager2 = ConfigurationManager()

print(config_manager1 is config_manager2)  # Both references point to the same instance

# Accessing configuration settings
setting1 = config_manager1.get_config('setting1')
setting2 = config_manager2.get_config('setting2')

print(setting1)
print(setting2)
