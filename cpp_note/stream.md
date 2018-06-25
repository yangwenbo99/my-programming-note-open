
<!-- vim-markdown-toc GFM -->

1. [Stream](#stream)
	1. [Hierarchy:](#hierarchy)
	1. [Input and output methods](#input-and-output-methods)
1. [Stream Manipulations](#stream-manipulations)

<!-- vim-markdown-toc -->
# Stream

C++ provides several header for stream. `<iostream` provides services for 
all stream I/O and provides the following objects:
- `cin`: standard input,
- `cout`: standard output,
- `cerr`: _unbuffered_ standard error stream, and
- `clog`: _buffered_ standard error stream.
C++ also provides `<iomanip>` for _parameterized stream manipulation_ and 
`<fstream>` for file processing.

## Hierarchy:
![basic_fstream](http://upload.cppreference.com/mwiki/images/f/f1/std-basic_fstream-inheritance.svg)
![basic_ifstream](http://upload.cppreference.com/mwiki/images/7/79/std-basic_ifstream-inheritance.svg)
![basic_ofstream](http://upload.cppreference.com/mwiki/images/b/b1/std-basic_ofstream-inheritance.svg)

## Input and output methods

In this section `os` represents a object with the type `basic_ostream`, and 
`is` for `basic_istream`
- `os.put(char)`: put a char
- `is.get()`, with multiple version, get a single `char` or characters.
	If used with `char*`, the size must be specified, the function will read 
	at most `count-1` characters and append `'\0'`, and if used without 
	`deli`, the delimiter will automatically be `'\n'`.
- `is.getline()`, get until `deli`, or, if `deli` not specified, use '\n'
	as `deli`.

# Stream Manipulations
[references](http://www.cplusplus.com/reference/library/manipulators/)

_Sticky_ manipulators: will not change
- `hex`
- `oct`
- `dec`
- `showbase`
- `noshowbase`
- `scientific`
- `fixed`
- `setbase(n)`: a _parameterized_ stream manipulator.
- `setprecision(n)`
- `os.setf()`: get and set flag
- `os.precision()`: get and set precision.

For parameterized manipulator:
```c++
#include <iomainp>
```

_Non-sticky_ manipulators
- `setw()`
- `os.width(n)`

They can be user defined, like: 
```c++
ostream &bell (ostream &os) {
	return os << '\a';
}
```
