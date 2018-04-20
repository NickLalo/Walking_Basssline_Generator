import sys
sys.path.append('C:\midiutil')

from MidiFile import *
import random

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 0.5    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI_1 = MIDIFile(1)  # One track
MyMIDI_1.addTempo(track, time, tempo)

# lowest noted is 36 C3

# 36 C
# 37 C#
# 38 D
# 39 D#
# 40 E
# 41 F
# 42 F#
# 43 G
# 44 G#
# 45 A
# 46 A#
# 47 B
# 48 C
# 49 C#
# 50 D
# 51 D#
# 52 E
# 53 F
# 54 F#
# 55 G
# 56 G#
# 57 A
# 58 A#
# 59 B
# 60 C

# chord pattern and length
# chord progression is 2,5,1,6 and each chord is held for 8 beats
chord_pattern = [2,8,  5,8,  1,8,  6,8]
song_key = "G"


def walk_bass(song_key, chord_pattern):
    print("song_key is: ", song_key)
    print("midi note is: ", key_note[song_key])
    start_note = main_note(-1)
    return

# main_note determines the main notes being walked towards
# if the tonic of the chord is already featured, exclude it
def main_note(seed):
    
    if seed == -1:
        note = random.randint(0,3)
        #0 = 1
        #1 = 3
        #2 = 5
        #3 = 7
        # need logic to determine if note is higher or lower than start note
    else:
        note = random.randint(1,3)



# key note is determined from key
# and gives the associated midi value
key_note = {
    "B": 35,
    "C": 36,
    "C#": 37,
    "Db": 37,
    "D": 38,
    "D#": 39,
    "Eb": 39,
    "E": 40,
    "F": 41,
    "F#": 42,
    "Gb": 42,
    "G": 43,
    "G#": 44,
    "Ab": 44,
    "A": 45,
    "A#": 46,
    "Bb": 46,
    "B": 47, }

def bass_note_of_chord(note):
    if note == 1:
        return 0
    elif note == 2:
        return 2
    elif note == 3:
        return 4
    elif note == 4:
        return 5
    elif note == 5:
        return 7
    elif note == 6:
        return 9
    elif note == 7:
        return 11

def chord_build(note):
        if chord_tonality(note) == "Maj":
            return "0, 4, 3, 7"
        elif chord_tonality(note) == "Min":
            return "0, 3, 4, 7"
        elif chord_tonality(note) == "Dim":
            return "0, 3, 3, 7"

def chord_tonality(note):
    if note == 1 or note == 4 or note == 5:
        return "Maj"
    elif note == 2 or note == 3 or note == 6:
        return "Min"
    elif note == 7:
        return "Dim"

def main():
    bass_notes = walk_bass(song_key, chord_pattern)

##    
##    x = 0
##    #add notes from first
##    for i, pitch in enumerate(bass_notes):
##        MyMIDI_1.addNote(track, channel, pitch, time + x, duration, volume)
##        x += 0.5
##
##        
##    #export file
##    with open("bass_notes.mid", "wb") as output_file:
##        MyMIDI_1.writeFile(output_file)
    
    return

main()

##default = [60, 62, 64, 65, 67, 69, 71, 72]
##first = [36, 64, 65, 60]
##second = [64, 67, 69, 64]
##third = [67, 71, 72, 67]
##
##x = 0
###add notes from list
##for i, pitch in enumerate(first):
##    MyMIDI_1.addNote(track, channel, pitch, time + x, duration, volume)
##    x += 0.5
##
##x = 0
###add notes from list
##for i, pitch in enumerate(second):
##    MyMIDI_1.addNote(track, channel, pitch, time + x, duration, volume)
##    x += 0.5
##
##x = 0
###add notes from first
##for i, pitch in enumerate(third):
##    MyMIDI_1.addNote(track, channel, pitch, time + x, duration, volume)
##    x += 0.5
##
##        
###export file
##with open("major-scale_new.mid", "wb") as output_file:
##    MyMIDI_1.writeFile(output_file)
##







