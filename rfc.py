
def calculate_rfc(class_info):
    """
    Calculates Response for a Class (RFC).

    RFC = Number of class methods +
          distinct methods called by those methods.

    Each method is counted only once.
    """

    class_methods = set(class_info["methods"])
    called_methods = set(class_info["response_methods"])

    response_set = class_methods.union(called_methods)

    return len(response_set)
