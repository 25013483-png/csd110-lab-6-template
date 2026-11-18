"""Helpers specific to lab 6 (loops and strings)"""

import pytest
import util

INDEX_HINT = ("An IndexError means your code used an index that is past the end of a string. If you loop with an "
              "index, the loop should stop when the index reaches len(...), e.g. `while index < len(text):`.")
NOT_A_STRING_HINT = ("Both arguments are strings, so you can loop over them (or index them) directly. "
                     "Check that you haven't mixed up a character with its index.")


# ---------------------------------------------------------------------------
# Parts 1 and 2 (num_letters is written twice: once with a while loop and once with a for loop)


def check_num_letters(num_letters, text, letters, expected, explanation, hint=None):
  """Check that num_letters(text, letters) returns expected.
     hint (optional) is extra advice shown when the result is too big"""
  call_text = util.describe_call(num_letters, text, letters)
  actual = util.call(num_letters, text, letters, hints={IndexError: INDEX_HINT, TypeError: NOT_A_STRING_HINT})
  if hint and isinstance(actual, int) and not isinstance(actual, bool) and actual > expected:
    explanation += f"\nHINT: {hint}"
  util.check_returned(call_text, actual, expected, explanation)


def check_loops(module_name, function_name, required, forbidden, readme_part):
  """Check that function_name in src/<module_name>.py uses a `required` loop ("while" or
     "for"), and that src/<module_name>.py has no `forbidden` loops anywhere"""
  finders = {"while": util.find_while_loops, "for": util.find_for_loops}
  definition = util.find_function_def(module_name, function_name)
  if definition is None:
    pytest.fail(f"Define a function named {function_name} in src/{module_name}.py, as described in {readme_part} of the README.",
                pytrace=False)
  if finders[required](definition) == []:
    pytest.fail(f"{function_name} in src/{module_name}.py must use a `{required}` loop to go through the strings, "
                f"as described in {readme_part} of the README.",
                pytrace=False)
  lines = finders[forbidden](util.parse_source(module_name))
  if lines != []:
    pytest.fail(
        f"src/{module_name}.py uses a `{forbidden}` on line(s) {', '.join(map(str, lines))}, but {readme_part} of the "
        f"README says to use a `{required}` loop instead. Rewrite your code so it only uses `{required}` loops." +
        (" (Note that a comprehension like [c for c in text] is also a for loop.)" if forbidden == "for" else ""),
        pytrace=False)


# ---------------------------------------------------------------------------
# Parts 5 and 6


def shift(text, amount):
  """The correct answer for shift (used to recognize common mistakes)"""
  if text == "":
    return ""
  amount = amount % len(text)
  return text[len(text) - amount:] + text[:len(text) - amount]


def cipher(text, amount):
  """The correct answer for cipher (used to recognize common mistakes)"""
  result = ""
  for character in text:
    for alphabet in ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
      if character in alphabet:
        character = shift(alphabet, amount)[alphabet.index(character)]
        break
    result += character
  return result


def check_string_result(function, args, expected, explanation, hint=None, hints=None, mistakes=None):
  """Check that function(*args) returns the string expected.
     hint (optional) is extra advice shown if the result is wrong.
     hints (optional) maps exception types to extra advice if the function crashes.
     mistakes (optional) maps wrong answers to a hint explaining the mistake that gives that
     answer (which is shown instead of hint)"""
  call_text = util.describe_call(function, *args)
  actual = util.call(function, *args, hints=hints)
  if isinstance(actual, str) and actual != expected:
    hint = (mistakes or {}).get(actual, hint)
  if hint:
    explanation += f"\nHINT: {hint}"
  util.check_returned(call_text, actual, expected, explanation)
