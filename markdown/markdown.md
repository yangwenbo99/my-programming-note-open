
<!-- vim-markdown-toc GFM -->

1. [Basic syntax](#basic-syntax)
	1. [Header](#header)
	1. [Block Quotes](#block-quotes)
	1. [Lists](#lists)
	1. [Code Block](#code-block)
	1. [Horizontal Rulers](#horizontal-rulers)
1. [Span elements](#span-elements)
	1. [Links](#links)
		1. [Inline link](#inline-link)
		1. [reference](#reference)
		1. [automatic links](#automatic-links)
	1. [Emphasis](#emphasis)
	1. [code](#code)
	1. [Images](#images)
	1. [Backslash Escape](#backslash-escape)

<!-- vim-markdown-toc -->

# Basic syntax #
## Header ##
Markdown supports two style of headers, Setext and atx.
For settext:

	+----------------------------------------------+
	| This is an H1                                |
	| =========================================    |
	|                                              |
	| This is an H2                                |
	| -----------------------------------------    |
	+----------------------------------------------+

For atx-style:

	+----------------------------------------------+
	| # This is an H1
	| ## This is an H2
	| ###### This is an H6
	| # This is an H1 #
	| ## This is an H2 ##
	| ### This is an H3 ######
	+----------------------------------------------+

## Block Quotes #
Markdown use email style ">" characters

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.
	
Markdowm also allows only put one ">" sign.

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

It can also be nested, and include heading list, and code blocks
> The first level
> ## a header
>
> 1. fist item
> 2. second item
>
> > The second level
>
> The first again.

## Lists ##

Markdowm supports ordered (numbered) and unordered (bulleted) lists

Unordered:
* Red
* Green
* Blue


+ Red
+ Green 
+ Blue

or

- Red 
- Green
- Blue

Ordered:
1. C
2. C++
3. Java
8. Python
2. Javascript
	1. second
	1. third

Note that the numbered used in md file has no effect in the number in html 
output.

- a list item
- this is with quote block

	> quote
	> quote

- and this is with code block:

		#include <stdio.h>
		int main (void) {
			return 0;
		}

	- note that it should be indented twice

And if Lin-pe don't want a list.  To display:
- 1986\. IJIJ

write:

	1986\. IJIJ

## Code Block ##

Just indent it......

	#include <stdio.h>
	int main (void) {
		return 0;
	}

## Horizontal Rulers ##

Use one of the following to produce it

	****
	* * * 
	*  *  * 
	--------

Just like this:

-  -  -  - 


# Span elements #

## Links ##

Markdown supports 2 kind of links:
- inline
- reference

### Inline link ###

Use:

	This is [an example](http://example.com/ "Title") inline link.

	[This link](http://example.net/) has no title attribute.

To produce:

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

	<p>This is <a href="http://example.com/" title="Title">
	an example</a> inline link.</p>

	<p><a href="http://example.net/">This link</a> has no
	title attribute.</p>

Or use local source:

	See [vim-markdown's readme file for more information](/help/)

### reference ###
	
	This is [an example][foo] reference-style link.
	or
	This is [an example] [foo] reference-style link.

And, write one of the following at somewhere else:

	[foo]: http://example.com/  "Optional Title Here"
	[foo]: http://example.com/  'Optional Title Here'
	[foo]: http://example.com/  (Optional Title Here)
	[foo]: <http://example.com/>  (Optional Title Here)

Note that link id is *case insensitive*!

### automatic links ###

Learn this from <https://daringfireball.net/projects/markdown/syntax#blockquote>

	<https://daringfireball.net/projects/markdown/syntax#blockquote>

And it also support email! <yangwenbo99@gmail.com>

## Emphasis ##

Single `*` or `_` will be treated as `<em>`, and double will be treated as 
`<strong>`.

## Code ##

To indicate a span of code, `wrap it with backtick quotes` (\`)
``To include multiple backtick quote in a code span, use multiple ` ``


    Indent to write code

```
Or use ``` for code blocks
```

```c
// optionally, you can add language abbreviation after ``` for highlight
int main (void) {
    return 0;
}
```

## Images ##

Amazing, isn't it........

	![Alt text](/path/to/img.jpg)
	![Alt text](/path/to/img.jpg "Optional title")

Or use reference style

## Backslash Escape ##

Use `\*this to escape *`. Markdown allow you, but not require you to use the 
following escapes, you only need it when it will create other meaning.

	\   backslash
	`   backtick
	*   asterisk
	_   underscore
	{}  curly braces
	[]  square brackets
	()  parentheses
	#   hash mark
	+   plus sign
	-   minus sign (hyphen)
	.   dot
	!   exclamation mark



