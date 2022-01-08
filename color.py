import math

baseVals = {"on": True, "effect": "none", "sat": 254, "bri": 254}


def setDict(d): return dict(baseVals, **d)


def hue(hue): return setDict({"hue": hue})


def hsb(h, s, b): return setDict({"hue": h, "sat": s, "bri": b})
def xy(x, y): return setDict({"xy": [x, y]})


OFF = setDict({"on": False})

RAINBOW = setDict({"effect": "colorloop"})

COLD = setDict({"hue": 39396, "sat": 13})
WARM = setDict({"hue": 8592, "sat": 121})

RED = hue(0)
ORANGE = hue(5461)
YELLOW = hue(10922)
LIME = hue(16384)
GREEN = hue(21845)
CYAN = hue(32768)
BLUE = hue(43690)
VIOLET = hue(49152)
PURPLE = hue(51882)
MAGENTA = hue(54613)
PINK = hsb(0, 150, 254)

colorChoices = {
    "Off": OFF,
    "Rainbow": RAINBOW,
    "Cold white": COLD,
    "Warm white": WARM,
    "Red": RED,
    "Orange": ORANGE,
    "Yellow": YELLOW,
    "Lime": LIME,
    "Green": GREEN,
    "Cyan": CYAN,
    "Blue": BLUE,
    "Violet": VIOLET,
    "Purple": PURPLE,
    "Magenta": MAGENTA,
    "Pink": PINK
}

############################################################################
# snippet from https://gist.github.com/error454/6b94c46d1f7512ffe5ee
# This is based on original code from http://stackoverflow.com/a/22649803


def __EnhanceColor(normalized):
    if normalized > 0.04045:
        return math.pow((normalized + 0.055) / (1.0 + 0.055), 2.4)
    else:
        return normalized / 12.92


def __RGBtoXY(r, g, b):
    rNorm = r / 255.0
    gNorm = g / 255.0
    bNorm = b / 255.0

    rFinal = __EnhanceColor(rNorm)
    gFinal = __EnhanceColor(gNorm)
    bFinal = __EnhanceColor(bNorm)

    X = rFinal * 0.649926 + gFinal * 0.103455 + bFinal * 0.197109
    Y = rFinal * 0.234327 + gFinal * 0.743075 + bFinal * 0.022598
    Z = rFinal * 0.000000 + gFinal * 0.053077 + bFinal * 1.035763

    if X + Y + Z == 0:
        return (0, 0)
    else:
        xFinal = X / (X + Y + Z)
        yFinal = Y / (X + Y + Z)

        return (xFinal, yFinal)
############################################################################


def rgb(r, g, b):
    x, y = __RGBtoXY(r, g, b)
    return xy(x, y)
