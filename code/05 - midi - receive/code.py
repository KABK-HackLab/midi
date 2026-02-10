
# import libraries 
import board
import time
import usb_midi
import adafruit_midi

# import auxiliar libraries
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

# Configure Midi
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0)

# Loop forever.
while True:
    # Receive and print incoming midi messages
    message = midi.receive()
    if (message!=None):
        print(message)

    # Pause for 1/100th of a second
    time.sleep(0.01)