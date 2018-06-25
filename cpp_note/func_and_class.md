
<!-- vim-markdown-toc GFM -->

1. [Function](#function)
	1. [Default arguments](#default-arguments)
	1. [Functions](#functions)
		1. [Function signature](#function-signature)
		1. [Overloading](#overloading)
		1. [Generic Programming](#generic-programming)
1. [Namespace](#namespace)
	1. [Scope](#scope)
		1. [Automatic Storage Duration](#automatic-storage-duration)
		1. [Table of storages and their duration](#table-of-storages-and-their-duration)
		1. [one definition rule](#one-definition-rule)
		1. [qualifiers](#qualifiers)
		1. [Language Linking](#language-linking)
	1. [Transitional namespace concept](#transitional-namespace-concept)
	1. [Modern namespace concept](#modern-namespace-concept)
		1. [Unnamed namespace](#unnamed-namespace)
		1. [`using` declaration and `using` directives](#using-declaration-and-using-directives)
1. [Class](#class)
	1. [Declearing and Defining](#declearing-and-defining)
	1. [Special Members ( & methods)](#special-members---methods)
		1. [_Default_ member functions](#default_-member-functions)
			1. [Copy Constructor](#copy-constructor)
			1. [assignment operator](#assignment-operator)
		1. [Constructors and Distructors](#constructors-and-distructors)
			1. [MyClass::MyClass](#myclassmyclass)
			1. [`MyClass::~MyClass`](#myclassmyclass-1)
			1. [const method](#const-method)
			1. [`this` pointer](#this-pointer)
			1. [`enum` with class](#enum-with-class)
				1. [review `enum`](#review-enum)
	1. [Friend](#friend)
	1. [Define a class instance](#define-a-class-instance)
	1. [Overloading operator](#overloading-operator)
		1. [Restrictions](#restrictions)
		1. [Type Conversion](#type-conversion)
			1. [From other type to class type](#from-other-type-to-class-type)
			1. [From class type to other type](#from-class-type-to-other-type)
1. [Good prectice](#good-prectice)

<!-- vim-markdown-toc -->

# Function

## Default arguments

only modify the prototype.

	int my_fun(const char * p, int n =1);
	// the default arguments should start from right to left.

## Functions

### Function signature

if two functions have different number of parameters or have
different number type of parameters, they have different
signature.

However, when checking signature, reference and non-reference are
treated as the same but const and non-const are not treated as the
same.

it's okay to sent pointer to non-const to const, but not vice versa

### Overloading

_Use them wisely_

	char * left (const char * str, unsigned int n);
	char * left (const char * str);
	// not as good as:
	char * left (const char * str, unsigned int n=1);

### Generic Programming
**Definition:** 
	use a general type to substitute more specified type

1. templates
		template <typename T> int my_fun(T a);	// or
		template <class T> int my_fun(T a);
2. Explicit Specialization

		// template prototype
		template <typename T> int my_fun (T a);	
		// explicit specialization
		template <> int my_fun<My_struct> (My_struct a);	// or
		// template <> int my_fun (My_struct a);
		// non template
		int my_fun (My_struct a);

	explicit specialization will override non-explicit, and non-template
	one will overide both 

3. decltype (C11)

		decltype(expression) var;

	1. if *expression* is an unparenthesized identifier, then var is of
	the same type of expression
	2. else, if *expression* is a function call, the compiler will deduce
	the type based on the prototype
	3 .else, if *expression* is an lvalue, then var is a reference;
			decltype((x)) var = y;
			var is the reference of y;
	4. else, the type will be the same as the expression.

4. trailing return type

		double h(int x, int y)
		// can be replaced by
		auto h(int x, int y) -> double

	which will make the following work

		template <typename T1, typename T2>
		auto f(T1 x, T2 y) -> decltype (x+y) {
			///
		}


# Namespace

## Scope
- local scope / block scope
- global scope / file scope
- external scope:
	+ across files
- internal scope:
	+ inside a file
- function prototype scope
	+ only inside a parenthesis
- class scope
- namespace scope
	+ global scope is a special kind of namespace scope

### Automatic Storage Duration
- no linkage
	auto int x;		// not more valid in c++ 11
	register int x;	// deprecated in c++ 11
	static int x = 233;

### Table of storages and their duration
```
+---------------+----------+----------+----------+----------------------+
| Storage       |          |          |          |                      |
|   Description | Duration | Scope    | Linkage  | Declaration          |
+-----------------------------------------------------------------------+
|               |          |          |          |                      |
| Automatic     | Auto     | Block    | None     | In a block           |
+-----------------------------------------------------------------------+
| Static without|          |          |          | *static* inside a    |
|  linkage      | Static   | Block    | None     |  block               |
+-----------------------------------------------------------------------+
| Static with   |          |          |          |                      |
|  external     | Static   | File     | External | Outside all function |
|  linkage      |          |          |          |                      |
+-----------------------------------------------------------------------+
| Static with   |          |          |          |                      |
|  internal     | Static   | FIle     | Internal | Outside all function |
|  linkage      |          |          |          |  with *static*       |
|               |          |          |          |                      |
+---------------+----------+----------+----------+----------------------+
```
	
### one definition rule

A variable can only be decleared once. When declare without defining, use *extern* keyword.

### qualifiers
- storage class quilifiers
	+ auto (not more used)
	+ register
	+ static
	+ extern
	+ thread_local (C++11)
	+ mutable
		* if used in structure or class, this item can be modified
			even if the type of the structure is const.
- CV-qualifier
	+ const
		* by default, const is static internal
	+ volatile
		* this value can change even without modification by this program

### Language Linking

C and C++ have different symbol in  assembly language.......
and people can explicitly specify which style to use.  

```c++
	extern "C" void foo();		// C style
	extern "C++" void bar();	// C++ style
	extern void foobar();		// c++ style
```
## Transitional namespace concept 

- declarative region
- potential scope
- scope

## Modern namespace concept

```c++
// c++ also has a 
namespace mynsp {
	// a name space can be inside another name space, however, it's not
	// allowed to put namespace in functions, blocks, and so on.
	namespace mpnnsp {
	}
}
```
### Unnamed namespace

```c++
namespace {
	...
}
```
When it's used, it's as if the using directive is used. This
provides an alternative way for internal static variables, and is
preferred by C++.


### `using` declaration and `using` directives

```c++
	using std::cin;		// using declaration
	// almost equivalent to *auto &cin = std::cin;*
	// if cin overloaded, all will be included
	using namespace std;	// using directives
	// This one will do in the block as if the identifiers inside the
	// namespace is declared in the smallest region that contain both
	// this statement and the namespace
```

# Class

## Declearing and Defining

in .h file:

```c++
class MyClass {
private:
	int ....
	// only inline function is allowed
	inline int my_inline_function () {
		...
	}
public:
	....
}
```

in .cpp file:

```c++
int MyClass::my_function () {
}
```

## Special Members ( & methods)

### _Default_ member functions

C++ will provides following member functions:

- A default constructor,
	+ if no constructor created,
- A default distructor, 
	+ if no distructor ceated,
	+ will only performs member to member (shalow) disturction!
- A copy constructor
	+ if no copy constructor defined,
	+ will only performs member to member (shalow) cooy!
	+ `MyObj obj1 = obj2;`
	+ (and perhaps) `MyObj obj1 = MyObj(balabala);`
- An assignment operator,
	+ `obj1 = obj2`
- An address operator.

#### Copy Constructor

	it should looks like:

```c++
MyClass (const MyClass &m);
// note that here, it can only be const MyClass & parameter
```

and be used for:

```c++
MyClass m = n;
m = p;
```

#### assignment operator

For the following statement, there are 2 implements spicified
treatements.
```c++
MyClass m = n;
```

1. directly copy n to space ordered by m, or
2. copy n to a tempory space, and assign the unnamed variable to m

### Constructors and Distructors

#### MyClass::MyClass

the program will provide a default constructor iff you do not
define one by yourself.

#### `MyClass::~MyClass`

maybe we need some tools or used `new`, so we have to free it now.

#### const method

if a method promotes not to modify the object, it should be
decleared as const.

```c++
//declaration
void my_method () const;
//definition
void MyClass::my_method () const {...}
```

#### `this` pointer

#### `enum` with class

##### review `enum`

```c++
enum name { enumerator = constexpr , ... };
enum aaa {a, b, c=0, d};	// a==0, b==1, c==0, d==2
// c++11 add more syntax
enum name : type { enumerator = constexpr , 
	enumerator = constexpr , ... };
when used, just 
	enum my_enum = b;		
		// this is why enumerator should not use short name`
		```

##### `enum` as class member

an `enum` placed in class will make it as if enumerators are
class menbers.

	class Stack {
	private:
		enum {MAX = 10};    // constant specific to class
		Item items[MAX];    // holds stack items
		...
	}
	const int iii = Stack::mmmm;	
		// valid, if mmmm is in public suction


##### `class`/`struct` scoped `enum`

in c++11, we can also give enum a class or struct scope

```c++
enum struct|class name { 
	enumerator = constexpr , enumerator = constexpr , ... }
enum struct|class name : type { 
	enumerator = constexpr , enumerator = constexpr , ... }
	```

## Friend


## Define a class instance
```c++
// Declaring
class MyClass {
	...
public:
	friend int my_friend (MyClass &m);
};
// defining
int my_friend (MyClass &m);
```

This will enable my_friend to access the private member of the class

```c++
MyClass a;			// valid, use default constructor
MyClass b(...);		// valid
MyClass c();		// valid as it's some compilers' extra grammar
// but....... with total different meaning!
// this is a *nested function declaration* rather than instance
// definition!!!!
```

## Overloading operator

```c++
class MyClass {
	...
public:
	friend const MyClass & operator+(MyClass &m, MyClass &n);
	MyClass & operator+(MyClass &m) const;
	// both make sense, but the first one better, because with comversion,
	// other type can perform as the first operator to get the result
};
```

### Restrictions

```c++
- Operloaded operators must be valid C++ operator,
- they must be used in valid grammar, 
- the followings can't be overloaded
	+ sizeof
	+ .
	+ .*				// pointer to member
	+ ::
	+ ?:
	+ typeid
	+ const_cast
	+ dynamic_cast
	+ reinterpret_cast
	+ static_cast
- the followings can only be overloaded using member functions
	+ =
	+ ()				// function call
	+ []				// index
	+ ->				
```

### Overloading `++` and `--` Operators

>  To overload the refix and postfix increasement operators, each overloaded
>  operator function must have a distinct signature.

The prefix version is exactly in the same form as other operator. 

```c++
MyClass &operator++();
friend MyClass &operator++(MyClass o);
```

However, the 
postfix one is slightly different. When the compiler see `my_object++`, it will
call `my_object.operator++(0)`. Thus, to have postfix `++` and `--` overloaded, 
just:

```c++
MyClass operator++(int);
// or
friend MyClass operator++(MyClass &o, int);
```

**NOTE:** the prefix one can be defined to return a reference, but the postfix
one generally should return an object. Thus, **_ object with prefix operator 
can be lvalue _**.

### Type Conversion

#### From other type to class type

a constructor with only a parameter will make the following statement
valid:

```c++
MyClass m = 3;
m = 3;
```

But, to make these code no valid (conversion from int to MyClass
should always use explict cast), we can use `explicit` keyword

```c++
explicit MyClass (int i);
```

then, 

```c++
m = 3; 		// invalid, not implict conversion from int to MyClass
m = MyClass(3);	// valid, and most accepted C++ grammar
m = (MyClass) 3;// valid
```

#### From class type to other type

- the conversion function must be a class method,
- the conversion function must not spicify a return type, and
- the conversion function must have no arguments.

		class MyClass {
			...
			operator int () const;
			operator double ();
			...
		}

```c++
// this will makes all the followings possible
MyClass m;
int a = int(m);
int b = double(m);
double c = m;
```

`explicit` can also be used here ONLY in C++11!!!
	

# Good prectice
- prepare some error message for the place that the program should
never reach
- delete will check wether the argument passed is NULL, if so, nothing
done
	- so always Initialize pointer that are not used right away to NULL.
- C++ prinmer plus P677




