"""
Relay & MIDI Controller (Example Project)
------------------------------------------

This script runs on a Raspberry Pi Pico using CircuitPython to demonstrate 
how to combine a physical input, a relay output, and USB MIDI communication.

Function:
- Detects when a connected switch or sensor is triggered
- Activates a relay for 30 seconds to control external hardware (e.g., lights)
- Simultaneously sends a MIDI NoteOn message (note 60) via USB to a host computer
- After 30 seconds, sends a second MIDI NoteOn (note 61) to indicate reset/end of sequence

Hardware (example configuration):
- Switch connected to GPIO 17 (with pull-down resistor)
- Relay connected to GPIO 28 (driving external hardware)
- USB connection to a host computer with MIDI-compatible software


Author: Austin Zercher
Date: May 8th, 2025

Dependencies:
- CircuitPython
- Adafruit MIDI library
- USB MIDI enabled
"""

import time
import board
import digitalio

import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

#---------------Switch & Relay Init---------------
switch = digitalio.DigitalInOut(board.GP17)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

relay = digitalio.DigitalInOut(board.GP28)
relay.direction = digitalio.Direction.OUTPUT

#---------------MIDI Init---------------
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0], in_channel=0,
    midi_out=usb_midi.ports[1], out_channel=0
)

#---------------State Variables---------------
is_open = False
off_signal_sent = False
trigger_time = None

#---------------Main Loop---------------
while True:
    now = time.monotonic()

    # When switch is triggered and relay is not active
    if not switch.value and not is_open:
        relay.value = True
        print("Trigger activated...")
        midi.send(NoteOn(60, 127))  # Start signal sent via MIDI
        trigger_time = now
        is_open = True
        off_signal_sent = False
        time.sleep(0.1)  

    # Send off signal and turn off relay after 30 seconds
    if is_open and not off_signal_sent and trigger_time is not None:
        if now - trigger_time >= 30:
            midi.send(NoteOn(61, 127))  # End/reset signal sent via MIDI
            relay.value = False
            print("Sequence complete...")
            print("Relay reset...")
            off_signal_sent = True

    # Reset if switch is released
    if switch.value:
        is_open = False

    time.sleep(0.01)