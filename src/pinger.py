import pingers.icmp_pinger
import pingers.tcp_pinger
import pingers.mc_pinger

import copy

class Pinger:
    def __init__ (self, config):
        self.config = config
        self.cached = []
        self.services = config.get_services()

        for service in self.services:
            service["history"] = []

    def get_values (self):
        return {"services": self.cached}

    def ping_service (self, service):
        print("Pinging service " + service["name"] + " at " + service["address"] + ":" + str(service["port"]))
        if service["connection"] == "tcp":
            return pingers.tcp_pinger.ping(service["address"], service["port"])
        elif service["connection"] == "icmp":
            return pingers.icmp_pinger.ping(service["address"])
        elif service["connection"] == "minecraft":
            return pingers.mc_pinger.ping(service["address"], service["port"])

    def ping_all (self):
        print("Pinging all...")
        cache = []
        for service in self.services:
            result = self.ping_service(service)
            data = copy.deepcopy(service)
            data["result"] = result

            if len(service["history"]) >= 42:
                service["history"].pop(0)

            service["history"].append(result)

            if self.config.is_hide_port():
                data["port"] = "hidden"
            if self.config.is_hide_address():
                data["address"] = "hidden"
            cache.append(data)

        self.cached = cache