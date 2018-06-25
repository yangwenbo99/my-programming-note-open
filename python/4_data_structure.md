
<!-- vim-markdown-toc GFM -->

1. [Namespace, its life-time and scope](#namespace-its-life-time-and-scope)
1. [List](#list)
	1. [List Comprehensions](#list-comprehensions)
		1. [Nested List Comprehensions](#nested-list-comprehensions)
1. [Tuple](#tuple)
1. [set](#set)
1. [Dictionary](#dictionary)
1. [Classes](#classes)
	1. [Definition and instantiation](#definition-and-instantiation)
	1. [Remarks of naming](#remarks-of-naming)
	1. [Inheritance](#inheritance)
		1. [Multiple inheritance](#multiple-inheritance)
		1. ["Private"](#private)
		1. [Odds and Ends](#odds-and-ends)
		1. [Iterators](#iterators)
			1. [Generators](#generators)
				1. [Generator Expressions](#generator-expressions)
		1. [Customlization and Operator Overload](#customlization-and-operator-overload)

<!-- vim-markdown-toc -->

# Namespace, its life-time and scope

__Life time of name__
- Built-in: __removed before publishing__
- Global (for a module): __removed before publishing__ 
- `__main__` namespace, the statements read from a script or read from 
	`<stdin>`
- Local space of a function:__removed before publishing__

__Scope and search__

	+---------------------------------+  ^^
	|   The outermost scope, which    |  ||
	|   contains built-in names       |  ||
	|                                 |  ||
	|  +---------------------------+  |  ||
	|  |   "Next to last" scope,   |  |  ||
	|  |   containg the module's   |  |  ||
	|  |   global names            |  |  ||
	|  |                           |  |  ||
	|  |  +---------------------+  |  |  ||
	|  |  |    Enclosing fun-   |  |  |  || Searched from
	|  |  |    ction, which     |  |  |  || inside to
	|  |  |    is   not local   |  |  |  || outside
	|  |  |    and not global   |  |  |  ||
	|  |  |    scope            |  |  |  ||
	|  |  |                     |  |  |  ||
	|  |  |  +---------------+  |  |  |  ||
	|  |  |  |               |  |  |  |  ||
	|  |  |  |  Local names  |  |  |  |  ||
	|  |  |  +---------------+  |  |  |  ||
	|  |  +---------------------+  |  |  ||
	|  +---------------------------+  |  ||
	+---------------------------------+  ++

For Python, it is important to know that "scopes are determined _textually_"
i.e. the object referred by names called in a function is determined in the 
context where the function _defines_, rather than where the function called
and regardless of how the function called (by its own name or by alias).

For Python, if no `global` statement is used, assignments always go to 
local variables. Everything will operate on _local_ things by default...

The `global` statement can be used to indicate that a particular variable 
live in the global scope, and should be _bound_ there; the `nonlocal` 
statement indicates that it should be _bound_ to enclosing scope...
# List
__code removed before publishing__

- `append(x)`
- `extend(iterable)`
	- Equivalent to `a[len(a):] = iterable`
- `insert(x)`
- `remove(x)`
- `pop([i])`
	- if `i` not given, pop the last item
- `clear`
- `index(x[, start[, end]])`
	- Return zero-based index to the first item found, if not found, raise 
	  ValueError 
- `count(x)`
- `sort(key=None, reverse=False)`
- `reverse()`
- `copy()`: return a copy

## List Comprehensions
List comprehensions provide a concise way to create lists.

Refer to <https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions>.

List comprehension provides a concise way of "comprehending", i.e. 
generating a new list.

__removed before publishing__

### Nested List Comprehensions
__removed before publishing__

However, built-in functions should be preferred.....
```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```


# Tuple
Tuple is _unchangeable_.

__removed before publishing__

# set
__removed before publishing__

# Dictionary
__removed before publishing__

# Classes

- Normally class members are _public_, 
- all member functions are _virtual_
- classes themselves are objects
- built-in types can be used as base classes
- operator overloading is supported

- Objects can have _alias_, i.e. they are generally passed by reference.
	For small and immutable object, this can be ignored, but for large ones, 
	its significant...

## Definition and instantiation
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Class definitions, like function definitions (`def`), must be executed 
before they have effect.

When a class definition finish normally, a _class object_ is created.

- function (methods) inside class definition, 
- other things inside definition

(refer to <https://docs.python.org/3.6/tutorial/classes.html>)
__removed before publishing__


__Class instantiation__
Class _instantiation_ uses function notation, just:
```python
x = MyClass()
```

Interesting thing, but corresponded to python philosophy: when variable of 
immutable object is reassigned, new object is created.
```python
>>> x.i
12345
>>> x.i = 2333
>>> x.i
2333
>>> MyClass.i
12345
>>> MyClass.i = 2345678
>>> x.i
2333
>>> y = MyClass()
>>> y.i
2345678
>>> MyClass.i=898989898
>>> y.i
898989898
```

When a class is instantiated, its `__init__()` attribute will be called, 
if defined.
```python
def __init__(self):
    self.data = []
```


__Method Object__

`x.f` is not the same thing as `MyClass.f`; `x.f` is _method_ object, and 
`MyClass.f` is a function object.
```python
>>> def g(self):
...     print("God-bye world")
... 
>>> x.f = g
>>> x.f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: g() missing 1 required positional argument: 'self'
```

`x.f()` calls the `f` attribute of `x`, however, it is not necessary to 
call `x.f()`:

```python
class MyClass:
    def __init__(self):
        self._count_ = 0
    def count(self):
        self._count_ += 1
        return self._count_

x = MyClass()
xcount = x.count;
while (xcount() < 3):
    print(x._count_)
```

Output:
```
1
2
```

Very often, `x.f(...)` is equivalent to `MyClass.f(x, ...)`.

## Remarks of naming 

To prevent name of method attributes from having the same name as data
attributes, the following methods can be used:
- Capitalizing method names,
- Prefixing or postfixing an underscore (or other unique string) after a 
	data attributes.
- Using verb for method and noun for data attributes

It is almost _impossible_ for python to do data hiding, thus, client must
be careful when using data attributes. Also, unlike C++ or Java, There is 
no shorthand for referencing data attributes (or other methods!) from 
within methods. As it is a convention, the first argument of a function 
attribute should always `self`.

## Inheritance

Python, of course, support inheritance...

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

__NOTE__: method of base class may call a method of a derived class, 
because all methods in Python are _virtual_, in the words of C++.
But how to ensure method of base class being executed? In C++, we use
`BaseClass::method(...)`, but in python, it is even straight forward,
`BaseClass.method(self, ...)`

`isinstance(object, Class)` can be used to check whether one object is 
an instance of `Class` or its subclass.
`issubclass(Class, info)` can be used to check whether one class is an 
subclass of come other class(es). (A class is considered as a subclass of
itself) If `info` is a tuple of classes, this function will return true
iff `Class` is a subclass of one of members of `info`.

### Multiple inheritance
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

`super()` can be used to access attributes, especially class data 
attributes. It is searched under `__mro__` attribute, and the default
`__mro__` generating mechanism can be express using the following pseudo
code:

```python
def gen_mro(classname):
	if classname = object:
		return [object]
	res = []
	for i in classname.parents:
		res[len(res):len(res)] = gen_mro(i)[:-1]
	res.delete_multiple()
	rearrange res, so that all super classes are put behind its subclass(es)
	res[0:0] = [classname]
	return res
```
This is different from C++. 

The methods of a subclass are searched based on the order in `__mro__`
(method resolution order) Python uses this way to handle _diamond 
relationship_ properly.

### "Private"
In Python, nothing is private, but, but it has some conventions (__removed before publishing__).

Followings are from <https://docs.python.org/3.6/tutorial/classes.html>.

Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

__code removed before publishing__

### Odds and Ends
From <https://docs.python.org/3.6/tutorial/classes.html>

Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, __removed before publishing__

### Iterators
`iter(var)` will return the same result as `var.__iter__()`, which should 
be an iterator, that _iterates_ elements of a class. `next(it)` is 
equivalent to `it.__next__()`, which return the next object in the container
or raise a `StopIteration` exception, which indicates the end of iteration.
Objects that iterable are capable to be used by `for` loop.

#### Generators
__code removed before publishing__

When `yield` executed, it will get one elements and "freeze" after this
statement, the execution will continue, if one yield met, it will "freeze"
again, and if the function finish, it will just raise `StopIteration`.

##### Generator Expressions
__code removed before publishing__
```

### Customlization and Operator Overload
<https://docs.python.org/3/reference/datamodel.html>
