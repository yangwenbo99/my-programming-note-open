
<!-- vim-markdown-toc GFM -->

1. [Module](#module)
	1. [Ways of import](#ways-of-import)
	1. [Executing a module as a script](#executing-a-module-as-a-script)
	1. ["Compiled" python module](#compiled-python-module)
	1. [Standard modules](#standard-modules)
	1. [`dir()` function](#dir-function)
1. [Package](#package)

<!-- vim-markdown-toc -->

# Module

[Information about the Python library](https://docs.python.org/3/library/index.html) 

A module is a file containing python definitions, its name is in `__name__`.

## Ways of import

(this paragraph is from 
<https://docs.python.org/3/tutorial/modules.html>)

When a module `my_module` is imported, the interpreter will first search 
.....__removed before publishing__

```python
>>> import my_module
>>> my_module.myfun(2)
>>> myfun = my_module.myfun
>>> myfun(33)
```

The following method does not introduce the module into the local symbol 
table.
```python
>>> from my_module import myfun2, myfun3
>>> myfun2(222)
```

And this way is dangerous:
```python
>>> from fiob import *
```

This can give a module a name in local symbol table that is different from 
its own name
```python
>>> import my_module as mymod 
```

They can be combined......
```python
>>> from my_module import my_function1 as myfun1
```

__NOTE:__ to reimport an module during execution, 
`module_name.reimport(module_name)`

## Executing a module as a script 

If one module is executed as a script, it's `__name__` will be `"__main__"`.

```python
#!/bin/python3

def myfun(n):
    for i in range(n):
        print(i, end=" ")
        print(__name__)

if __name__ == "__main__":
    import sys
    myfun(int(sys.argv[1]))

```

## "Compiled" python module
<https://docs.python.org/3/tutorial/modules.html>

## Standard modules
Refer to <https://docs.python.org/3/library/index.html>

## `dir()` function

It shows names defined by a module

```python
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
```

# Package
<https://docs.python.org/3/tutorial/modules.html>


Not finished....
