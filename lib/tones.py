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