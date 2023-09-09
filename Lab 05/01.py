def is_valid_score(score):
    try:
        if score < 0 or score > 100:
            raise Exception
        else:
            return True

    except Exception as an_error:
        return "ERROR: Invalid score!"

print(is_valid_score(85.5))
print(is_valid_score(-1))
print(is_valid_score([16, 12]))
print(is_valid_score(123))
print(is_valid_score(0))
print(is_valid_score(100))
print(is_valid_score('sixteen'))