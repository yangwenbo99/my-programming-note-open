This file talks about class, its methods and inheritance

<!-- vim-markdown-toc GFM -->

1. [Conceptual Relationship between Classes](#conceptual-relationship-between-classes)
1. [Inheritance](#inheritance)
	1. [Basic Syntax](#basic-syntax)
	1. [`public` `protected` and `private` inheritance](#public-protected-and-private-inheritance)
	1. [Special Methods](#special-methods)
		1. [Constructors](#constructors)
		1. [Copy constructors](#copy-constructors)
		1. [Destructor](#destructor)
		1. [Assignment operators](#assignment-operators)
			1. [`Derived = Derived`](#derived--derived)
			1. [`Derived = Base`](#derived--base)
			1. [Base = Derived](#base--derived)
		1. [`virtual` Method and **ABC**(*abstract base-class*)](#virtual-method-and-abcabstract-base-class)
			1. [But how does it know?](#but-how-does-it-know)
		1. [Friend](#friend)
1. [Composition](#composition)
1. [Friend](#friend-1)
	1. [Declaration as friend](#declaration-as-friend)
	1. [Static Class Member](#static-class-member)

<!-- vim-markdown-toc -->

# Conceptual Relationship between Classes

- A _is-a_ B:
	+ A is a (special kind of) B.
- A _has-a_ B:
	+ A has some properties that can described using B.
- A _is-implemented-as-a_ B:
	+ A use B as its data structure etc.
- A _uses-a_ B:
	+ A need to use a B.

# Inheritance

This implements a *is-a* relationship.

## Basic Syntax

```c++
Class BaseClass {
	...
}
Class DeriveClass : pulic BaseClass {
	...
}
```

## `public` `protected` and `private` inheritance

The table concludes the effects of these type of inheritance. (Body of the table
is its effect of the derived class)

```c++
+-------------+--------------------------------------+
| Base Class  |   Type of Inheritance                |
| Access      +------------+------------+------------+
| Spicifier   |   public   |  protected |  private   |
+----------------------------------------------------+
|             |            |            |            |
|  public     |  public    |  protected |  private   |
|             |            |            |            |
+----------------------------------------------------+
|             |            |            |            |
|  protected  |  protected |  protected |  private   |
|             |            |            |            |
+----------------------------------------------------+
|             | not        | not        | not        |
|  private    | directly   | directly   | directly   |
|             | accessble  | accessble  | accessble  |
+-------------+------------+------------+------------+
```


## Special Methods
### Constructors	

Nearly all derived classes should call base class'
constructor, the way of calling them is using member
initializer syntax:

```c++
Class DeriveClass : pulic BaseClass {
	DeriveClass (...);
}

DeriveClass::DeriveClass (...) : BaseClass (...) {
	...
}
```

If its not called explicitly, the compiler will call the
default constructor implicitly.

### Copy constructors

If not explicitly defined, it will be created as following:
	first, call base-constructor, 
	second, to do member-to-member copy.

### Destructor

After derived classes' destructor, the base classes'
destructor will be called. They should always be virtual

### Assignment operators
It's not inherited, because it need assign more things.
	
#### `Derived = Derived`

the assignment operator of the derived class is used.
the assignment operator of the base class can be used to
assign the base portion of the object

#### `Derived = Base`

a. explicitly defining an operator
	Derived &operator= (const Base &);
b. defining an conversion operator

#### Base = Derived

the assignment operator of the base class is used

### `virtual` Method and **ABC**(*abstract base-class*)

this keyword will make the program execute methods by true
type rather than pointer type 

Constructors should *always* be **non**-virtual.
Destructors should *always* be **virtual**, unless the class would
never be a base class.

NOTE: this only provide convinces for 

```c++
int foo (Base & base) {
	return base.met ();
}
```
but not:
```c++
int bar (Base base) {
	return base.met ();
}
```

#### But how does it know?

The answer is easy. **Vtable**(for *virtual method table*).

### Friend

if a derived class object want to use base-class's friend, just
a cast is enough (and sometime even no cast needed). The
following 2 way of casting are both acceptable:	

```c++
os << (const Base &) hs;
os << dynamic_cast<const Base &> hs;
```

## Multiple inheritance
```c++
class MyClass : public Base1, public Base2{
	MyClass () : public Base1(...), public Base2(...) {};
}
```

__NOTE:__ The base classes' constructors are not called in the order of 
writing, rather they are called in the order of listing in the first line 
of class definition.

Some time the calls may be ambiguous:
```c++
class Base1 {
private:
	int base1_mem_1_;
	int base1_mem_2_;
public:
	int set_mem_1();
	virtual ~Base1();
};
class Base2 {
private:
	int base2_mem_1_;
	int base2_mem_2_;
public:
	int set_mem_1();
	virtual ~Base2();
};

class Derived : public Base1, public Base2 {
public:
	void print();
};
```
When calling `my_obj.set_mem_1()`, without doubt, the compiler will 
definitely complain. However, solving this problem is easy: adding an
_scope resolution operator_.
```c++
my_obj.Base1::set_mem_1();
my_obj.Base1::set_mem_1();
```

If you want to call `set_mem_1()` directly, the derived class must 
_explicitly_ define one. However, 

### Diamond Inheritance

					 +--------------+
					 |              |
					 |   BaseBase   |
					 +-------+------+
									 |
				+----------+---------+
				|                    |
	+-----+------+      +------+-----+
	|            |      |            |
	|  Base1     |      |  Base2     |
	+-----+------+      +------+-----+
				|                    |
				+----------+---------+
									 |
						+------+------+
						|             |
						|  Derived    |
						+-------------+

To prevent derived has two version of protected variables, `BaseBase` must 
make all of them `virtual`. In fact, the better way is to make `Base1` or 
`Base2` pure virtual.

# Composition

This implement a *has-a* or some other relationship.

In code, they are treated the same as fundamental data type. Generally, they
should be initialized using *member initializers*, but can also be 
initialized using transitional way. If they are not explicitly initialized,
the default constructor will be called implicitly, and if they do not have
default constricter, a compiler error will occur.


# Friend

A class can have friend as *standalone function*, *entire class* or *class method*.

## Declaration as friend

```c++
class MyClass1 {
	// friend function
	friend int myFun(MyClass1 m);
	// friend class
	friend class MyClass2;
}
```

**NOTE:** access notions of `private`, `protected` and `public` are *not relevant* to `friend`s. So, the good practice is to place all `friend` declaration first inside a class' definition, rather than precede them with any access specifier. 


## Static Class Member

