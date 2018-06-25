
# Exception handling

C++'s exception handing features enable users to write *robust* and 
*fault-tolerant program* easier. Exception handling grammar makes error 
handling code simpler and clearer.

## Grammar
[Some codes are from wikibooks.](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Exception_Handling)

```c++
void AFunction()
{
    // This function does not return normally, 
    // instead execution will resume at a catch block.
    // The thrown object is in this case of the type char const*,
    // i.e. it is a C-style string. More usually, exception
    // objects are of class type.
    throw "This is an exception!"; 
}

void AnotherFunction()
{
    // To catch exceptions, you first have to introduce
    // a try block via " try { ... } ". Then multiple catch
    // blocks can follow the try block.
    // " try { ... } catch(type 1) { ... } catch(type 2) { ... }"
    try 
    {
        AFunction();
       // Because the function throws an exception,
       // the rest of the code in this block will not
       // be executed
    }
    catch(char const* pch)  // This catch block 
                            // will react on exceptions
                            // of type char const*
    {
        // Execution will resume here.
        // You can handle the exception here.
    }
               // As can be seen
    catch(...) // The ellipsis indicates that this
               // block will catch exceptions of any type. 
    {
       // In this example, this block will not be executed,
       // because the preceding catch block is chosen to 
       // handle the exception.
    }
}
```

The `catch` block  should be _right_ after `try ` block. If the object (defined
in standard) type match the type in `catch`, or is the derived class of that 
type, then the block will be execute. A `catch` block can have one optional 
variable name, which can be used to identify the exception in the `catch` 
block.

__NOTE:__ It is logic error to catch the same type twice.

C++ use the __termination model of exception handling__, rather than __sumption
model of exception handling__, meaning the code in `try` block after **throw
point** will not be resumed after `catch`ed.
"stack unwilling"

### `exception` class

In general, (derived class of) `exception` class should be used for exception 
handling. C++ language defines a 
[list of build-in exceptions](http://en.cppreference.com/w/cpp/error/exception)
which maybe directly used or be used as base class for user-defined exceptions.
A typical user defined exception only has a constructor:

```c++
class MyException : public domain_error {
public:
	MyException (const std::string &what_arg = "Lead to 0 denominator!") 
		: domain_error(what_arg) {}
}
```

However, every type can be thrown:

```c++
throw 5;
throw Object();
```
__NOTE:__
1. `throw x>0 ? 5; 5.3;` will always be double (because ofimplicit type 
	transform)
2. A function often have "error" should use return value to indicate error, 
	rather than throw exception. because that should not be consedered as 
	_exception_.

### Handing procedure
1. If an exception is thrown in a function (outside `catch` and `try`), the
	function will be terminated and go back to the caller. 
2. If a function received a exception from a callee, it is as if the same 
	exception is thrown in the same function, at the place calling the callee.
3. If an exception is thrown in `try` block, the execution point will go to 
	corresponding `catch`, if it has. If not (_stack unwiding_), the program
	will behave as if the exception is thrown _right_ outside the `try` and 
	`catch` blocks.
4. If an exception is thrown in `catch` block, grammar `throw;` can be used
	rather than `throw expression;`, if the exception to thrown is the same
	as caught exception.

When `thrown expression` is used, the program will copy-initialize the 
exception object (or use
[_move constructor_](http://en.cppreference.com/w/cpp/language/move_constructor) 
for rvalue), after that, the expression is a *lvalue* which will exist until 
the termination of last `catch` clause (if it is not re-thrown).

## Exception safety
[Most of this part is from wikibooks.](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Exception_Handling)
A piece of code is said to be exception-safe, if run-time failures within the code will not produce ill effects, such as memory leaks, garbled stored data, or invalid output. It has multiple levels:
1. __Failure transparency__, also known as the _no throw guarantee_: Operations are guaranteed to succeed and satisfy all requirements even in presence of exceptional situations. If an exception occurs, it will not throw the exception further up. (Best level of exception safety.)
2. __Commit or rollback semantics__, also known as _strong exception_ safety or no-change guarantee: Operations can fail, but failed operations are guaranteed to have no side effects so all data retain original values.
3. __Basic exception safety__: Partial execution of failed operations can cause side effects, but invariants on the state are preserved. Any stored data will contain valid values even if data has different values now from before the exception.
4. __Minimal exception safety__, also known as _no-leak guarantee_: Partial execution of failed operations may store invalid data but will not cause a crash, and no resources get leaked.
5. __No exception safety__: No guarantees are made. (Worst level of exception safety)



If one want to write exception code, the code must be guaranteed to be
_exception-safe_. Consider the following code.

```c++
void g()
{
    throw exception();

  
void f()
{
    int* pI = new int(0);
    g();
		// Ah, Kiong-hi oo. 
		// If exception thrown, the pI will never be delete
    delete pI;
}

int main()
{
    f();
    return 0;
}
```

This code will cause __memory leak__, meaning `pI` will _never_ be delete. Change `f()` to the following may be better:

```c++
void f()
{
    int* pI = new int(0);
		try {
			g();
		} catch (exception e) {
			delete pI;
			throw;
		}
		// Ah, Kiong-hi oo. 
		// If exception thrown, the pI will never be delete
    delete pI;
}
```

However, using a more general type to catch and throw may lead to loss of 
information. See the test program:

```c++
#include <stdexcept>
#include <iostream>

int main () {
	using namespace std;
	try {
		try{
			try {
				throw invalid_argument("No good...");
			} catch (invalid_argument e) {
				cout << e.what() << " thrown, type: " 
					<< typeid(e).name() << endl;
				cout << "Throw again!" << endl;
				throw;
			}
		} catch (logic_error e) {
			cout << e.what() << " thrown, type: " 
				<< typeid(e).name() << endl;
			cout << "Throw again!" << endl;
			throw;
		}
	} catch (exception e) {
		cout << e.what() << " thrown, type: " 
			<< typeid(e).name() << endl;
	}

	return 0;
}
```

Output: 
```
No good... thrown, type: St16invalid_argument
Throw again!
No good... thrown, type: St11logic_error
Throw again!
std::exception thrown, type: St9exception
```

Moreover, no all exception will be caught by `exception e`, because exceptions 
need not to be a derived class of `exception`.
The better way to do so (without losing information) is (form wikibook):
```c++
void f()
{
    int* pI = new int(0);

    try
    {
        g();
    }
    catch (...)
    {
        delete pI;
        throw; // This empty throw re-throws the exception we caught
               // An empty throw can only exist in a catch block
    }

    delete pI;
}
```

### Another way to solve this: `unique_ptr`
This part is not from wikibooks

Go back to the `f()` function:
```c++
void f () {
    unique_ptr<int> pI(new int(0));
    g();
    // delete pI;				// no need to delete (in fact, it cannot be done)
}
```
The `unique_ptr` class will manage a _"unique"_ pointer, which means when the 
destructor of `unique_ptr` is called, it will free the memory that it 
\* **owns** *.  However, when using assignment, copy-constructor, `swap()`, 
`.release()` and `.reset()` the ownership will be lost or transferred, thus, 
if the `unique_ptr` is destructed, the object _originally_ owned by the pointer
will not be freed.

__NOTE:__ There are more _smart pointers_, for more information, read 
[the reference](http://en.cppreference.com/w/cpp/memory);

## Declear A function without throwing an exception

Add an `noexcept` after `)` in both declearation and definition. If `const` is 
presented in that, add `noexcept` after `const`.

## `new` and exception

For the situation, when `new` failed, it will throw a `bad_alloc` exception,
which is defined in `<new>`. For `noexcept` version, use `new(nothrow)`, and 
`nothrow` is a object of type `nothrow_t`.

__NOTE:__ for the situation that the possibility of allocation failure is 
considered ignorable, `new` with exception is better, because the programmer
do not need to consider error, and if the small possibility thing happen, the
program will terminate. For very big allocation, which have high possibility 
of allocation failure, the one with `throw` is not considerably better than
the one without it.

### new_handler

`new_handler`is a (pointer to a) function with this prototype:
```c++
void handler ();
```

A handler typically do (at least) one of the following things:
1. Try to get more free memory,
2. throw an `bad_alloc` exception, or
3. terminate the program (eg. `std::terminate()` or `exit(1)`.

After executing handler function, the control flow return to `new` statement,
and the program will try to allocate the memory again. If the handler is set to
`nullptr`, the default handler (which only throw `bad_alloc`) will be used.

**Example from <http://en.cppreference.com/w/cpp/memory/new/set_new_handler>**

```c++
#include <iostream>
#include <new>
 
void handler()
{
    std::cout << "Memory allocation failed, terminating\n";
    std::set_new_handler(nullptr);
}
 
int main()
{
    std::set_new_handler(handler);
    try {
        while (true) {
            new int[100000000ul];
        }
    } catch (const std::bad_alloc& e) {
        std::cout << e.what() << '\n';
    }
}
```
