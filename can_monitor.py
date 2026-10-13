import can

from datetime import datetime

bus = can.Bus(
	interface="socketcan",
	channel="vcan0"
)

print("AUTOMOTIVE CAN MONITOR")
print("Listening on vcan0... Press Ctrl+C to stop.\n")

try:
	while True:
		message = bus.recv(timeout=1.0)

		if message is None:
			continue

		timestamp = datetime.now().strftime("%H:%M:%S")
		
		print(
			f"[{timestamp}] "
			f"ID=0x{message.arbitration_id:03X} "
			f"DLC={message.dlc} "
			f"DATA={message.data.hex(' ').upper()}"
		)

except KeyboardInterupt:
	print("\nMonitor stopped.")

finally:
	bus.shutdown()





B
B
B
B
A
A
A
B
B
B
 
