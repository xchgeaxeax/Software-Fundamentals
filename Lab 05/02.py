def is_valid_radius(radius):
    try:
        if radius > 0:
            return True
        else:
            raise Exception
    except Exception:
        return ("ERROR: Invalid radius!")
    except TypeError:
        return ("ERROR: Invalid radius!")


print(is_valid_radius(16))
print(is_valid_radius(-1))
print(is_valid_radius('12'))
print(is_valid_radius([16, 12]))
print(is_valid_radius(2.5))
print(is_valid_radius(0))
