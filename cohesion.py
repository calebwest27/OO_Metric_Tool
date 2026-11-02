
def calculate_cohesion(class_info):
    """
    Calculates Tight Class Cohesion (TCC).
    Two methods are connected if they share
    at least one instance attribute.
    """

    methods = class_info["methods"]
    attributes = class_info["method_attributes"]

    total_pairs = len(methods) * (len(methods) - 1) // 2

    if total_pairs == 0:
        return None

    connected_pairs = 0

    for i in range(len(methods)):
        for j in range(i + 1, len(methods)):

            method1 = methods[i]
            method2 = methods[j]

            if attributes[method1] & attributes[method2]:
                connected_pairs += 1

    return round(connected_pairs / total_pairs, 2)
