from enum import Enum

PALETTE_HSV_16 = [ # based on caren d ache 16 colors
    {'set': 16, 'hue': 132, 'sat': 6, 'val': 231, 'red': 226, 'green': 231, 'blue': 227, 'hex': '#E2E7E3', 'name': 'soft gray'},
    {'set': 16, 'hue': 195, 'sat': 23, 'val': 45, 'red': 41, 'green': 44, 'blue': 45, 'hex': '#292C2D', 'name': 'charcoal'},
    {'set': 16, 'hue': 198, 'sat': 18, 'val': 142, 'red': 132, 'green': 139, 'blue': 142, 'hex': '#848b8e', 'name': 'cool blue gray'},
    {'set': 16, 'hue': 221, 'sat': 145, 'val': 86, 'red': 37, 'green': 52, 'blue': 86, 'hex': '#253456', 'name': 'steel blue'},
    {'set': 16, 'hue': 219, 'sat': 195, 'val': 131, 'red': 31, 'green': 66, 'blue': 131, 'hex': '#1F4283', 'name': 'deep ocean blue'},
    {'set': 16, 'hue': 200, 'sat': 255, 'val': 195, 'red': 0, 'green': 129, 'blue': 195, 'hex': '#0081C3', 'name': 'sky blue'},
    {'set': 16, 'hue': 356, 'sat': 220, 'val': 221, 'red': 221, 'green': 30, 'blue': 40, 'hex': '#DD1E28', 'name': 'crimson'},
    {'set': 16, 'hue': 34, 'sat': 220, 'val': 239, 'red': 239, 'green': 151, 'blue': 33, 'hex': '#EF9721', 'name': 'sunset orange'},
    {'set': 16, 'hue': 54, 'sat': 255, 'val': 250, 'red': 250, 'green': 228, 'blue': 0, 'hex': '#FAE400', 'name': 'sunny yellow'},
    {'set': 16, 'hue': 32, 'sat': 67, 'val': 84, 'red': 84, 'green': 74, 'blue': 62, 'hex': '#544A3E', 'name': 'earth brown'},
    {'set': 16, 'hue': 149, 'sat': 255, 'val': 146, 'red': 0, 'green': 146, 'blue': 71, 'hex': '#009247', 'name': 'emerald green'},
    {'set': 16, 'hue': 104, 'sat': 142, 'val': 192, 'red': 113, 'green': 192, 'blue': 85, 'hex': '#71C055', 'name': 'olive green'},
    {'set': 16, 'hue': 78, 'sat': 184, 'val': 193, 'red': 149, 'green': 193, 'blue': 54, 'hex': '#95C136', 'name': 'lime green'},
    {'set': 16, 'hue': 332, 'sat': 228, 'val': 236, 'red': 236, 'green': 25, 'blue': 122, 'hex': '#EC197A', 'name': 'rose pink'},
    {'set': 16, 'hue': 332, 'sat': 184, 'val': 232, 'red': 232, 'green': 65, 'blue': 142, 'hex': '#E8418E', 'name': 'magenta'},
    {'set': 16, 'hue': 281, 'sat': 122, 'val': 157, 'red': 134, 'green': 82, 'blue': 157, 'hex': '#86529D', 'name': 'violet'}
]

# Qt returns a hue value of -1 for achromatic colors.
GRAY = {'hue': -1, 'sat': 0, 'val': 200, 'red': 200, 'green': 200, 'blue': 200, 'name': 'gray'}

class LockState(Enum):
    OPEN = 1
    CLOSE = 2
    LOCKED = 3