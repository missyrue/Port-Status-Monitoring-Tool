import re
from collections import defaultdict

LOG_FILE = "port_status.log"

class LogAnalyzer:
    def __init__(self):
        self.events = []
        self.stats = {
            "total": 0,
            "up": 0,
            "down": 0
        }
        self.port_activity = defaultdict(lambda: {"UP": 0, "DOWN": 0})

    def parse_logs(self):
        try:
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("❌ Log file not found!")
            return

        for line in lines:
            self.stats["total"] += 1

            if "DOWN" in line:
                self.stats["down"] += 1
                status = "DOWN"
            else:
                self.stats["up"] += 1
                status = "UP"

            # Extract port and switch using regex
            match = re.search(r"Port (\d+) on Switch (\d+)", line)
            if match:
                port = int(match.group(1))
                switch = int(match.group(2))

                self.port_activity[(switch, port)][status] += 1

                self.events.append({
                    "raw": line.strip(),
                    "switch": switch,
                    "port": port,
                    "status": status
                })

    def display_summary(self):
        print("\n========= LOG SUMMARY =========")
        print(f"Total Events : {self.stats['total']}")
        print(f"Ports UP     : {self.stats['up']}")
        print(f"Ports DOWN   : {self.stats['down']}")
        print("===============================\n")

    def display_port_analysis(self):
        print("\n====== PORT-WISE ANALYSIS ======")
        for (switch, port), data in self.port_activity.items():
            print(f"Switch {switch}, Port {port} -> UP: {data['UP']} | DOWN: {data['DOWN']}")
        print("================================\n")

    def display_timeline(self):
        print("\n========= EVENT TIMELINE =========")
        for event in self.events:
            print(event["raw"])
        print("==================================\n")

    def run(self):
        self.parse_logs()
        self.display_summary()
        self.display_port_analysis()
        self.display_timeline()


if __name__ == "__main__":
    analyzer = LogAnalyzer()
    analyzer.run()
