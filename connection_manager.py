class ConnectionManager:
  def __init__(self, config_manager, service_registry):
      self.config_manager = config_manager
      self.service_registry = service_registry

  def establish_connections(self):
      if not self.config_manager.configs:
          print("No configuration loaded.")
          return

      for server in self.config_manager.configs.get('servers', []):
          print(f"Establishing connection to {server['server']}")
          # Simulate connection establishment
          self.service_registry.register_service(server['server'], server)
          print(f"Connection established to {server['server']}")