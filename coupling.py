
def calculate_coupling(class_info):
    """
    Calculates Coupling Between Objects (CBO).
    Counts the number of distinct external classes
    referenced by a class.
    """

    return len(class_info["dependencies"])
