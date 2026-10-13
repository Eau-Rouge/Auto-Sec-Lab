# Research Findings

## Experiment 1: Virtual CAN Communication

### Objective

Verify that synthetic CAN frames can be transmitted and
received on a virtual CAN interface.

### Procedure

1. Created the vcan0 interface.
2. Started candump to capture frames.
3. Sent test frames using cansend.
4. Confirmed the received IDs and payloads.

### Observations

- Frames were received successfully.
- The monitor displayed arbitration IDs and payload bytes.
- Different payload lengths were observed.

### Limitations

The experiment uses synthetic data. It does not
establish the meaning of real vehicle signals or prove
that any vulnerability exists.
