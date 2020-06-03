# This is the would be 2nd microservice that actully forms the service layer.

NULL_ERR_MSG = "Cannot add null data"
EMPTY_ERR_MSG = "Cannot add empty list"
STRING_ERR_MSG = "Cannot add str data"


def sum(arg):
    """Method returns the sum elements within arg. 

    This service takes a list of items as arg, it checks if the items are integers and if so adds them
    and returns the result.

    Args:
        arg (list): list Of elements, there is no restriction on the type of element.

    Returns:
        int: result of addition of all the elements within arg.
    	str: reason why it could not perform addition.
    """
   
    # We now check the input to complete the unit tests
    if None in arg:  # if there is no input data
        return NULL_ERR_MSG

    if len(arg) == 0: # if there is no data
        return EMPTY_ERR_MSG

    result = 0
    try:
        for val in arg:
            result += int(val)
    except:
        # Cannot cast args to int
        # message is logged from server.py
        result = STRING_ERR_MSG

    # All went fine and we return the result
    return result