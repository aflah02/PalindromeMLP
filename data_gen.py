import string
import numpy as np

all_chars = string.ascii_uppercase

def generate_palindromic_strings(length, count):
    """
    Generate palindromic strings of length `length`.
    """
    assert length % 2 == 1, "length must be odd"
    assert length >= 3, "length must be at least 3"
    strings = []
    while len(strings) < count:
        s = ""
        for j in range(length // 2):
            s += np.random.choice(list(all_chars))
        s += np.random.choice(list(all_chars))
        s += s[:length // 2][::-1]
        if s not in strings:
            strings.append(s)
    return strings

def generate_nonpalindromic_strings(length, count):
    """
    Generate non-palindromic strings of length `length`.
    """
    assert length % 2 == 1, "length must be odd"
    assert length >= 3, "length must be at least 3"
    strings = []
    while len(strings) < count:
        s = ""
        for j in range(length):
            s += np.random.choice(list(all_chars))
        if s not in strings:
            strings.append(s)
    return strings

def generate_palindromes_off_by_one_swap(length, count, preexisting_strings):
    """
    Generate palindromes of length `length` that are off by one character.
    """
    assert length % 2 == 1, "length must be odd"
    assert length >= 3, "length must be at least 3"
    strings = []
    while len(strings) < count:
        s = ""
        for j in range(length // 2):
            s += np.random.choice(list(all_chars))
        s += np.random.choice(list(all_chars))
        s += s[:length // 2][::-1]
        i = np.random.randint(length)
        j = np.random.randint(length)
        tries = 0
        while s[i] == s[j] and tries < 10:
            tries += 1
            j = np.random.randint(length)
        if i > j:
            i, j = j, i
        s_new = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        if s_new not in strings and s_new not in preexisting_strings:
            strings.append(s_new)
    return strings

def generate_palindromes_off_by_one_random_replacement(length, count, preexisting_strings):
    """
    Generate palindromes of length `length` that are off by one character.
    """
    assert length % 2 == 1, "length must be odd"
    assert length >= 3, "length must be at least 3"
    strings = []
    while len(strings) < count:
        s = ""
        for j in range(length // 2):
            s += np.random.choice(list(all_chars))
        s += np.random.choice(list(all_chars))
        s += s[:length // 2][::-1]
        # i should not be the middle character
        i = np.random.choice([x for x in range(length) if x != length // 2])
        char_at_i = s[i]
        tries = 0
        randomly_sampled_char = np.random.choice(list(all_chars))
        while char_at_i == randomly_sampled_char and tries < 10:
            tries += 1
            randomly_sampled_char = np.random.choice(list(all_chars))
        s = s[:i] + randomly_sampled_char + s[i+1:]
        if s not in strings and s not in preexisting_strings:
            strings.append(s)
    return strings

if __name__ == "__main__":
    SEQ_LENGTH = 9
    palindromic_strings = generate_palindromic_strings(SEQ_LENGTH, 33000)
    nonpalindromic_strings = generate_nonpalindromic_strings(SEQ_LENGTH, 11000)
    palindromic_strings_off_by_one_swap = generate_palindromes_off_by_one_swap(SEQ_LENGTH, 11000, nonpalindromic_strings)
    palindromic_strings_off_by_one_random_replacement = generate_palindromes_off_by_one_random_replacement(SEQ_LENGTH, 11000, nonpalindromic_strings + palindromic_strings_off_by_one_swap)
    # Interesection between any two sets should be empty
    assert len(set(palindromic_strings).intersection(set(nonpalindromic_strings))) == 0
    assert len(set(palindromic_strings).intersection(set(palindromic_strings_off_by_one_swap))) == 0
    assert len(set(palindromic_strings).intersection(set(palindromic_strings_off_by_one_random_replacement))) == 0
    assert len(set(nonpalindromic_strings).intersection(set(palindromic_strings_off_by_one_random_replacement))) == 0
    assert len(set(nonpalindromic_strings).intersection(set(palindromic_strings_off_by_one_swap))) == 0
    assert len(set(palindromic_strings_off_by_one_swap).intersection(set(palindromic_strings_off_by_one_random_replacement))) == 0
    # Write to file
    data_folder = "data/"
    with open(data_folder + "palindromic_strings.txt", "w") as f:
        for s in palindromic_strings:
            f.write(s + "\n")

    with open(data_folder + "nonpalindromic_strings.txt", "w") as f:
        for s in nonpalindromic_strings:
            f.write(s + "\n")

    with open(data_folder + "palindromic_strings_off_by_one_swap.txt", "w") as f:
        for s in palindromic_strings_off_by_one_swap:
            f.write(s + "\n")

    with open(data_folder + "palindromic_strings_off_by_one_random_replacement.txt", "w") as f:
        for s in palindromic_strings_off_by_one_random_replacement:
            f.write(s + "\n")


