# Auto-Sec-Lab

# Automotive Security Lab

A hands-on automotive cybersecurity research project focused on vehicle network communication, CAN traffic analysis, and defensive monitoring.

## Project Overview

This project explores how automotive electronic control units communicate over Controller Area Network (CAN) and how software tools can monitor that communication for unusual behavior.

The lab currently uses a virtual CAN interface on Ubuntu, allowing experiments without connecting to a real vehicle.

## Current Features

- Ubuntu Linux lab running in Oracle VirtualBox
- Virtual CAN interface using Linux SocketCAN (`vcan0`)
- Synthetic CAN message generation with `can-utils`
- Python-based CAN traffic monitor using `python-can`
- Console output showing timestamps, arbitration IDs, payload lengths, and message data

## Technology Stack

- Python 3
- Ubuntu Linux
- Linux SocketCAN
- can-utils
- python-can
- Oracle VirtualBox
- Git and GitHub

## Repository Structure

```text
automotive-security-lab/
├── README.md
├── requirements.txt
├── src/
│   └── can_monitor.py
├── docs/
│   ├── lab-setup.md
│   └── findings.md
└── screenshots/
```

## Getting Started

### 1. Install dependencies

On Ubuntu:

```bash
sudo apt update
sudo apt install can-utils python3 python3-venv python3-pip
```

### 2. Create a virtual CAN interface

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

If `vcan0` already exists, do not run the interface creation command again.

### 3. Set up Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the monitor

```bash
python src/can_monitor.py
```

### 5. Generate test traffic

In a separate terminal:

```bash
cansend vcan0 123#1122334455667788
cansend vcan0 321#AABBCCDDEEFF0011
cansend vcan0 456#01020304
```

These are synthetic test frames, not real vehicle signals.

## Roadmap

- [x] Configure Ubuntu research environment
- [x] Create a virtual CAN interface
- [x] Send and receive synthetic CAN frames
- [x] Implement a basic Python CAN traffic monitor
- [ ] Add message counters and traffic statistics
- [ ] Implement configurable anomaly-detection rules
- [ ] Evaluate detection performance against controlled test cases
- [ ] Document findings, limitations, and defensive recommendations

## Safety and Scope

All current experiments use a virtual CAN interface and synthetic messages. This project is for educational and defensive cybersecurity research. Testing on physical vehicles or networks requires explicit authorization and appropriate safety controls.

## Disclaimer

This project is a work in progress. The current monitor displays CAN frames but does not yet decode real vehicle signals or provide a validated intrusion detection system.
