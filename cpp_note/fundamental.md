# Table of Contents
<!-- vim-markdown-toc GitLab -->

1. [New to C++](#new-to-c)
	1. [Tokens](#tokens)
	1. [type](#type)
	1. [overflow (underflow)](#overflow-underflow)
	1. [type conversion](#type-conversion)
	1. [*new* and *delete* operator](#new-and-delete-operator)
	1. [Range based for loop](#range-based-for-loop)
	1. [IO](#io)
		1. [cin](#cin)
			1. [get](#get)
			1. [detect ending](#detect-ending)
		1. [EOF](#eof)
		1. [File IO](#file-io)
			1. [open](#open)
			1. [methods](#methods)
			1. [copy one file to other file](#copy-one-file-to-other-file)
	1. [Differences in functions](#differences-in-functions)
		1. [Function prototype](#function-prototype)
	1. [`string` type](#string-type)
	1. [Recusion of `main ()` function](#recusion-of-main-function)
	1. [Reference](#reference)
1. [Terms](#terms)
1. [MEMOs](#memos)

<!-- vim-markdown-toc -->


# New to C++
## Tokens

- keywords
- identifiers
- string constants
- numeric constants
- operators
- punctuators
		
	identifiers give *unique* name to certain catagory of identifiers

## type

### Fundamental type

	singed/unsigned

	char
	short
	int 
	long
	(etc)
	bool
	wchar_t
	float
	double
	long double


	&, *, []

Following section is from c++ standard draft 4659.

#### bool

`bool` can only hold `0` and `1`.

#### _cv_ `void*`

This is the formal name of most `void *`.

#### `std::nullptr_t`

Value of this type should only be a null pointer constant, and `sizeof(std::nullptr_t)`
shall be equal to `sizeof(void *)`

### Compound Type

- _arrays_ of objects of a given type
- _functions_, which have parameters of given type and return `void` or reference 
	or a given type
- _pointers_ to _cv_ `void` or objects (here means every type) or functions (including
	static members of classes, but not necessarily including non-static members of a class)
- _references_ to objects or functions of a given type. There are two types of reference:
	+ _lvalue reference_
	+ _rvalue reference_
-	_pointers to non-static class members_
-	_classes_
-	_unions_
-	_enumerations_

#### Reference

1. There shall be no references to reference, no arrays of references, and no pointers
	to references.
2. The declaration of reference should contain an initializer, unless the definition 
	contains an explicit `extern` specifier, is a class member or is the declaration of a 
	parameter or a return type.
	- a null reference should not exist in a well-designed program. The only way to get it
		is by `T &r = ((T *) nullptr)`.
	- a reference cannot be bound directly to a bit-field.
3. If a _typedef-name_ or a _decltype-specifier_ denotes a type `TR` which is a 
	reference to a type T, an attempt to create the type "lvalue reference to _cv_ `TR`" 
	creates "lvalue reference to T", and attempt to create the type "rvalue reference to 
	_cv_ `TR`" creates the type TR. (__reference collapsing__)

	struct / class
	union
	enum
	typedef
	*template*

#### _cv_

_cv_ stands for any subset of the following set, including empty set.

	{volatile, const}


## overflow (underflow)
c++ never inform you

## type conversion
Both `(int) l` or `int(l)` are allowed, however, the later is preferred.

## `new` and `delete` operator

	int *p = new int;
	delete p;			// allowed
	delete p;			// this time, not allowed
	p = null;
	delete p;			// allowed

	int *p = new int [10];
	delete [] p;		// free the whole array, but not only p[0]

### Initialization

```c++
int *p = new int(6);		// (ONLY IN C++11)
struct coordinate {
	double x;
	double y;
	double z;
};
coordinate *p = new coordinate {1, 2, 3}	// only in C++11
we can also use this for int....
int *p = new int [3] {1, 2, 3};			// only in C++11
double *p = new double {2.5};			// only in C++11
```

### When `new` fails:
in ancient time, `null` is returned, 
	now, `std::bad_alloc` is thrown.

### `new` and `delete` operators, function, and replacement function

They should not be directly called, however it's 
good demostration for overloading

	void * operator new (std::size_t);	// new
	void * operator new[] (std::size_t)	// new []
	void operator delete (void *);		// delete p;
	void operator delete[] (void *);	// delete[] p;

	int *p = new int; 		// equivalent to 
	int *p = new(sizeof(int));
	int *pa = new int[40];	// equivalent to
	int *pa = int[] (40*sizeof(int));
	delete p;				// equivalent to 
	delete(p);

### Placement `new`

First, `#include <new>`.

The default placement new do no thing but just return the pointer
sent...... Very useful isn't it? :-D
	- However, it can be overloaded.

	int *pi = new (buffer) int;			// buffer is a pointer
	int *pa = new (buffer) int[50];

## Range based for loop
	double prices[5] = {1.2, 2.3, 4.4, 6.0, 5.5};
	for (double x : prices) {
		x *= 0.8;
	}

## IO
### cin
#### get

	// These functions are members of istream
	// They demostrated "function overloading"
	// as shown, most of these function return the same object 
	// that it belongs to

#### detect ending

	cin.eof();		
		// return true, if EOF detected, otherwise, false
	cin.fail();
		// return true, if the latest reading failed, otherwise, false
	if EOF detected, cin.clear() must be used, or nothing can be read.
	c = cin.get(); 	// this can get an EOF
	cin.get(c)		// this can't get an EOF

### EOF

- In Unix, as well-known, <C-d> simulated EOF
- In Windows, press <C-z>, then <CR>

### File IO

	#include <fstream>
	ifstream, ofstream

#### open

	.open(file, [mode]);

modes:
- app			(append)
- binary		(binary mode)
- in 			(reading)
- out 			(writing)
- trunc	(discard contents of the stream when opening)
- ate:	(seek to end of stream immediately after open)

#### methods

	.is_open();
	.good();
	.open(char *);
	.eof();
	.fial();

#### copy one file to other file

	while (if.good() && of.good()) {
		if >> buff;
		of << buff;
		// this will "ensure" the program will read the last record
		// twice
	}
	while (of.good()) {
		if >> buff;
		if (!if.good())
			break;
		of << buff;
	}
	// or just
	while ((if >> buff) && of) {
		// use implicit conversion from stream to bool (C++11) 
		// though less line, but somewhat not preferred
		of << buff;
	}
	

## Differences in functions
### Function prototype
Function prototype is __composary__ for functions that need to be used 
before definition. Looking at the follwing code:

```c++
void say_hi ();
	// have different meaning in C and C++
	// In C: a function with return type void, but unspecified
	//     parameters 
	// In C++: a function with return type void and no parameter.
void say_hi (void);
	// good in both C and C++
	// a function with return type void and no parameter.
void say_hi (...);
	// not good in C, because in C it means variable parameters
	// but OK in C++, in C++ it means unspecified parameters
```

In C, prototype is optional, if not given, the compiler will guess
the definition using the first time it's called...... Though, sometimes 
it maybe wrong. C++ provides a *"simple"* but  *"decent"* solution by 
simply prohibiting doing so, and make prototype compulsory...... 

	int main (void) {
		int a, b, c;
		...
		my_function(a, b, c);
		/* C compiler will guess the prototype is:
		 *     int my_function(int, int, int);
		 */
		...
	}
	/* but it's possible that: */
	double my_function (int a, double b, float c);

## `string` type

string is like struct rather than char[].

	string a = "I'm a.";
	string b = a; 	//allowed

in object string, conversion to and from char* is defined, so it's OK to
directly use string to take the place of char* and the reverse

## Recusion of `main ()` function 

In C, main() can call itself, but in C++, not allowed...

## Reference

	int &r = a;
	// reference variable should be initialled when defining 
	// r is the same as a
	void f (int &x)
	// const reference is preferred for structure
	double f(My_struct const &a)

Some important points:

1. NEVER pass a expression other than a single variable to a function using 
  non-const reference

		double f(int const &a);
		f(++i);
		what should it do?

2. temporary variables
	C++ can automatically generate temporary variables when the argument
	does not match a reference argument. But in modern C++, it is only
	allowed when it's a const reference.

	The compiler will generate a temporary variable, when:

	1. the actual argument is the correct type, but not *lvalue*, or
	1. the actual argument is not the correct type, but can be
		 converted into correct type

	In old-style C (even before *const* was introduced), *lvalue* means entities that can be put on the left of an assignment statement.  However, in C++ (after *conse* being introduced), it means the variable that can be accessed by dereferencing it address. And *lvalue* can be classified as *modifiable lvalue* and *non-modifiable lvalue*

	*literal constants (except string) are NON-lvalues. *

3. *Rvalue reference*

		double && rref = std::sqrt(36.0);

4. reference as return value

		My_struct & my_function (const My_struct & s) {
			......
			return s;
		}
	This is OK, it just return `s`.
	However, ONLY RETURN THE VARIABLES THAT WILL EXIST AFTER THE END OF
	THE FUNCTION. 
		My_struct & my_function (const My_struct & s) {
			int a;
			......
			return a;	// 會死儂兮 (WRONG)
		}

	- if you use *new* remember to *delete* it.
	
5. use *const* for returning referencing value:
		const My_struct & my_function (const My_struct & s) {
			......
			return s;
		}
	unless, you can tolerate the stupid thing:
		my_function(s1) = s2;
			
	variables created in a function with "new" will be kept after the
	execution of the function.



# Terms
In C++ (and many other language), 
- *parameter*s means the formal parameter, i.e. the parameters passed
	to the function, and 
- *argument*s means the actual parameter (argument), i.e. the
	arguments passed to the function

# MEMOs
1. 
	in the following function:

		int my_fun (int arr[]);

	if I want to make arr (but not arr[i]) a const, then, I have to
	write: 

		int my_fun (int (const arr)[]);
2. 
	though, c++ allow allocating space dynamically using simple
	expression, but the following is not allowed:

		int p[] = new int [a];

	but, the following is allowed:

		int * p = new int [a];

3. use auto and typedef to simplify the code;
	look at the terrible function:

		void *my_function (const int *a, int * const b, 
			int const (const *arr)[], 
			int (*callback) (const int, const int));

	啊恭喜恭喜恭喜你啊
	when defining a pointer to my_function:

		(void *) (*p) (const int*, int * const, int const * const,
			(int *)(const int, const int));

	or:
		auto *p = &my_function();

	or: 
		typedef (void *) (*p_my_function) (const int*, int * const, int const * const, (int *)(const int, const int));
		p_my_function p;

4. Inline-function
	A common practice is put all inline-function (including definition and
	declaration) at the place that prototype should be put.
	Inline function can't be recursive....
	And no inline function may not be really inline




