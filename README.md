TCP/IP Monitoring Program - Jonathan Saks

Introduction:
Hello and welcome to my TCP/IP program. This program is intended to provide a management service that monitors multiple servers, and tracks connectivity and status. It is capable of handling TCP connection tests for specified servers/ports, managing configurations for monitoring different servers, and displays the results in real-time. The system is designed to be robust, retrying connections and saving messages when the management service or monitored server becomes unreachable.

----------------------------------------------------------------------------------------------
Requirements:
- Python 3.6 or newer
- Any operating system (Windows, MacOS, Linux)
- Network access to the specified servers you wish to monitor
----------------------------------------------------------------------------------------------
Installation:
1. Make sure that the latest version of Python is installed.
2. Install all necessary package dependencies: pip install -r requirements.txt
----------------------------------------------------------------------------------------------
Usage:
The following command will establish a server at a specified IP/port: python python_server.py
1. Go to python_server.py
2. Adjust the IP/port according to what you're wanting
3. Run the following command "python python_server.py"

The following command starts the MONITORING SERVICE: python monitoring_service.py
The program will then:
  1. Start listening on a designated port
  2. Accept configuration from the management service
  3. Perform configure checks
  4. Send results back to management service
  5. Listen for new configurations
  6. Run continuously

The following command starts the MANAGEMENT SERVICE: python management_service.py
The program will then:
  1. Prompt the user to either create or load a configuration file for monitoring the servers
  2. Display the current configuration (or allow for modification, if need-be)
  3. Start monitoring, showing real-time connection statuses/results
NOTE: As it is right now, it is hardcoded to listen to a specific ip and port (127.0.0.1; 65432). If you would like to listen to something different, you will need to change the ip and port in management_service.py, python_server.py, and/or monitoring_service.py (comments made above the areas that would be changed).
----------------------------------------------------------------------------------------------
Management Service Commands:
"1" - Creates or loads configuration file (.json)
"2" - View the current configuration
"3" - Displays the real-time monitoring results
"4" - Exits the program
