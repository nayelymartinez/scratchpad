# Overview

The "Terminology" folder contains terms and vocabulary commonly taught in Algorithm and theory CS courses with an emphasis on Python-oriented code. It includes example files demonstrating the practical application of a term when appropriate. Most, if not all, exampe files are written in either Python or Java.

The remainder of this README document contains the terminology, along with its definition. If there's a term you would like to be added, please email **nayely.e.martinez@gmail.com**.

# Table of Contents
* Polymorphism
* Function overloading
* Function vs. method

# Terms
## Polymorphism

Polymorphism is the ability to present the same interface for different underlying forms (data types).
This can range from implementation specifications from a super class (subtyping) to differing signatures (ad hoc or function overloading).
There are three main types of polymorphism:

1 - ** Ad hoc polymorphism **
Functions with same name can denote different implementations depending on its signature.

Python, as a dynamically typed language, does not generally require overloading functions, since you can pass in optional arguments.
Applicable Languages: Java

2 - ** Subtyping **
(Aka plain polymorphism in OOP programming
Polymorphic behavior allows you to specify common methods that subclasses need on an abstract level, and then hand off to those subclasses to implement.
Applicable Languages: Python, Java

3 - ** Parametric polymorphism **
(Aka plain polymorphism in functional programming)

Functions or datatypes can be written generically so that it can handle values identically without depending on their type.

* Ex. Append() fn that joins two lists can be constructed so as to ignore the type of elements to be added wtihin each list.
