import pytest
import re
import util

REPL_PROMPT = ">>> "


def repl_session():
  """Return the lines of src/q4.txt that were typed at the REPL's >>> prompt"""
  text = (util.SRC_DIR / "q4.txt").read_text(encoding="utf-8")
  if text.strip() == "":
    pytest.fail("src/q4.txt is empty. Copy and paste your REPL session from Part 4 of the README into it.",
                pytrace=False)
  typed = [line[len(REPL_PROMPT):] for line in text.splitlines() if line.startswith(REPL_PROMPT)]
  if typed == []:
    pytest.fail(
        "src/q4.txt doesn't look like a REPL session: none of its lines start with the REPL's >>> prompt. Run "
        "`python` in the terminal, do the experiments in Part 4 of the README, then copy and paste the whole session "
        "(including the >>> prompts and Python's responses) into src/q4.txt.",
        pytrace=False)
  return typed


def check_tried(pattern, what, step):
  if not any(re.search(pattern, line) for line in repl_session()):
    pytest.fail(
        f"src/q4.txt doesn't seem to include any {what}. Step {step} of Part 4 in the README asks you to experiment "
        f"with these.",
        pytrace=False)


def test_q4_contains_a_repl_session():
  repl_session()


def test_q4_tries_indexing():
  check_tried(r"\w\[[^\]:]+\]", "indexing (e.g. text[0])", 3)


def test_q4_tries_slicing():
  check_tried(r"\w\[[^\]]*:[^\]]*\]", "slicing (e.g. text[2:5])", 4)


def test_q4_tries_f_strings():
  check_tried(r"\b[fF][rR]?['\"]", "f-strings (e.g. f\"X is {x}\")", 5)


def test_q4_tries_format():
  check_tried(r"\.format\(", "calls to the format function (e.g. \"{} {}\".format(x, y))", 6)
