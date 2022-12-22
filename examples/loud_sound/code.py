from adafruit_circuitplayground import cp

while True:
    if cp.switch:
        print("Slide switch off!")
        cp.pixels.fill((0, 0, 0))
        cp.stop_tone()
        continue

    if cp.button_a:
        print("Button A pressed!")
        cp.pixels.fill((15, 0, 0))
        cp.start_tone(262)
    elif cp.button_b:
        print("Button B pressed!")
        cp.pixels.fill((0, 0, 15))
        cp.start_tone(330)
    else:
        if cp.loud_sound(sound_threshold=300):
            cp.pixels.fill((0, 15, 0))
        else:
            cp.pixels.fill((0, 0, 0))
        cp.stop_tone()
        time.sleep(0.5)
