import pytest
import util
import util_lab_6 as lab6

DIRECTION_HINT = ("Your function moved the letters the wrong way. A positive amount moves each letter *back* "
                  "toward 'a' (e.g. cipher('b', 1) is 'a'), which is what happens if you look up each letter in "
                  "an alphabet shifted with your shift function from Part 5.")
NOT_IN_ALPHABET_HINT = ("index() crashes with a ValueError when the character is not in the string. Characters "
                        "that are not letters must be left unchanged, so check whether a character is `in` the "
                        "alphabet before looking up its index.")
CASE_HINT = ("Uppercase letters must stay uppercase and lowercase letters must stay lowercase. One way to do this "
             "is to use a second alphabet of uppercase letters (and its shifted version) for uppercase letters.")


def cipher():
  """Return the cipher function defined in src/q6.py"""
  return util.get_student_function("q6", "cipher", "Part 6")


def check(text, amount, expected, explanation, hint=None):
  mistakes = {
      lab6.cipher(text, -amount): DIRECTION_HINT,
      lab6.cipher(text.lower(), amount): CASE_HINT,
      lab6.cipher(text.upper(), amount): CASE_HINT,
  }
  lab6.check_string_result(cipher(), (text, amount), expected, explanation, hint,
                           hints={ValueError: NOT_IN_ALPHABET_HINT}, mistakes=mistakes)


def test_cipher_is_defined():
  cipher()


def test_cipher_takes_two_parameters():
  util.check_parameter_count(cipher(), 2, "the string to encrypt, and the amount to shift by")


def test_cipher_has_a_docstring():
  cipher()
  util.check_has_docstring("q6", "cipher")


def test_cipher_returns_instead_of_printing(capsys):
  util.check_returns_instead_of_printing(capsys, cipher(), "abc", 1)


def test_shift_of_0_does_nothing():
  check("abc", 0, "abc", "A shift of 0 leaves every letter as it was.")


def test_positive_amount_moves_letters_back():
  check("b", 1, "a", "A shift of 1 moves each letter back 1 place in the alphabet.")
  check("hij", 3, "efg", "A shift of 3 moves each letter back 3 places in the alphabet.")


def test_negative_amount_moves_letters_forward():
  check("a", -1, "b", "A shift of -1 moves each letter forward 1 place in the alphabet.")
  check("hij", -3, "klm", "A shift of -3 moves each letter forward 3 places in the alphabet.")


def test_letters_wrap_around_past_a():
  check("abc", 3, "xyz", "Letters that move back past 'a' wrap around to the end of the alphabet.")
  check("abc", 2, "yza", "Letters that move back past 'a' wrap around to the end of the alphabet.")


def test_letters_wrap_around_past_z():
  check("xyz", -3, "abc", "Letters that move forward past 'z' wrap around to the start of the alphabet.")
  check("xyz", -2, "zab", "Letters that move forward past 'z' wrap around to the start of the alphabet.")


def test_large_amounts():
  check("abc", 26, "abc", "There are 26 letters, so a shift of 26 moves each letter all the way around the alphabet.")
  check("xyz", 100, "bcd", "A shift of 100 is the same as a shift of 100 % 26, which is 22.")
  check("abc", -27, "bcd", "A shift of -27 is the same as a shift of -1.")


def test_uppercase_letters_stay_uppercase():
  check("HIJ", 3, "EFG", "Uppercase letters are encrypted to uppercase letters.", CASE_HINT)
  check("ABC", 3, "XYZ", "Uppercase letters are encrypted to uppercase letters.", CASE_HINT)


def test_case_is_maintained():
  check("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", 1,
        "ZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYy",
        "Each letter keeps its case (uppercase or lowercase) when it is encrypted.", CASE_HINT)


def test_characters_that_are_not_letters_are_unchanged():
  check(" ,!@#$%^&*()_", 23, " ,!@#$%^&*()_", "Characters that are not letters must be left unchanged.")
  check("0123456789", 5, "0123456789", "Characters that are not letters must be left unchanged.")


def test_empty_string():
  check("", 5, "", "There is nothing to encrypt in the empty string.")


def test_readme_examples():
  for amount, expected in [(1, "Gdkkn, vnqkc!"), (0, "Hello, world!"), (-1, "Ifmmp, xpsme!"), (3, "Ebiil, tloia!"),
                           (123, "Olssv, dvysk!"), (234, "Hello, world!")]:
    check("Hello, world!", amount, expected, "This is one of the examples in Part 6 of the README.")


def test_cipher_can_be_decoded():
  encrypted = util.call(cipher(), "Hello, World!", 3, hints={ValueError: NOT_IN_ALPHABET_HINT})
  if not isinstance(encrypted, str):
    util.check_returned("cipher('Hello, World!', 3)", encrypted, "Ebiil, Tloia!")
  check(encrypted, -3, "Hello, World!",
        f"cipher('Hello, World!', 3) returned {encrypted!r}. Encrypting that with the opposite amount (-3) must give "
        f"back the original message.")


def test_q6_has_no_print_calls():
  lines = util.find_print_calls("q6")
  assert lines == [], (
      f"src/q6.py calls print() on line(s) {', '.join(map(str, lines))}. cipher should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py, or inside an `if __name__ == \"__main__\":` "
      f"block at the end of the file.)")
