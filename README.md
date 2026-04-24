#  Port Status Monitoring Tool using SDN (Mininet + POX)

##  Student Details

* **Name:** Aaruni Choudhary
* **SRN:** PES2UG24CS013

---

##  Problem Statement

The goal of this project is to monitor sch port status in a Software Defined Network (SDN) environment.
The system detects port up/down events in real-time and logs them while generating alerts for failures.

---

##  Concept Overview

This project uses **event-driven monitoring** in SDN.

* The switch detects port changes
* It sends an OpenFlow **PortStatus event**
* The controller (POX) receives it
* The system logs and displays alerts

---

##  Tools & Technologies

* Mininet
* POX Controller
* Python

---

## 📁 Project Structure

```
pox/
└── ext/
    └── port_monitor.py
```

---

## ⚙️ Setup Instructions

### 1. Clone POX

```bash
cd ~
git clone https://github.com/noxrepo/pox.git
```

---

### 2. Add Controller File

```bash
cd ~/pox/ext
nano port_monitor.py
```

Paste the project code and save.

---

##  How to Run

### 🔹 Step 1: Start POX Controller

```bash
cd ~/pox
./pox.py log.level --DEBUG port_monitor
```

---

### 🔹 Step 2: Start Mininet (New Terminal)

```bash
sudo mn --controller=remote
```

---

##  Test Scenarios

###  Scenario 1: Normal Operation

```bash
pingall
```

**Expected Output:**

```
*** Ping: testing ping reachability
*** Results: 0% dropped (all hosts reachable)
```

---

###  Scenario 2: Port Failure Simulation

```bash
link s1 h1 down
```

Then:

```bash
pingall
```

**Expected Output:**

```
Some packets dropped / host unreachable
```

---

##  Sample Output (Controller Terminal)

```
[2026-04-21 12:30:10] Switch connected: 1
[2026-04-21 12:30:25] Port 1 on Switch 1 is UP
[2026-04-21 12:31:02] ALERT: Port 1 on Switch 1 is DOWN 🚨
```

---

## 📄 Log File Output

Check logs using:

```bash
cat port_status.log
```

Example:

```
[2026-04-21 12:31:02] ALERT: Port 1 on Switch 1 is DOWN 
```

---

##  Validation

* ✔ Port status detected correctly
* ✔ Logs generated with timestamps
* ✔ Alerts shown for failures
* ✔ Network behavior changes verified using ping


---

##  Key Features

* Real-time port monitoring
* Event-driven SDN architecture
* Logging system
* Failure alert mechanism

---

##  Conclusion

This project demonstrates how SDN controllers can monitor and react to network changes dynamically using OpenFlow events. It highlights the efficiency of event-driven architectures over traditional polling mechanisms.

