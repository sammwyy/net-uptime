import json

class ConfigParser:
    def __init__ (self):
        app_file = open("./config/app.json", "r")
        services_file = open("./config/services.json", "r")

        self.services = json.load(services_file)["services"]
        self.settings = json.load(app_file)

    def get_services (self):
        return self.services
        
    def get_name (self):
        return self.settings["app"]["name"]

    def get_description (self):
        return self.settings["app"]["description"]

    def get_icon (self):
        return self.settings["app"]["icon"]

    def get_check_interval (self):
        return self.settings["monitor"]["check_interval"]

    def is_hide_port (self):
        return self.settings["security"]["hide_ports"]

    def is_hide_address (self):
        return self.settings["security"]["hide_address"]