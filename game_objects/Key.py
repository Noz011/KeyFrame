import mido
from mido import MidiFile, MidiTrack, Message

NOTE_TO_MIDI = {
    'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
}

class Key:
    def __init__(self):
        self.msg = mido.Message('note_on', note = 60)

    def note_to_midi(note):
        note_name = note[:-1]  # Extract the note name (e.g., 'A', 'B', etc.)
        octave = int(note[-1])  # Extract the octave (e.g., '0', '2', etc.)
        return NOTE_TO_MIDI[note_name] + 12 * (octave + 1)
    
    def length_to_ticks(length, ticks_per_beat):
        if length == 1:
            return ticks_per_beat * 4  # Whole note
        elif length == 2:
            return ticks_per_beat * 2  # Half note
        elif length == 4:
            return ticks_per_beat  # Quarter note
        elif length == 8:
            return ticks_per_beat // 2  # Eighth note
        elif length == 16:
            return ticks_per_beat // 4  # Sixteenth note
        
        return ticks_per_beat  # Default to quarter note