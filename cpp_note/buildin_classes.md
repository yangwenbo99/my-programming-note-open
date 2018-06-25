
<!-- vim-markdown-toc GFM -->

1. [C++ Sequence Container](#c-sequence-container)
	1. [Near containers](#near-containers)
	1. [Basic requirements for elements in containers](#basic-requirements-for-elements-in-containers)
	1. [Define An Instance](#define-an-instance)
	1. [Methods](#methods)
1. [Iterators](#iterators)
	1. [Category & Hierarchy of iterators](#category--hierarchy-of-iterators)
		1. [Predefined type of iterators](#predefined-type-of-iterators)
	1. [`istream_iterator` and `ostream_iterator`](#istream_iterator-and-ostream_iterator)
1. [<algorithm>](#algorithm)
1. [`string` Class](#string-class)
	1. [Important Concepts & Methods](#important-concepts--methods)
		1. [Length, Capacity and Max_size](#length-capacity-and-max_size)
		1. [Convert to C-string](#convert-to-c-string)
		1. [Find substring / character](#find-substring--character)
		1. [Replace contents](#replace-contents)
		1. [Other Important methods](#other-important-methods)
	1. [Iterators](#iterators-1)
	1. [String stream](#string-stream)

<!-- vim-markdown-toc -->

# C++ Sequence Container

_Avoid reinventing the wheel._
__勿重果造一斗輪仔__

C++ provides several kinds of *sequence container*, and, historically, 
they are called _Standard Template Library_ or _STL_, and, historically,
developed by HP's employee:

- sequence containers
	- `array`
		+ a compile-time non-resizable array.
		+ direct access to all elements.
		+ only in C++11
	- `vector`
		+ Dynamic array
		+ direct access to all elements.
		+ rapid(const complexity) push and pop from or at end.
	- `deque`
		+ [double-ended queue](https://en.wikipedia.org/wiki/Double-ended_queue)
		+ direct access to all elements.
		+ rapid(const complexity) push and pop from or at front and end.
	- `list`
		+ doubly linked list
		+ rapid(const complexity when privided iterator) insert
	- `forward_list` 
		+ singly linked list
		+ rapid(const complexity when privided iterator) insert
		+ only in C++11
- Ordered associative containers
	- `set`
		+ rapidly lookup (`lb(size)`)
		+ no duplication
	- `multiset`
	- `map`
		+ one-to-one mapping
		+ no duplication allowed
		+ rapid key-based lookup (`lb(size)`)
- Unordered associative containers:
	(Items are stored in _key-value pairs_)
	- `unordered_set`
	- `unordered_multiset`
	- `unordered_map`
	- `unordered_multimap`
- Container adapters
	- `stack`: LIFO
	- `queue`: FIFO
	- `priorty_queue`: HEFO, highest priority element first out

These containers are defined in headers named after the names of the container.

Ordered comtainers manage items in _key-value paairs_ and (in C++11) keys 
are _immutable_. The sequence containers and associative containers are 
commonly referred as _first-class_ containers.

`stack`, `queue` and `priorty_queue` can be implied as constrained sequence
containers. So they are defined as container _adapters_, rather than 
_containers_.

## Near containers
C++ also has some _near containers_, i.e. those objects has _some_, but not
all features of containers. Some typical near containers are:
- normal array (not the array containers)
- `bitset`s
- `valarray`s: perform high-speed 
	[vector](https://en.wikipedia.org/wiki/Euclidean_vector)(not `vector`
	container calculation

## Basic requirements for elements in containers
When added to container, an element is _copied_ into that container, thus,
it must have a copy constructor, and (possibly) need to have a assignment 
operator. In _ordered_ associative containers, and many algorithms require
elements to be _comparable_, i.e. they should provide _less-than_ and 
_equality_ operators. In C++11, objects can also be _moved_ into container
elements, in which case, a _move_ constructor is needed.


## Define An Instance

```c++
std::array<int,4> arr{ 1, 2, 3, 4 };
std::vector<int> vec;
```


## Methods
	
Go to the reference page....
They are containers. Thus, they have `begin()`, `end()`, `size()`, 
`max_size()`, `empty()`, and `swap()` methods. Another important method is 
`reserve`.


# Iterators
They are similar to pointers and used to point to first-class container.
Iterators holds information sensitive to their type of container.

STL containers provides member function `begin()` and `end()`, which provide
iterators point to the start and the end(which DNE) of the container.

## Category & Hierarchy of iterators

	+----------+
	|  Input   <-+  +----------+   +-----------+    +-----------+
	+----------+ |  |          |   |           |    |           |
	             +--+  Forward <---+Bidirection<----+  Random   |
	+----------+ |  |          |   |           |    |   Access  |
	|  Output  <-+  +----------+   +-----------+    +-----------+
	+----------+

- Input: for sequential input operation, and does not need to be able to 
	go backward. 
- Output: for sequential output operation, and does not need to be able to 
	go backward. 
- Forward: can be used to access the sequence of elements in a range in the
	direction that goes from its beginning towards its end.
- Bidirection: can go backward.
- Random Access: can access any elements in constant time.

The following first-class containers support random access iterator: 
- `array`
- `vector`
- `deque`
And the following support bidirection iterators:
- `list`
- `set`
- `multiset`
- `map`
- `multimap`

### Predefined type of iterators 
- `iterator`
- `const_iterator`: using non-const iterator to point to const container 
	will cause compiling error. 
- `reverse_iterator`
- `const_reverse_iterator`


## `istream_iterator` and `ostream_iterator`
```c++
#include <iterator>
#include <climits>
#include <string>
#include <iostream>

int main () {
	using namespace std;
	istream_iterator<int> ii(cin);
	ostream_iterator<int> oi(cout);

	int i = INT_MAX;
	string s;
	while (i != 0) {
		i = *ii;
		// the next int will be read right now and temporately stored
		// for object, pre-increment should be preferred, because it does not 
		// create temporary object 
		++ii;
		getline(cin, s);
		*oi = i;
		++oi;
		cout << "string is: " << s << endl;
	}

	return 0;
}
```

`copy` can be used to output a whole container

# `algorithm`
The algorithm STL only operate on containers elements by iterator, and 
certain algorithms needs certain iterators 
[more information](http://en.cppreference.com/w/cpp/header/algorithm)


# Function object
function object and function are called _functor_, function in 
<algorithm> that can receive funcion object can also receive function.


# `string` Class
[Reference](http://en.cppreference.com/w/cpp/string/basic_string)

definition:

```c++
typedef basic_string<char> string;
```

Usage

```c++
#include <string>
 
...

string hello = "hello";
// (almost) the same as:
string hello("hello");
/* note that "=" in definition is not assignment
 */
// string hello = 22 		// not allowed
// string hello = '0' 	// not allowed
// however, it has an assign operator with char parameter
hello = '2';			// allowed
```

__NOTE:__ (_before C++11) elements stored in string do not necessarily  
be terminated by `'\0'`.

## Important Concepts & Methods 

### Length, Capacity and Max_size
(see the test program `string_1_size.cpp` and `string_2_resize.cpp`)

- `size()` and `length()`, which have the same function,
- `capacity()`
- `max_size()`

### Convert to C-string

`npos`: no position, which has some special usage

```c++
string str = "String";
char *cstr[BUF_SIZE];

// use .copy() to copy to cstring
str.copy(cstr, size(), 0);
// or
str.copy(cstr, npos);

// return a non-modifiable string
char *cstr2 = str.c_str();
// or 
const char *cstr3 = str.data()
char *cstr4 = str.data()					// since c++11
```
__NOTE:__ `cstr2` and `cstr3` is not guaranteed to be valid if operation 
possibly leading data address of `str` to be modified modified carried 
out. And changing contents by `cstr2` and `cstr3` is undefined. 

### Find substring / character

### Replace contents

```c++
clear()
insert()
erase()
push_back()
pop_back()
append
operator +=
replace
```

### Other Important methods

```c++
.empty()
.substr(start, end)
.substr(start)
operator[]
operator > == < 
substr();
.at()
```

**NOTE:** `.at()` provides *bounds checking* for `string`, but `operator []` 
does not.


## Iterators

`string` provides iterators with almost the same operators as pointers.

```c++
string::const_iterator it = str.begin();
// cout << it;					// not allowed
while(it < length)  {
	cout << *it++;
}
```

## String stream

```c++
#include <string>
#include <iostream>
#include <sstream>

...

istringstream is;
is.str("sdfgjkl");		// or just istringstream is("sdfghjk");
ostringstream os;
call str
```
[see example](http://en.cppreference.com/w/cpp/io/basic_istringstream/str)


# Bitset
(It can be used like int and also an array)[http://en.cppreference.com/w/cpp/utility/bitset]

# Other things:
```c++
typename vector<T>::const_iterator ci;
```
Use this syntax to indicate that `vector<T>::const_iterator` is a name of 
type, rather than a static member.
