import itertools


def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif first(word) == last(word) and is_palindrome(middle(word)):
        return True
    else:
        return False


def is_divisible(a, b):
    return a % b == 0


def is_power(a, b):
    if a == 0 or a == 1:
        return True
    elif is_divisible(a, b) and is_power(a / b, b):
        return True
    else:
        return False


def square_root(number, estimation):
    while True:
        new_estimate = (estimation + number / estimation) / 2
        if abs(new_estimate - estimation) < 0.00001:
            break
        estimation = new_estimate
    return new_estimate


def is_palindrome_string(word):
    return word == word[::-1]


def print_only_as_long_as(length):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > length:
            print(word)


def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True


def print_only_if(word_function, arguments):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if word_function(word, arguments):
            print(word)


def avoids(word, letters):
    for letter in word:
        if letter in letters:
            return False
    return True


def print_only_if_avoids(letters):
    print_only_if(avoids, letters)


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


def print_only_if_uses(letters):
    print_only_if(uses_only, letters)


def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True


def print_only_if_uses_all(letters):
    print_only_if(uses_all, letters)


def is_abecedarian(word):
    for index in range(0, len(word)):
        if index + 1 < len(word) and word[index] > word[index + 1]:
            return False
    return True


def print_only_if_abecedarian():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)


def get_count_for_combination(fin, combination):
    count = 0
    letters = ''.join(combination)
    for line in fin:
        word = line.strip()
        if avoids(word, letters):
            count = count + 1
    return count


def find_forbidden_letters():
    fin = open('words.txt')
    letters = "abcdefghijklmnopqrstuvwxyz"
    minimum_word_count = 113809
    best_combination = ""
    for current_five in itertools.combinations(letters, 5):
        count = get_count_for_combination(fin, current_five)
        fin.seek(0)
        if minimum_word_count > count:
            minimum_word_count = count
            best_combination = current_five
    print("Best combination is", best_combination, "printing just", minimum_word_count, "words")
