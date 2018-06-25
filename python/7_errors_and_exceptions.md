
<!-- vim-markdown-toc GFM -->

1. [Syntax Errors](#syntax-errors)
1. [Exceptions](#exceptions)
	1. [Built-in Exceptions](#built-in-exceptions)
	1. [User defined exceptions](#user-defined-exceptions)
	1. [Raising and Handling Exceptions](#raising-and-handling-exceptions)
		1. [`raise`](#raise)
		1. [Handling Exceptions](#handling-exceptions)
			1. [Clean-ups](#clean-ups)

<!-- vim-markdown-toc -->

# Syntax Errors
Not more to mention....
```python
>>> if True print("True")
  File "<stdin>", line 1
    if True print("True")
                ^
SyntaxError: invalid syntax
```

# Exceptions

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
The last line will indicates what happened. 

## Built-in Exceptions

Python has a list of 
[Built-in Exceptions](https://docs.python.org/3.6/library/exceptions.html#bltin-exceptions).
All exceptions must be sub-classes of `BaseException`, programmers are 
encouraged to derive new class from `Exception` or its sub-classes.

## User defined exceptions

## Raising and Handling Exceptions

Programs may defines its own exceptions, they has to be subclass of 
`BaseException` and are encouraged to be subclass of `Exception`.
Generally, exception class should be kept simple, i.e. they should 
only provides a message and needed information to understand the exception.
Most exceptions are defined in with a name ended with "Error".

### `raise`

`raise` statement raise exceptions.

	raise_stmt ::=  "raise" [expression ["from" expression]]

If no expression presented, raise re-raise the last exception that was 
active in the current scope. If there is no such exception, `RunTimeError`
will be raised. The exception expression after `from` is an indicator 
of the new exception thrown, which will be set as the `__cause__` 
attribute of the new exception thrown.

### Handling Exceptions

```python
try:
	contents
[exception expression:
	pass]*
[exception (expression, ...)
	pass]*
[else:
	pass]
[finally:
	pass]
```

The procedure of exception handling is the same as Java and C++, so 
Lin-pe will not mention it here.

#### Clean-ups

The benefit of `else` is that it claims that the exceptions will not 
occurs in the clause(s), preventing mistakenly handling the some 
exceptions. The `finally` clause will _always_ be executed at the end of 
`try` statement, even if it is left via `break`, `continue` or `return`.

The followings are from <https://docs.python.org/3.6/tutorial/errors.html>

Excerpt 1
```python
for line in open("myfile.txt"):
    print(line, end="")
```

Excerpt 2
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Excerpt 2 is better than 1 because it close f as soon as the for loop ends,
or as soon as an exception happens.


