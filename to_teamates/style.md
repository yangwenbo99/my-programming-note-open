# Style

Because we are going to work together, we need to reach a consensus in writing code. I am OK for any coding style, once it keeps enough and appropriate blank space. 

If you want us to use your coding style, please provides it, just in the same way of the following presentation. 

## Example Style Guide

This is a modified version of Google Java Style Guide.
<http://google.github.io/styleguide/javaguide.html#s1-introduction>

### Introduction

#### Terminologies
In this document, unless otherwise clarified:

1. The term class is used inclusively to mean an "ordinary" class, enum class, interface or annotation type (`@interface`).
2. The term member (of a class) is used inclusively to mean a nested class, field, method, or constructor; that is, all top-level contents of a class except initializers and comments.
3. The term comment always refers to implementation comments. We do not use the phrase "documentation comments", instead using the common term "Javadoc."

Other "terminology notes" will appear occasionally throughout the document.

#### Guide notes

Example code in this document is _non-normative_. That is, while the examples are in Google Style, they may not illustrate the _only_ stylish way to represent the code. Optional formatting choices made in examples should not be enforced as rules.

### Source file Basic

#### File name

The source file name consists of the case-sensitive name of the top-level class it contains (of which there is exactly one), plus the `.java` extension. The only exception is that a small class can be put in the same file in an other top level class

#### File encoding

All files should be encoded in **UTF-8**, but non-ascii characters should only be allowed in string content and (occasionally) comments.

#### Special characters


