
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
    # Send a midi note (G sharp 2nd octave with velocity of 120)
    midi.send(NoteOn(44, 120))

    # Send a value of 44 on control change channel 1
    midi.send(ControlChange(1, 44))

    # Pause for 1 of a second
    time.sleep(1)

    # Send a midi note off (G sharp 2nd octave with velocity of 120) and a value of 100 on control change channel 1
    midi.send([NoteOff(44, 120),ControlChange(1, 100)])
    
    # Pause for 1 of a second
    time.sleep(1)
