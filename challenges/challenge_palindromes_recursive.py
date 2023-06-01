def is_palindrome_recursive(word, low_index, high_index):
    if word == '' or word is None:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
