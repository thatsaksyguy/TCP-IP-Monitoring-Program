class ServiceRegistry:
  def __init__(self):
      self.services = {}

  def register_service(self, name, config):
      self.services[name] = config

  def enable_keepalive(self, socket):
      # Enables the TCP Keepalive feature for a given socket with specific keepalive options.
      socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
      # Set the TCP Keepalive interval
      socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
      socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 1)
      socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)