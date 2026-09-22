# Python Practice – CodeWithHarry Course

Practice code and small programs written while following the CodeWithHarry Python course, organized by chapter (topic), plus two small standalone games. 79 practice programs across 11 chapters.

> [!NOTE]
> **This is a learning repository**, not a production project. The code is exercise-level, written while first learning each topic, and a few files intentionally demonstrate what happens when something goes *wrong* (e.g. mutating a tuple). See [Known Issues](#known-issues--things-to-fix) before treating any file as a reference implementation.

---

## Chapter Index

| Chapter | Topic | Highlights |
|---|---|---|
| [Chapter1](Chapter1) | Getting started | Multi-line `print()`, a first Flask "Hello World" route, listing a directory with `os.listdir` |
| [Chapter2](Chapter2) | Variables & input | Reading input, `int()` casting, basic arithmetic, `type()` |
| [Chapter3](Chapter3) | Strings | f-strings, `.replace()`, `.find()`, multi-line strings, escape characters |
| [Chapter4](Chapter4) | Lists & tuples | Building a list with `.append()`, `sorted()`, tuple immutability, `.count()` |
| [Chapter5](Chapter5) | Sets & dictionaries | Set de-duplication, mixed-type sets, dictionary lookup with `.get()`, `.update()` |
| [Chapter6](Chapter6) | Conditionals | Pass/fail percentage checker, a keyword-based spam-phrase detector, username length validator |
| [Chapter7](Chapter7) | Loops | Multiplication tables (`for` and `while`), prime check with `for...else`, sum of N numbers, recursive factorial |
| [Chapter8](Chapter8) | Functions | Largest of three numbers, Celsius→Fahrenheit, recursive sum, a star pattern, inches→cm, removing an item from a list |
| [Chapter9](Chapter9) | File handling | Reading/writing/appending text files, searching a log file for a keyword, generating 18 multiplication-table files, copying and comparing file contents |
| [Chapter10](Chapter10) | OOP basics | Classes, `__init__` constructors, instance vs. class attributes, `@staticmethod` |
| [Chapter11](Chapter11) | OOP advanced | Inheritance (`super()`), operator overloading (`__add__`, `__mul__`), `__repr__`, `__len__`, `@property` with a setter |

## Mini Projects

| Project | Description |
|---|---|
| [`Project 1 , Snake, water gun game`](<Project 1 , Snake, water gun game>) | A rock-paper-scissors variant (snake beats water, water beats gun, gun beats snake) played against a random computer choice |
| [`Project 2, Number Guess`](<Project 2, Number Guess>) | Guess a random number between 1 and 50; the program counts and reports how many attempts it took |

---

## Concepts Practiced

Variables, type casting and input handling · string formatting and methods · lists, tuples, sets and dictionaries · conditionals · `for`/`while` loops and `for...else` · functions and recursion · file I/O (read, write, append) · basic Flask routing · object-oriented programming: classes, constructors, static methods, inheritance, dunder/magic methods, and properties.

---

## Known Issues / Things to Fix

A few files behave differently than intended — useful to know before treating them as reference code:

- **`Chapter7/problem6.py`** — `factorial` starts at `0` instead of `1`, so `factorial * number` always returns `0`. A correct version is left commented out just above it.
- **`Chapter4/problem3.py`** — assigns to a tuple index (`tuple[0] = "Ahmed"`), which raises `TypeError: 'tuple' object does not support item assignment`. This is intentional, to show tuples are immutable, but the script won't run past that line.
- **`Project 2, Number Guess/main.py`** — the "too high" branch correctly says *"Enter lower number"*, but the else branch prints *"Print higher number"* instead of *"Enter higher number"* — a copy-paste typo, not a logic bug.
- **`Chapter9/problem2.py`** — opens `high_score.txt` for reading without first checking the file exists. It works here because `high_score.txt` is already included in this repo, but the script would crash on a machine where that file is missing.
- **`Chapter11/problem3.py`** — the `@property` getter (`e.salaryafterincrement`) is only called in a commented-out line, so the script currently just prints the raw `increment` value rather than demonstrating the computed property.
- **`Chapter8/problem4.py`** — names a recursive function `sum`, which shadows Python's built-in `sum()` for the rest of that file.
- **Naming style varies** — most classes use `self`, but `Chapter10/problem6.py` uses `slf` instead. Both work; `self` is the Python convention.

## Generated Output Files

`Chapter9/` includes the actual `.txt` files and the `tables/Table2`–`Table19` files these scripts read and write (poem, log file, high score, multiplication tables). These are outputs from running the exercises, kept so the file-handling examples are runnable as-is without regenerating them first, not hand-written source.

---

## How to Run

Most files run directly and prompt for input in the terminal:

```bash
python Chapter7/problem1.py
```

`Chapter1/program3.py` needs Flask installed first:

```bash
pip install flask
python Chapter1/program3.py
```

File-handling scripts in `Chapter9/` use relative paths, so run them from inside the `Chapter9/` folder.

---

## Credits

Course: [CodeWithHarry](https://www.youtube.com/watch?v=UrsmFxEIp5k) — Python tutorial series.
