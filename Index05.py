def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)==5:
        return True
    
    if len(s)>5 and len(s)<5:
        return  False 