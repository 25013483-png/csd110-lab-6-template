# Lab 6 - Loops and String Sequences

## Setup

1. Click the "**Use this template**" button near the top of this repository on GitHub
2. Set the following properties on the GitHub repository, then click "Create repository":
    - **Owner**: your GitHub username (NOT the course organization)
    - **Name**: csd110-26f-lab-6
    - **Visibility**: Private
3. In your new repository, go to Settings -> Collaborators, and add your instructor as a collaborator.
4. Create a branch named `lab-6` on which to do your lab work
5. Create a Codespace on that branch, and open it (give it a few minutes to initialize)
6. In your Codespace terminal, verify your setup using `gh lab setup-check`

### Required Reading 

It is assumed that you have watched all lecture videos and completed readings and practice exercises up to the end of Chapter 8 (not including Chapter 4) in the course textbook.  If you have not done so yet, you should! 

### Reflections

As you are working on your lab, help yourself remember important things by taking notes in `reflections.md`. Record notes about anything you think important to remember, any problems you encountered and how you resolved them, and any remaining questions you may still have.

> **NOTE**: `reflections.md` is a 'markdown' file.  Markdown is a markup language that has simple syntax for adding formatting to plain text documents. See [this documentation on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to learn how to format text in a markdown file.

### AI Use

> **IMPORTANT**: ***Failure to include an accurate AI Use Statement as described below may result in a lab grade deduction of up to 100% depending on your instructor's evaluation of how well you understand the code you submit***

You MAY use AI as a LEARNING AID to help you understand topics you are needing extra help with.
You may NOT use AI to do your work for you or to avoid having to think and learn on your own.

#### AI Use Statement

**Whether or not you use AI**, you MUST include an AI Use Statement in your `reflections.md` document that indicates clearly:

- Which specific AI tools you used in the completion of this lab (or an explicit statement that you did not use any AI tools).
- Links to or copies of **ALL** AI chats you had related to this assignment. 

> **IMPORTANT:** if sharing a link, do NOT simply copy the URL from your browser; you MUST click the **Share** button and create a public link.

Examples:
- I used ChatGPT to help me better understand the lab requirements.  Below are links to my ChatGPT chats.
- I used Claude to give me examples of statements vs expressions in Python.  Below are links to my conversation.
- I did not use any AI tools to complete this lab.

### Running your code

#### From the terminal

1. Open the terminal (View -> Terminal)
2. Enter a command like the following `python path/to/script.py`.  For example, to run the `q1.py` script in the `src` folder, run `python src/q1.py`.

#### Using the debugger

1. Open the Python file you want to run
2. Open the 'Run and Debug' panel (right side, right-arrow icon with bug in lower left corner). 
3. Make sure the "Python Debugger: Current File" configuration is selected in the dropdown at the top of the panel.
4. Click the green arrow button to run the currently opened Python file

### Testing your code

A set of tests have been prepared for this lab that will help you determine if your code is correct or not.

#### Running tests 

| Task | Command | Example |
|------|---------|---------|
| Run all tests | `pytest` | `pytest` |
| Stop at the first failing test while working | `pytest -x` | `pytest -x` |
| Run one test file | `pytest <path_to_file>` | `pytest test/test_q1.py` |
| Run one test function | `pytest <path_to_file>::<function_name>` | `pytest test/test_q1.py::test_num_letters_is_case_insensitive` | 

While working, use `pytest -x` to focus on one failure at a time. Fix that issue and run the same command again to continue through the tests. Once the tests are passing this way, run `pytest` to check the entire lab.

#### Reading test output

The output of the tests will give you an indication of which tests passed or failed. For any failed tests, you will also see messages that should help you determine why the test failed.

Here are some tips for dealing with failing tests:

1. The name of the test itself usually gives a clue as to what the test is checking (e.g. `test_num_letters_is_case_insensitive`).
2. Read the message under the test name. It usually says which function call was tested, what your function returned, what it should have returned, and why.
3. When a string is wrong, the message shows the "Expected" and "Returned" values one above the other, with a `^` under the first character that is different.
4. If a line starting with `src/` appears in the output, it shows the line in **your** code where the problem happened.
5. If a test says your code "did not finish", it is probably stuck in an infinite loop: check that the condition of each `while` loop eventually becomes `False`.
6. The tests for each part are in order, starting with the simplest. Fix the first failing test before worrying about later ones. Often fixing one test fixes other failing tests as well.
7. When working on a failing test, run just that test (see above) so you can focus on its output without having to wade through the output of all the other tests.

#### Passing tests does not guarantee correctness

If all the tests passed, you can be reasonably sure that your code is correct, **BUT PASSING ALL TESTS DOES NOT NECESSARILY MEAN YOU WILL GET 100%** because some grades are assigned to non-coding tasks, and it is sometimes possible to create incorrect programs that do pass the tests.

## Instructions

### Overview

In this lab you will practice using loops and strings in Python programs.  You will create a number of 'utility' functions to help you determine things about strings that are not built into the Python standard library.

> **IMPORTANT**: You are expected to use meaningful names for all functions and variables, and you must document all functions with appropriate docstrings as discussed in class.  Failing to do so may result in a lower grade.

### Part 1 - While loop

In this part you will use a simple while loop to implement a function that determines the number of times certain letters appear in a given string.

> **IMPORTANT:** Use appropriate variable names, docstrings, and code comments

In `q1.py`...

1. Create a **PURE** function named `num_letters`
2. The function has 2 parameters, both of which must be strings (state this as a precondition in your docstring)
3. The function returns the number of times ANY of the characters from the *second* string appear in the *first* string.
4. The function must NOT be case sensitive
5. **IMPORTANT**: your implementation MUST use a `while` loop

 > **Examples:**
 > ```python
 > num_letters("something", "s")     # returns 1
 > num_letters("mississippi", "s")   # returns 4
 > num_letters("miSsiSsippi", "S")   # returns 4
 > num_letters("mississippi", "si")  # returns 8 (4 "s" plus 4 "i")
 > num_letters("mississippi", "ss")  # returns 4 (repeated letters in the second parameter must NOT add to the count)
 > num_letters("mississippi", "")    # returns 0
 > num_letters("", "s")              # returns 0
 > ```

### Part 2 - For loop

In `q2.py`...

1. Create the same function as in Part 1, but this time do NOT use a `while` loop; use a `for` loop instead

### Part 3 - More string traversal

In this part you will make a function that calculates the number of vowels in a given word.

> **IMPORTANT:** Use appropriate variable names, docstrings, and code comments

In `q3.py`...

1. Create a **PURE** function named `num_vowels`
2. The function has 1 parameter. Use guardians to ensure the following:

    1. Use an `assert` statement to verify that the parameter is a string
    2. Using a loop, check that each character in the string is a letter of the English alphabet (i.e., no spaces or special characters allowed); if it is not, raise an appropriate `AssertionError` (yes, you can use `assert` statements in the body of a loop)

3. The function returns the number of vowels (one of a, e, i, o, u or y) in the string.
    1. **IMPORTANT:** the function must NOT be case sensitive
    2. An empty string is valid (it contains no characters that are not letters), and has 0 vowels

    **HINT:** The `num_letters` function you just wrote will be useful!
   
4. For full marks, handle 'y' as follows: In English, the letter y is sometimes a vowel and sometimes a consonant. Update your function to take into account the following rules:

    1. If `y` is the only vowel in the word, then every instance of `y` is considered a vowel. (E.g., y is a vowel in the words 'wryly' and 'ympt')
    2. If `y` is NOT the only vowel in the word, then...
       1.  Any `y` followed by a, e, i, o, or u is considered a consonant
       1.  Any other `y` is a vowel

### Part 4 - Indexing, slicing, and formatting strings

In `q4.txt` copy and paste the REPL session you are guided through below. Your grade for this part will depend on how thoroughly you demonstrate experimentation.  Be a scientist! Make and test hypotheses about how you expect things to work.

1. In your terminal, run the `python` command to run a Python REPL
2. Create a variable that contains a string value with at least 10 characters, including spaces and emojis.
3. Use indexing to print various individual symbols in the string. Experiment with the different values for the index, including (but NOT limited to)...

    1. What is the index for the first character?
    2. What is the index of the last character?
    3. What happens if you use an index beyond the 'end' of the string?
    4. Can you retrieve just a space character? Just an emoji?
    5. How does the length of the string compare with the index of the last character?
    6. What happens when you use a negative index?
    7. Can you use a float as an index?
    8. Can you use as an index a variable or a function call that yields an integer?
    9. Can you use an expression such as `math.sqrt(100) + x * 2` as an index? (You will need to import the math module and set the variable x to an integer)
  
4. Use slicing to print various parts of the string. Experiment with different values for the start and end index of your slices, including...

    1. Leave one or the other or both blank
    2. What happens if you use negative indices?
    3. What happens if you use indices that are 'beyond the end' of the string?
    4. What happens if the indices are equal?
    5. What happens if the start index is greater than the end index?

5. Experiment with f-strings. Create f-strings that...

    1. Contain multiple placeholders, e.g. `f"X is {x} and Y is {y}"`
    2. Use function calls and other expressions as the placeholder values

6. Experiment with the `format` function.  Create strings that...

    1. Create a string that re-orders the values passed to the `format` function
    2. What happens if you provide a different number of arguments to the `format` function than there are placeholders in the string?
    3. There is a [powerful placeholder syntax](https://docs.python.org/3/library/string.html#format-examples) that allows you to format the values in each placeholder. Try some of the options documented in the previous link.

### Part 5 - Use slicing

In this part you will make a function that 'shifts' a given string (see the examples below) by a given amount. You will use this as a helper function in Part 6.

> **IMPORTANT:** Use appropriate variable names, docstrings, and code comments

In `q5.py`...

1. Create a **PURE** function named `shift`
2. The function accepts two parameters, a string (the string to shift) and an int (the amount to shift by)
3. The function returns a new string with the symbols in the given string 'shifted' by the given number of positions (see the examples below)
    1. Positive amounts move letters to the right; negative shifts move letters to the left
    2. Letters that 'fall off the end' get wrapped around to the other end so that the returned string is the same length as the original

    > **Examples:**
    > ```python
    > shift("abcdef", 1)    # "fabcde" 
    > shift("abcdef", 4)    # "cdefab" 
    > shift("abcdef", 0)    # "abcdef" 
    > shift("abcdef", -1)   # "bcdefa" 
    > shift("abcdef", 7)    # "fabcde"
    > shift("abcdef", 25)   # "fabcde"
    > shift("", 3)          # "" (an empty string has nothing to shift)
    > ```

    **HINT:** This function can be implemented quite simply using a couple slices.  (Did you experiment with negative slice indexes in part 4?  You should!)
    
    **HINT:** Remember how the `%` operator is useful for cyclical operations? This is another such circumstance. Note how a shift of 1, 7, and 25 all yield the same result above (and the same would be true for 13, 19, 25, 31, etc). Consider that `7 % len("abcdef") == 1`. You can use a similar calculation to determine how many positions to shift any given string for any given integer without going 'out of bounds'.

### Part 6 - Problem solving using loops and strings

Read about the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). In this part you will implement a function that encrypts a given string using the Caesar cipher with a specific shift amount.

A simple strategy for accomplishing this is as follows: 

- Create a string containing all the letters in the alphabet
- Create another string with all the letters shifted by a given number of positions (oh hey! you just made a function that does exactly that)
- Now, build the encrypted string by looping through each letter in the original string, and...
    - Determine the index of that letter in the regular alphabet
    - Find the corresponding letter (at that same index) in the shifted alphabet, and add this letter to the encrypted string

> **IMPORTANT:** Use appropriate variable names, docstrings, and code comments

In `q6.py`...

1. Create a **PURE** function named `cipher`
2. The function takes two parameters: a string to be encrypted, and an integer indicating the amount to shift by
3. The function returns a new string that is the Caesar cipher of the original string using the given shift amount
    1. Uppercase letters must remain uppercase and lowercase letters must remain lowercase when encrypted.
    2. Non-alphabetical symbols remain unchanged

   > **Examples:**
   > ```python
   > cipher("Hello, world!", 1)      # Gdkkn, vnqkc! 
   > cipher("Hello, world!", 0)      # Hello, world! 
   > cipher("Hello, world!", -1)     # Ifmmp, xpsme! 
   > cipher("Hello, world!", 3)      # Ebiil, tloia! 
   > cipher("Hello, world!", 123)    # Olssv, dvysk! 
   > cipher("Hello, world!", 234)    # Hello, world! (since 234 is a multiple of 26) 
   > ```

## Reflect

Did you take notes in `reflections.md` as you worked? (See the [Reflections](#reflections) instructions above.) You should!

Did you document your AI usage adequately? (See the [AI Use](#ai-use) instructions above.) You must!

## Submission

1. **Test** your code to verify that it is working as expected (see the [Testing your code](#testing-your-code) section above).
2. **Review** your code to ensure that you are using appropriate names, comments, and docstrings
3. **Commit** all changes in your lab files with meaningful commit messages.
4. **Push** your commits to GitHub
5. **Verify** that the code on GitHub is correct
6. Create a **Pull request** using your lab branch as the 'compare' branch and the main branch as the 'base'
7. Navigate to the "Files Changed" tab of your pull request, and **copy the URL** to this page into the lab folder on the LMS.

## Rubric

See the rubric attached to this lab in the LMS

### Automatic limits:

Your grade will be limited to a maximum of 79% for any of the following:
- Missing / inadequate [AI Use Statement](#ai-use)
- Missing / inadequate [Reflections](#reflections)
- Incorrect lab [Setup](#setup)

