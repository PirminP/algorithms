#  from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    if (
        type(first_string) != str
        or type(second_string) != str
        or len(first_string) == 0
        or len(second_string) == 0
    ):
        return (first_string, second_string, False)
