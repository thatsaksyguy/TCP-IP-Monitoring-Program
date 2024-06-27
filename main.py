import sys

from config_manager import ConfigManager
from connection_manager import ConnectionManager
from service_registry import ServiceRegistry
from task_distributor import TaskDistributor


def main_menu(service_registry, config_manager):
  while True:
      print("\nMain Menu:")
      print("1. Create or load configuration")
      print("2. View current configuration")
      print("3. Display results")
      print("4. Exit")
      choice = input("Enter your choice: ")
      if choice == "1":
          config_path = input("Enter configuration file path (or 'new' to create): ")
          if config_path.lower() == "new":
              # Gather user inputs for detailed configuration
              num_servers = int(input("How many servers would you like to monitor? "))
              servers_config = []
              for i in range(num_servers):
                  server = input(f"Enter address for server {i+1}: ")
                  port = int(input(f"Enter port for server {i+1}: "))
                  services = input(f"Enter services to monitor for server {i+1} (comma-separated, e.g., 'http,tcp'): ").split(',')
                  interval = int(input(f"Enter monitoring interval (in seconds) for server {i+1}: "))
                  servers_config.append({"server": server, "tcp": {"port": port}, "services": services, "interval": interval})

              # Create configuration dynamically
              new_config = {"servers": servers_config}
              save_path = input("Enter the path where you want to save the new configuration: ")
              config_manager.save_config(new_config, save_path)
          else:
              config_manager.config_path = config_path
              config_manager.load_configs()
      elif choice == "2":
          if config_manager.configs:
              print(f"Current Configuration: {config_manager.configs}")
          else:
              print("No configuration loaded.")
      elif choice == "3":
          display_results(service_registry, config_manager)
      elif choice == "4":
          print("Exiting...")
          sys.exit()
      else:
          print("Invalid choice. Please enter a number between 1 and 4.")

def display_results(service_registry, config_manager):
    if not config_manager.configs:
        print("No configuration loaded. Please load a configuration first.")
        return

    # Assuming services are registered and tasks need to be distributed
    task_distributor = TaskDistributor(service_registry, config_manager)
    task_distributor.distribute_tasks()

    connection_manager = ConnectionManager(config_manager, service_registry)
    connection_manager.establish_connections()

if __name__ == "__main__":
    service_registry = ServiceRegistry()
    config_manager = ConfigManager("")  # Empty path initially, will be set by user input

    main_menu(service_registry, config_manager)