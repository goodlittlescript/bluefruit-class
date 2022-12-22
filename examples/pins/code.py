"""
Circuit Playground Bluefruit Light-Up Tone Piano

Touch the each of the touchpads around the outside of the board to play a tone for each pad.
Touch A6 and TX at the same time to play the final tone in the octave. A0 is not a touchpad.
"""

from adafruit_circuitplayground import cp
import time

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)
white = (255,255,255)
rainbow = [red, orange, yellow, green, blue, indigo, violet]

# https://learn.adafruit.com/bluefruit-playground-app/tone-generator
data = """
C4  261.63  131.87
 C#4/Db4    277.18  124.47
D4  293.66  117.48
 D#4/Eb4    311.13  110.89
E4  329.63  104.66
F4  349.23  98.79
 F#4/Gb4    369.99  93.24
G4  392.00  88.01
 G#4/Ab4    415.30  83.07
A4  440.00  78.41
 A#4/Bb4    466.16  74.01
B4  493.88  69.85
C5  523.25  65.93
 C#5/Db5    554.37  62.23
D5  587.33  58.74
 D#5/Eb5    622.25  55.44
E5  659.25  52.33
F5  698.46  49.39
 F#5/Gb5    739.99  46.62
G5  783.99  44.01
"""

tones = {}
for line in data.strip().split("\n"):
    tone, freq, wavelength = line.strip().split()
    freq = float(freq)
    wavelength = float(wavelength)
    if "/" in tone:
        x, y = tone.split("/")
        tones[x] = freq
        tones[y] = freq
    else:
        tones[tone] = freq

cp.pixels.brightness = 0.01


pad_attrs = {
    "A4": (0, red, tones["C4"]),
    "A5": (1, orange, tones["D4"]),
    "A6": (3, yellow, tones["E4"]),
    "TX": (4, green, tones["F4"]),
    "A1": (6, blue, tones["G4"]),
    "A2": (8, violet, tones["A4"]),
    "A3": (9, white, tones["B4"]),
}
def light_pad(pad):
    i, color, tone = pad_attrs[pad]
    cp.pixels[i] = color
    # cp.start_tone(tone)

while True:
    if cp.switch:
        continue
    if cp.button_a:
        print("Button A")
        cp.pixels.fill((255, 255, 255))
        cp.start_tone(tones["C4"])
    elif cp.button_b:
        print("Button B")
        cp.pixels.fill((0, 0, 0))
        cp.start_tone(tones["E4"])
    else:
        cp.stop_tone()

    pads = []
    if cp.touch_A1:
        pads.append("A1")
    if cp.touch_A2:
        pads.append("A2")
    if cp.touch_A3:
        pads.append("A3")
    if cp.touch_A4:
        pads.append("A4")
    if cp.touch_A5:
        pads.append("A5")
    if cp.touch_A6:
        pads.append("A6")
    if cp.touch_TX:
        pads.append("TX")

    for pad in pads:
        print(f"Pad {pad}")
        light_pad(pad)

