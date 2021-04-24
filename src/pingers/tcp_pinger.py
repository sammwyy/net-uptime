from tcp_latency import measure_latency
import utils.format

def ping (address, port):
    ping = measure_latency(host=address, port=port, runs=1, timeout=2.5)[0]
    is_alive = True

    if ping == None:
        ping = -1
        is_alive = False

    return {
        "ping": utils.format.format_output(round(ping)),
        "is_alive": is_alive
    }
