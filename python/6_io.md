
<!-- vim-markdown-toc GFM -->

1. [Formatted string literals](#formatted-string-literals)
1. [Basic](#basic)
1. [Files](#files)
	1. [Opening a file](#opening-a-file)
	1. [Methods of file](#methods-of-file)
1. [JSON](#json)

<!-- vim-markdown-toc -->

# Formatted string literals
<https://docs.python.org/3/reference/lexical_analysis.html#f-strings>

```python
>>> print(f"My name is {my_name}")
My name is {my_name}
>>> print(f"My name is {my_name}")
My name is Paul
>>> print(f"I am {my_height} inches tall")
I am 74 inches tall
>>> print(f"I am {float(my_height):.5} inches tall")
I am 74.0 inches tall
```

__NOTE:__
For python2,
```python
y = "Those who know %s and those who %s." % (binary, do_not)
```

# Basic
```python
age = input("Your age please... ")
```

# Files
<https://docs.python.org/3.6/library/io.html#module-io>

## Opening a file
`open()` returns a file object, generally, 
<https://docs.python.org/3.6/library/functions.html#open>
```python
f = open(file_name, mode)
data = f.read
f.close()
```

If a file is only to be read once or so, using with will be 
a good practice, 
```python
with open("my_file") as f:
	read_data = f.read()
```
not needed to manually close it

## Methods of file
- `.read()`
- `.readline()`
- `.readlines()`		# read all line of a file into a list
- `.write(s)`
- `.tell()`
- `.seek(offset[, whence])`   #
	                  Go to certain posiion of a stream, `whence` can be one 
	                  of `SEEK_SET`, `SEEK_CUR` or `SEEK_END`

Other functions
- `list(f)`         # Cast a file into list, i.e. read all of its line into 
                      a list

# JSON

<https://docs.python.org/3.6/library/json.html#module-json>

`json` provides a series of functions to manipulate json.

- `json.dump(object, file)`, stores an object into a text file
- `json.dumps(object)`, converts an object into string
- `x = json.load(f)`
- `x = json.loads(s)`

