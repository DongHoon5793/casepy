"""
Utility functions for casepy.
"""


def list_to_bin_dict(in_list: list) -> dict:
    """
    Convert a list to a bin list.

    Args:
        in_list (list): The list to convert.

    Returns:
        dict: The bin dictionary.
    """
    result_dict = {}
    element_type_list = []
    for i in in_list:
        if i not in element_type_list:
            element_type_list.append(i)
            result_dict[i] = 1
        else:
            result_dict[i] += 1

    result_list = list(result_dict.values())
    # return result_list, element_type_list
    return result_dict
