from icmplib import ping
import utils.format

def ping (address):
    host = ping(address, count=1)

    is_alive = False
    ping = -1

    if host.is_alive:
        is_alive = True
        ping = utils.format.format_output(round(host.avg_rtt))

    return {
        "is_alive": is_alive,
        "ping": ping
    }