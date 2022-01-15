#25 - More Practice

# How to run
# > python3
# >>> import ex25       NO EXTENSION
# >>> sentence = "Hello World."
# >>> words = ex25.break_words(sentence)
# >>> words

# Triple Quote is documentation comment

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# Pre-defined sorted
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# Pre-defined pop(0) is first
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

# Pre-defined pop(-1) is last
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


