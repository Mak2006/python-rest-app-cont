# This is the would be 2nd microservice that actully forms the service layer.
def sum(arg):
    result = 0
    for val in arg:
        result += int(val)
    return result