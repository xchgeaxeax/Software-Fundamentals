import math
def get_volume(radius, height):
    try:


        if radius ==0 or height == 0:
            raise Exception('Not a cylinder')

        if radius < 0 and height < 0:
            raise Exception('Height and radius must be positive')

        if radius < 0:
            raise Exception('Radius must be positive')

        if height < 0:
            raise Exception('Height must be positive')


        volume = round(math.pi * radius ** 2 * height)
        return volume

    except TypeError:
        return "ERROR: Invalid input."
    except Exception  as result :
        return "ERROR: {}.".format(result)


print(get_volume(10, 2))
print(get_volume(-10, 2))
print(get_volume(10, -2))
print(get_volume(-10, -2))
print(get_volume(10, 0))
print(get_volume('ten', 2))