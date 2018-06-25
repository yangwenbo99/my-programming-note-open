
<!-- vim-markdown-toc GFM -->

1. [Topic on Polymorphism](#topic-on-polymorphism)
	1. [Casting](#casting)
		1. [Runtime Type Information (RTTI)](#runtime-type-information-rtti)
			1. [Dynamic casting](#dynamic-casting)
		1. [Other casting](#other-casting)
			1. [`reinterpret_cast`](#reinterpret_cast)
			1. [`static_cast`](#static_cast)
			1. [`const_cast`](#const_cast)
		1. [`typeid`](#typeid)
1. [Template](#template)
	1. [Function Template](#function-template)
	1. [Class Template](#class-template)
		1. [Non-type Parameters & Default types/value to template](#non-type-parameters--default-typesvalue-to-template)
		1. [Explicit specialization](#explicit-specialization)
		1. [Default Types for Class Template](#default-types-for-class-template)

<!-- vim-markdown-toc -->

# Topic on Polymorphism

## Casting
(See the test program: ./casting.cpp) 

C++ has the following casting formats:
- `reinterpret_cast <new_type> (expression)`
- `dynamic_cast <new_type> (expression)`
- `static_cast <new_type> (expression)`
- `const_cast <new_type> (expression)`

**Ques**: will the address of a derived class be the same as the its base class
portion? If not, `(typename *)` casting will be stupid, because casting only convey address. 
[Further information](http://people.scs.carleton.ca/~dehne/projects/cpp-doc/tutorial/tut5-4.html)

### Runtime Type Information (RTTI)

**Runtime type information** enable a program doing down-casting correctly in
complex situation.

#### Dynamic casting
_Apply to pointers and references_.

```c++
derived = dynamic_cast <DerivedClass *> (base_ptr);
/*
 * Return:
 *     nullptr, if fail (not cast-able)
 *     the address of derived class, if success (cast-able)
 */
```

### Other casting
[Many information is from this tutorial](http://people.scs.carleton.ca/~dehne/projects/cpp-doc/tutorial/tut5-4.html)
If a compiler know the pointed object has a base class, it will use the 
portion of that base class for the new pointer. However, if it it doesn't 
know, it will bahave as just copy the value.

#### `reinterpret_cast`

_Apply to pointers_.
For class with multiple base class, this may cause *stupid* effect. 

__removed before publish__

#### `static_cast`

_Apply to pointers_.
__removed before publish__

```c++
double d=3.14159265;
int i = static_cast<int>(d);
```

#### `const_cast`

_This can modify the **constness** of an object_
(Even an object is a const, it's not written in the binary code, and this 
is why `const_cast` is possible)


### `typeid`

[Further information](http://en.cppreference.com/w/cpp/language/typeid)

To use this operator, `<typeinfo>` must be included.

`typeid( )` will return (a `type_info` object containing) type of the object
itself, *regardless of the type of pointer to access that object*. 
Generally, the only useful member of it is method `name()`


# Template

**NOTE:** most compilers requires template to be put in every file using it,
so it's normal that template function is putted in `.h` file.

## Function Template

To define:

```c++
template <typename T>
T swap (T &a, T &b);
// or
template <class T>
T swap (T &a, T &b);
//or
template <typename T, typename U>
T combine(T t, U u);
```

## Class Template

To define template class, every thing need to be put into header file.

```c++
template <typename T>
Class MyClass {
...
	int my_method ();
}
//...
template <typename T>
int MyClass<T>::my_method () {
	...
}
```

To use the class:

```c++
MyClass<int> m;
MyClass<AnOtherClass> m;
```

To declare function manipulating such class:
```c++
template <typename T>
T &do_some_thing (MyClass<T>, T, T);
```

### Non-type Parameters & Default types/value to template

A template may look like this:

```c++
template <typename T, int elements>
// perhaps a array with length elements is created
```

__Note:__ the above class is generated *in compilation time*.

### Explicit specialization

```c++
template <>
class Stack <double> {...}
```

When used this, templated methods cannot be used.

### Default Types for Class Template

```c++
template <typename T = std::string, int elements>
// perhaps a array with length elements is created
```

