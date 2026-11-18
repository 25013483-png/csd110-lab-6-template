import pytest
import util
import util_lab_6 as lab6

DUPLICATE_HINT = (
    "Your function seems to count a letter once for each time it appears in the second string. Instead, check "
    "each character of the *first* string once, and count it if it is `in` the second string.")
CASE_HINT = "Convert both strings to the same case (e.g. with .lower()) before comparing their characters."


def num_letters():
  """Return the num_letters function defined in src/q1.py"""
  return util.get_student_function("q1", "num_letters", "Part 1")


def check(text, letters, expected, explanation, hint=None):
  lab6.check_num_letters(num_letters(), text, letters, expected, explanation, hint)


def test_num_letters_is_defined():
  num_letters()


def test_num_letters_takes_two_parameters():
  util.check_parameter_count(num_letters(), 2, "the string to search, and the letters to count")


def test_num_letters_has_a_docstring():
  num_letters()
  util.check_has_docstring("q1", "num_letters")


def test_num_letters_returns_instead_of_printing(capsys):
  util.check_returns_instead_of_printing(capsys, num_letters(), "mississippi", "s")


# Counting one letter
def test_letter_that_appears_once():
  check("something", "s", 1, "There is 1 's' in 'something'.")
  check("abc", "b", 1, "There is 1 'b' in 'abc'.")
  check("a", "a", 1, "There is 1 'a' in 'a'.")


def test_letter_that_appears_several_times():
  check("mississippi", "s", 4, "There are 4 's' letters in 'mississippi'.")
  check("ccc", "c", 3, "There are 3 'c' letters in 'ccc'.")
  check("badacdad", "d", 3, "There are 3 'd' letters in 'badacdad'.")


def test_letter_that_does_not_appear():
  check("hello", "z", 0, "There are no 'z' letters in 'hello'.")


# Counting several letters
def test_several_letters():
  check("mississippi", "si", 8, "There are 4 's' letters plus 4 'i' letters in 'mississippi'.")
  check("abc", "abc", 3, "All 3 letters of 'abc' are one of 'a', 'b' or 'c'.")
  check("a", "abc", 1, "There is 1 letter in 'a', and it is one of 'a', 'b' or 'c'.")
  check("adbecf", "abc", 3, "'a', 'b' and 'c' each appear once in 'adbecf'.")
  check("zysxhxyuayz", "zyxw", 7, "'zysxhxyuayz' has 2 z's, 3 y's, 2 x's and no w's.")


# Empty strings
def test_empty_letters_string():
  check("mississippi", "", 0, "There are no letters to count, so the count is 0.")


def test_empty_string_to_search():
  check("", "s", 0, "There is nothing to search, so the count is 0.")
  check("", "", 0, "There is nothing to search, so the count is 0.")


# Repeated letters in the second string must not add to the count
def test_repeated_letters_are_not_double_counted():
  check("mississippi", "ss", 4, "There are 4 's' letters in 'mississippi'. Repeating 's' in the second string "
        "must NOT add to the count.", DUPLICATE_HINT)
  check("abc", "bbbbbbbb", 1, "There is only 1 'b' in 'abc'.", DUPLICATE_HINT)
  check("aaa", "aaa", 3, "There are 3 'a' letters in 'aaa'.", DUPLICATE_HINT)


# Upper and lower case
def test_num_letters_is_case_insensitive():
  check("miSsiSsippi", "S", 4, "num_letters must not be case sensitive, so 's' and 'S' are both counted.\n"
        f"HINT: {CASE_HINT}")
  check("MISSISSIPPI", "s", 4, "num_letters must not be case sensitive, so 'S' is counted when looking for 's'.\n"
        f"HINT: {CASE_HINT}")
  check("mississippi", "S", 4, "num_letters must not be case sensitive, so 's' is counted when looking for 'S'.\n"
        f"HINT: {CASE_HINT}")
  check("BdS", "sDb", 3, f"num_letters must not be case sensitive.\nHINT: {CASE_HINT}")


def test_letters_that_differ_only_in_case_are_not_double_counted():
  check("mississippi", "sS", 4, "There are 4 's' letters in 'mississippi'. Since case doesn't matter, 's' and 'S' "
        "are the same letter, so asking for both must NOT add to the count.", DUPLICATE_HINT)
  check("Banana", "aA", 3, "There are 3 'a' letters in 'Banana'.", DUPLICATE_HINT)


# Characters that are not letters
def test_characters_that_are_not_letters():
  check("Hello, world!", " !", 2, "'Hello, world!' has 1 space and 1 '!'.")
  check("1 + 1 = 2", "1", 2, "'1 + 1 = 2' has 2 '1' characters.")


# How the code is written
def test_num_letters_uses_a_while_loop():
  lab6.check_loops("q1", "num_letters", required="while", forbidden="for", readme_part="Part 1")


def test_q1_has_no_print_calls():
  lines = util.find_print_calls("q1")
  assert lines == [], (
      f"src/q1.py calls print() on line(s) {', '.join(map(str, lines))}. num_letters should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py, or inside an `if __name__ == \"__main__\":` "
      f"block at the end of the file.)")
