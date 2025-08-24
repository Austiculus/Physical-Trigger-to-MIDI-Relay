# Physical Trigger to MIDI & Relay Controller

This repository contains a generic CircuitPython project demonstrating how to combine physical input detection, relay control, and USB MIDI messaging on a Raspberry Pi Pico.

It is intended as an educational and demonstration system for interactive hardware-to-MIDI workflows.

## Features
- Detects a physical trigger (e.g., switch press)
- Activates a relay for a fixed duration
- Sends MIDI NoteOn messages over USB to indicate start and end of the sequence
- Automatic reset logic for repeated interactions

## Hardware (Example Setup)
- **Switch** connected to a GPIO pin with a pull-down resistor
- **Relay** connected to a GPIO pin, controlling external hardware
- **USB connection** to a host computer running MIDI-compatible software

> Note: The setup and code are presented in a generic manner and do not include proprietary exhibit-specific details.

## Dependencies
- CircuitPython
- `adafruit_midi` library
- USB MIDI support enabled

## Usage
1. Flash the Raspberry Pi Pico with `relay_midi_controller.py`.
2. Connect a physical input (switch) and relay according to the GPIO assignments in the code.
3. Connect the Pico via USB to a computer or MIDI-capable device.
4. Trigger the switch to activate the relay and send MIDI messages.
5. After the fixed duration, the relay resets automatically and a second MIDI signal is sent.

## Notes
- The code logic is fully generic and safe for public sharing.
- Can be adapted for any project requiring timed relay activation and MIDI output from a physical input.
