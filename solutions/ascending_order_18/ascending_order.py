"""this is a solution for the ascending order problem."""


def sort_numbers(num_list):
    """
    Sorts a list of numbers in ascending order.

    Args:
        num_list (list): A list of numbers (integers or floats).

    Returns:
        list: A new list containing the numbers sorted in ascending order.
    """
    return sorted(num_list)


def get_input():
    """
    Takes a comma-separated string input from the user
    converts it to a list of numbers, and sorts them.

    Returns:
        list: A sorted list of numbers.
    """
    user_input = input("Enter a list of numbers separated by commas: ")
    num_list = [int(num.strip()) for num in user_input.split(",")]
    return sort_numbers(num_list)


if __name__ == "__main__":
    sorted_list = get_input()
    print(f"Sorted list: {sorted_list}")
