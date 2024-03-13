# First Python Kata

Let's do our first Python kata. This one comes straight off the JavaScript course, so you should have done this already. The logic you employ will be the same, we just need to change to Python syntax.

For practice, let's set up our repo properly. First of all, ensure that you have installed `flake8`, `pytest` and can use `make` as described in `README.md`. 

## Sentence to upper or lower CamelCase

The first challenge is to implement a function which takes a sentence and converts it to upper or lower camel case.

The function takes two arguments; the sentence, and a boolean, true if UpperCamelCase is to be returned and false if lowerCamelCase is to be returned.

To help you on your way we have created the test folder, and your very first Python test file complete with first test!

💡 **The import structure at the top of this file will help you build new test files for each kata. Each new test file must start with test\_**

## How to go about writing tests
There is no set way to write tests, each problem you face is unique and you will have to approach it with an open mind.  There are however some guidelines you can follow to give you more confidence that your tests are thorough. The following is a list of things to consider when writing tests:

- **Test the smallest units of functionality**. Write tests for each function or method. If a function calls another function you want to test them separately. This will make it easier to debug when something goes wrong.
- **Test the happy path first**. Write tests for the expected behaviour of your code. This will help you to make sure that your code is working as expected.  If a function is supposed to return a list, write a test that checks that it returns a list. If a function is supposed to take a string and a number as inputs, give the function a string and a number in your happy path tests.
- **Think about the problem outside of code to create test cases**. Programming is a tool we use to solve problems in the 'real world'. Think about how you would solve the problem without writing code (with a pen and paper).  What types of inputs could you get?  If it is a string, does it matter if it is empty, if letters are capitalised, if there are white spaces, numbers, special characters?  If it is a number, what happens if it is a float, a negative number, a very large number? If you think that these cases might be important, write tests for each of them. If you have multiple inputs, think about how different combinations of inputs might affect the output, and then write tests for each of these cases.
- **Organise your tests in a structured way**. You might be able to write simple tests in a single line and still have them be readable.  With more complex tests you might want to very obviously structure them in a 'arrange', 'act', 'assert' format.  You may even want to write comments to explain what parts of a test are doing if you think it would not be immediately obvious to someone else reading your code.  When you find a way that works for you, stick to it and keep it consistent throughout your testing.
- **Organise your test files in a structured way**. Test files can get large so organising your tests in a logical order can help someone else understand what is going on. Keep happy path tests together, and errors together etc. If your function has multiple inputs keep the tests that are testing the first input together.  You might want to use comments to separate different sections of your tests.
- **You can have multiple assert statements in a single test**. If you have a function that returns a list, you can write a test that asserts that the list has the correct length, and then another assert statement that checks that the list contains the correct values.  This can make your tests more readable and easier to debug rather than having a separate test for each assert statement.
- **What do you want to happen when things go wrong (the sad path)**?  If you give a function an input that it is not expecting, what should happen?  Should it throw an error?  Should it return a default value?  Should it return a string saying "woops something isn't quite right"? For these katas we want to focus on the happy path, but it is worth thinking about what you want to happen when things go wrong.  If you want to write tests for the sad path, decide what **you** want to happen... and then test for it!

## Running tests

To run your tests for each kata, in your terminal you will run the following command from the root directory of the project:

```bash
make unit-test <path to test file>
```

For example, to test `sentence_to_camel_case`, run:
```bash
make unit-test test/test_sentence_to_camel_case.py
```

To run **all** your test files in your test folder run the following command:

```bash
make run-checks
```

For the later katas (from `multiplication_table` onwards), this command will also run a PEP8 check.

## Examples

You can use these examples to start building up your test suite

```python
sentence_to_camel_case("this sentence", True)
# should return "ThisSentence"
```

```python
sentence_to_camel_case("this sentence", False)
# should return "thisSentence"
```

```python
sentence_to_camel_case("This Bigger strange Sentence", True)
# should return "ThisBiggerStrangeSentence"
```

For a further challenge extend your current function or implement another in the same file which takes CamelCase and returns it as a plain english sentence (ending in a full stop).

```python
camel_to_english("thisBiggerStrangeSentence")
# should return "This bigger strange sentence."
```

Note that there are already some changes from the JavaScript example.

-   Following PEP8, our function names are in `snake_case` rather than `CamelCase`
-   There is no semicolon following the function invocation.
-   The boolean keywords begin with capital letters (ie `True` and `False`).
-   The comments are indicated by a hash `#` rather than the double slash `//` of JavaScript.

So, set up a code file in `src/sentence_to_camel_case`, and a test file in `test`, and get coding! The purpose of this is to get to grips with Python syntax, so don't worry too much about the logic of how you do this - if you have a working JavaScript version, by all means just try to translate it.

Some stuff you might find useful:

1. [The Python SpeedSheet](https://speedsheet.io/s/python) is a useful cheatsheet for Python. Look at the Hello World section, and [the basics of Functions](https://speedsheet.io/s/python?q=functions-only).
1. The [string operations](https://speedsheet.io/s/python?q=strings-only#T7xJ) section might be useful too. Purists may want to look at the actual [Python docs](https://docs.python.org/3/library/string.html).
1. Who knows, maybe something on [list operations](https://speedsheet.io/s/python?q=list-only#hCt6) might be [useful](https://docs.python.org/3/tutorial/datastructures.html)?

In the standard, tried and trusted Northcoders fashion, we'll just chuck you in at the deep end with no buoyancy aid, although we might throw you a lifeline if you really need it! Go for it!
