import json

class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.configs = None

    def load_configs(self):
        try:
            with open(self.config_path, 'r') as file:
                self.configs = json.load(file)
        except FileNotFoundError:
            print(f"Configuration file not found: {self.config_path}")

    def save_config(self, config, save_path):
        try:
            with open(save_path, 'w') as file:
                json.dump(config, file, indent=4)
                self.config_path = save_path
                self.configs = config
        except Exception as e:
            print(f"Failed to save configuration: {e}")