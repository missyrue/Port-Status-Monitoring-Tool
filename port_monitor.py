from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

LOG_FILE = "port_status.log"

def log_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {message}"

    print(full_msg)

    with open(LOG_FILE, "a") as f:
        f.write(full_msg + "\n")


class PortMonitor(object):
    def __init__(self):
        core.openflow.addListeners(self)
        log.info("Port Status Monitoring Tool Started")

    def _handle_ConnectionUp(self, event):
        log_event(f"Switch connected: {event.dpid}")

    def _handle_PortStatus(self, event):
        port_no = event.port
        dpid = event.dpid

        if event.ofp.desc.state == 1:
            status = "DOWN"
            log_event(f"ALERT: Port {port_no} on Switch {dpid} is DOWN 🚨")
        else:
            status = "UP"
            log_event(f"Port {port_no} on Switch {dpid} is UP")

def launch():
    core.registerNew(PortMonitor)
