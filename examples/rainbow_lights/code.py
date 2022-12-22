"""
Circuit Playground Bluefruit Light-Up Tone Piano

Touch the each of the touchpads around the outside of the board to play a tone for each pad.
Touch A6 and TX at the same time to play the final tone in the octave. A0 is not a touchpad.
"""

from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.02

# https://bsouthga.dev/posts/color-gradients-with-python
def hex_to_RGB(hex):
  ''' "#FFFFFF" -> [255,255,255] '''
  # Pass 16 to the integer function for change of base
  return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def RGB_to_hex(RGB):
  ''' [255,255,255] -> "#FFFFFF" '''
  # Components need to be integers for hex to make sense
  RGB = [int(x) for x in RGB]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])

def color_dict(gradient):
  ''' Takes in a list of RGB sub-lists and returns dictionary of
    colors in RGB and hex form for use in a graphing function
    defined later on '''
  return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
      "r":[RGB[0] for RGB in gradient],
      "g":[RGB[1] for RGB in gradient],
      "b":[RGB[2] for RGB in gradient]}


# Value cache
fact_cache = {}
def fact(n):
  ''' Memoized factorial function '''
  try:
    return fact_cache[n]
  except(KeyError):
    if n == 1 or n == 0:
      result = 1
    else:
      result = n*fact(n-1)
    fact_cache[n] = result
    return result


def bernstein(t,n,i):
  ''' Bernstein coefficient '''
  binom = fact(n)/float(fact(i)*fact(n - i))
  return binom*((1-t)**(n-i))*(t**i)


def bezier_gradient(colors, n_out=100):
  ''' Returns a "bezier gradient" dictionary
      using a given list of colors as control
      points. Dictionary also contains control
      colors/points. '''
  # RGB vectors for each color, use as control points
  RGB_list = [hex_to_RGB(color) for color in colors]
  n = len(RGB_list) - 1
  def bezier_interp(t):
    ''' Define an interpolation function
        for this specific curve'''
    # List of all summands
    summands = [
      list(map(lambda x: int(bernstein(t,n,i)*x), c))
      for i, c in enumerate(RGB_list)
    ]
    # Output color
    out = [0,0,0]
    # Add components of each summand together
    for vector in summands:
      for c in range(3):
        out[c] += vector[c]
    return out
  gradient = [
    bezier_interp(float(t)/(n_out-1))
    for t in range(n_out)
  ]
  # Return all points requested for gradient
  return {
    "gradient": color_dict(gradient),
    "control": color_dict(RGB_list)
  }

def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)

controls = [ RGB_to_hex(rgb) for rgb in [red, orange, yellow, green, blue, indigo, violet]]

N=80
n=0
t=0.1
gradient = bezier_gradient(controls, n_out=N)['gradient']
colors = cycle(list(zip(gradient['r'], gradient['g'], gradient['b'])))
while True:
    if cp.switch:
        t = 0.1
        continue

    if cp.button_a:
        t += 0.01
    elif cp.button_b:
        t -= 0.01
        if t < 0:
            t = 0

    color = next(colors)
    print(f"step: {n} ({color})")
    cp.pixels[n] = color
    time.sleep(t)
    n+=1
    if n >= 10:
        n = 0
