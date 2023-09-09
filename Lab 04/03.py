import math
def get_volume(radius, height):
    if radius<0 and height<0:
        return "Invalid input"
    elif radius<0:
        return "Invalid input"
    elif height<0:
        return    "Invalid input"
    elif radius==0:
        return "Not a cylinder"
    elif height==0:
        return    "Not a cylinder"
    return round(radius*radius*math.pi*height)