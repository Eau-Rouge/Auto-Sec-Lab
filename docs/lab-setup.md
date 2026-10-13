# Lab Setup

## Environment

- Ubuntu Linux running in Oracle VirtualBox
- Linux SocketCAN
- Virtual CAN interface: vcan0
- Python 3 and python-can
- can-utils

## Configure the Virtual CAN Interface

Load the virtual CAN kernel module:

    sudo modprobe vcan

Create and enable the interface:

    sudo ip link add dev vcan0 type vcan
    sudo ip link set up vcan0

Verify the interface:

    ip link show vcan0

## Generate Synthetic Traffic

Listen for messages:

    candump vcan0

Send a test frame in another terminal:

    cansend vcan0 123#1122334455667788

## Notes

All tests documented here use synthetic traffic on a
virtual interface. No physical vehicle is connected.
