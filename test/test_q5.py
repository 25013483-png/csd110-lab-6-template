import pytest
import util
import util_lab_6 as lab6

DIRECTION_HINT = ("Your function shifted the letters the wrong way. Positive amounts move letters to the right "
                  "(toward the end of the string), so shift('abcdef', 1) is 'fabcde'.")
WRAP_HINT = ("Use the % operator to turn any amount into an amount from 0 to len(text) - 1, e.g. "
             "7 % len('abcdef') is 1 (see the hints in Part 5 of the README).")
EMPTY_HINT = ("A ZeroDivisionError here usually means you calculated `amount % len(text)` when the text is empty "
              "(so len(text) is 0). Shifting the empty string gives the empty string, so handle that case first.")


def shift():
  """Return the shift function defined in src/q5.py"""
  return util.get_student_function("q5", "shift", "Part 5")


def check(text, amount, expected, explanation, hint=None):
  lab6.check_string_result(shift(), (text, amount), expected, explanation, hint,
                           hints={ZeroDivisionError: EMPTY_HINT, IndexError: WRAP_HINT},
                           mistakes={lab6.shift(text, -amount): DIRECTION_HINT})


def test_shift_is_defined():
  shift()


def test_shift_takes_two_parameters():
  util.check_parameter_count(shift(), 2, "the string to shift, and the amount to shift it by")


def test_shift_has_a_docstring():
  shift()
  util.check_has_docstring("q5", "shift")


def test_shift_returns_instead_of_printing(capsys):
  util.check_returns_instead_of_printing(capsys, shift(), "abcdef", 1)


def test_shift_of_0_does_nothing():
  check("abcdef", 0, "abcdef", "Shifting by 0 leaves the string as it was.")
  check("abc", 0, "abc", "Shifting by 0 leaves the string as it was.")


def test_shift_right_by_1():
  check("abcdef", 1, "fabcde", "Each letter moves 1 place to the right, and the last letter wraps around to the start.")
  check("abcdefgh", 1, "habcdefg",
        "Each letter moves 1 place to the right, and the last letter wraps around to the start.")


def test_shift_right_by_more_than_1():
  check("abcdef", 4, "cdefab",
        "Each letter moves 4 places to the right, and the last 4 letters wrap around to the start.")
  check("abcde", 4, "bcdea", "Each letter moves 4 places to the right, and the last 4 letters wrap around to the start.")


def test_shift_left():
  check("abcdef", -1, "bcdefa",
        "A negative amount moves letters to the left, so the first letter wraps around to the end.")
  check("abcdef", -4, "efabcd",
        "A negative amount moves letters to the left, so the first 4 letters wrap around to the end.")


def test_shift_by_the_length_of_the_string_does_nothing():
  check("abcdez", 6, "abcdez", "Shifting a 6 letter string 6 places moves every letter all the way around, back to "
        "where it started.", WRAP_HINT)
  check("bcdef", -5, "bcdef", "Shifting a 5 letter string -5 places moves every letter all the way around, back to "
        "where it started.", WRAP_HINT)


def test_shift_right_past_the_end():
  check("abcdef", 7, "fabcde", "Shifting a 6 letter string 7 places is the same as shifting it 1 place.", WRAP_HINT)
  check("abcdef", 13, "fabcde", "Shifting a 6 letter string 13 places is the same as shifting it 1 place.", WRAP_HINT)
  check("abcdef", 25, "fabcde", "Shifting a 6 letter string 25 places is the same as shifting it 1 place.", WRAP_HINT)


def test_shift_left_past_the_start():
  check("abcdef", -7, "bcdefa", "Shifting a 6 letter string -7 places is the same as shifting it -1 places.",
        WRAP_HINT)
  check("abcdef", -25, "bcdefa", "Shifting a 6 letter string -25 places is the same as shifting it -1 places.",
        WRAP_HINT)


def test_shift_any_characters():
  check("Hi, 😀!", 2, "😀!Hi, ", "shift works with any characters, not just letters.")


def test_shift_single_character():
  check("a", 5, "a", "A string with only 1 character is the same however far it is shifted.", WRAP_HINT)


def test_shift_empty_string():
  check("", 3, "", "The empty string has no characters to shift, so shifting it gives the empty string.")


def test_q5_has_no_print_calls():
  lines = util.find_print_calls("q5")
  assert lines == [], (
      f"src/q5.py calls print() on line(s) {', '.join(map(str, lines))}. shift should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py, or inside an `if __name__ == \"__main__\":` "
      f"block at the end of the file.)")
