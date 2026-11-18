import pytest
import util

VALID_WORD_HINT = ("This word is valid (it is a string, and every character is a letter), so it should not fail an "
                   "assert statement. Check the conditions in your assert statements.")
NEXT_LETTER_HINT = ("If you check the letter after a 'y', remember that the last letter of a word has no letter "
                    "after it, so check the index before using it.")
TYPE_HINT = ("Check the type of the argument with an assert statement (e.g. `assert type(word) == str`) *before* "
             "looping over it or calling string methods on it.")
CASE_HINT = "Convert the word to lower case (e.g. with .lower()) before counting vowels."
ENGLISH_LETTERS_HINT = ("isalpha() returns True for letters from other alphabets (like é), so it can't be used to "
                        "check for English letters. Instead, check whether each character is `in` a string of the "
                        "letters a to z.")


def num_vowels():
  """Return the num_vowels function defined in src/q3.py"""
  return util.get_student_function("q3", "num_vowels", "Part 3")


def check(words_and_counts, explanation, hint=None):
  """Check num_vowels for each (word, expected count) pair"""
  for word, expected in words_and_counts:
    actual = util.call(num_vowels(), word, hints={AssertionError: VALID_WORD_HINT, IndexError: NEXT_LETTER_HINT})
    util.check_returned(f"num_vowels({word!r})", actual, expected,
                        f"'{word}' has {expected} vowel{'s' if expected != 1 else ''}. {explanation}" +
                        (f"\nHINT: {hint}" if hint else ""))


def test_num_vowels_is_defined():
  num_vowels()


def test_num_vowels_takes_one_parameter():
  util.check_parameter_count(num_vowels(), 1, "the word to count the vowels in")


def test_num_vowels_has_a_docstring():
  num_vowels()
  util.check_has_docstring("q3", "num_vowels")


def test_num_vowels_returns_instead_of_printing(capsys):
  util.check_returns_instead_of_printing(capsys, num_vowels(), "hello")


# Words with a, e, i, o and u (and no y)
def test_words_with_no_vowels():
  check([("crwth", 0), ("b", 0)], "None of its letters are vowels.")


def test_words_with_vowels():
  check([("red", 1), ("reed", 2), ("read", 2), ("education", 5), ("sequoia", 5), ("aeiou", 5)],
        "Every a, e, i, o and u is a vowel.")


def test_num_vowels_is_case_insensitive():
  check([("Aa", 2), ("EDUCATION", 5), ("SeQuOiA", 5)], "num_vowels must not be case sensitive.", CASE_HINT)


def test_empty_string_has_no_vowels():
  check([("", 0)], "The empty string has no characters at all (so none of them are non-letters), which makes it valid.")


# Words with y (see the rules for y in Part 3 of the README)
def test_y_is_a_vowel_when_it_is_the_only_vowel():
  check([("why", 1), ("lynx", 1), ("ympt", 1), ("wryly", 2), ("syzygy", 3)],
        "When y is the only vowel in a word, every y is a vowel.")


def test_y_at_the_end_is_a_vowel():
  check([("ready", 3), ("boy", 2), ("aeiouy", 6)],
        "A y that is not followed by a, e, i, o or u (including a y at the end of a word) is a vowel.")


def test_y_followed_by_a_vowel_is_a_consonant():
  check([("yo", 1), ("yak", 1), ("yellow", 2), ("beyond", 2), ("canyon", 2), ("kayak", 2), ("yoyo", 2)],
        "When the word has other vowels, a y followed by a, e, i, o or u is a consonant.")


def test_y_not_followed_by_a_vowel_is_a_vowel():
  check([("ytrium", 3), ("psychology", 4), ("yearly", 3), ("yummy", 2), ("siyyad", 3), ("aeiyyou", 6)],
        "When the word has other vowels, a y followed by a, e, i, o or u is a consonant, and any other y "
        "(including one followed by another y) is a vowel.")


def test_y_rules_are_case_insensitive():
  check([("WhY", 1), ("SYZYGY", 3), ("YELLOW", 2), ("yEllow", 2), ("KaYAk", 2), ("PSYCHOLOGY", 4)],
        "num_vowels must not be case sensitive, and that includes the rules for y.", CASE_HINT)


# Invalid arguments must fail an assert statement
def test_argument_that_is_not_a_string_fails_assert():
  for value in [1, 3.5, None]:
    util.check_raises_assertion_error(num_vowels(), (value,), "the argument is not a string",
                                      hints={TypeError: TYPE_HINT, AttributeError: TYPE_HINT})


def test_list_of_letters_fails_assert():
  util.check_raises_assertion_error(
      num_vowels(), (["a", "b"],), "the argument is a list, not a string", hints={TypeError: TYPE_HINT,
                                                                                AttributeError: TYPE_HINT},
      returned_hint="A list of letters passes the check that each item is a letter, so you must also check that the "
      "argument is a string (e.g. `assert type(word) == str`).")


def test_word_with_characters_that_are_not_letters_fails_assert():
  for word in ["abc!def", "abc1", "don't", "hello world", " "]:
    util.check_raises_assertion_error(num_vowels(), (word,), f"{word!r} contains a character that is not a letter")


def test_word_with_letters_that_are_not_english_fails_assert():
  for word in ["café", "naïve"]:
    util.check_raises_assertion_error(
        num_vowels(), (word,), f"{word!r} contains a letter that is not one of the 26 letters of the English alphabet",
        returned_hint=ENGLISH_LETTERS_HINT)


# How the code is written
def test_num_vowels_uses_a_loop():
  definition = util.find_function_def("q3", "num_vowels")
  assert definition is not None, "Define a function named num_vowels in src/q3.py, as described in Part 3 of the README."
  assert util.find_for_loops(definition) + util.find_while_loops(definition) != [], (
      "num_vowels must use a loop to check that each character of the word is a letter, as described in Part 3 of "
      "the README.")


def test_q3_has_no_print_calls():
  lines = util.find_print_calls("q3")
  assert lines == [], (
      f"src/q3.py calls print() on line(s) {', '.join(map(str, lines))}. num_vowels should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py, or inside an `if __name__ == \"__main__\":` "
      f"block at the end of the file.)")
