---
tags: sphinx
date: "2025-05-29"
category: "Programming"
---
# Modern C++ Trick and Tips

This came about as a collection of teach moments, so lets put them all together in one place! There are lots of other resources that will go into any of these deeper, I'm trying to show enough here to make each of the patters approachable.

## Lambdas
#### Lambdas as Loops
For custom loop style iterators, where simple ``for`` loops are not possible, we use ``forEachXXX`` style functions which accept a lambda function. For example, here is a demo of a iteration the first 10 prime numbers.

    template <typename Func>
    void forEachPrimeExample(Func& a_func)
    {
        for (int i : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) // a unique iteration pattern that we want to reuse
        {
            a_func(i); // apply the passed function for prime number i
        }
    }

We define a unique pattern for iteration, but the goal is we want to be able to reuse this in multiple contexts and not duplicate code. So this function takes a templated function argument, where as long as the function `a_func` has a signature that looks like `a_func(int)` this will be valid code. For future use, we can very compactly use this as a loop using a lambda function like so
    
    forEachPrimeExample(
        [&] (int prime) // start the lambda, capture surrounding variables by reference, operate on an input int
            {
                // this is the loop interior, where "prime" is our loop invariant
                std::cout << "iterating over prime " << prime << std::endl;
                // .... do more things with variable "prime"
            } // end of the lambda, or the "loop interior" 
    ); // end forEach function call


## Templates
In C++ say I want to write a function that works on a generic argument type. For example, compute the square of a number. I could write a specific function for any numeric type: int, unsigned int, float, double, etc. All of these would look the same, except for the argument type and return type. With a template we can define a function instead over some generic
```c++
template <typename T>
T square(T value)
{
    return value * value;
}
```
where T is the type that will be operated on. Now this will be valid for any type that has a multiplication operator.
```c++
int i = 2;
square(i); // returns an int value of 4

float f = 3.0;
square(f); // returns a float value of 9.0

std::string s = "a";
square(s); // this will encounter a compilation error, because std::string does not have a multiplation operator.
```
Also note here, when calling square, we don't have to specify which typed version is called because the compiler is able to deduce it from the function argument. We could however specify it with 
```c++
square<long int>(i); // explicitly call the version using long integers
```
Pretty simple. The more interesting use case is when the template parameter is expected to be an object. For example
```c++
// one version of an object
struct A{
    bool doThing() {return true;};
}
// another version, with the same function signature
struct B{
    int doThing() {return 2;};
}

// a function template, the operates on any type as long as that types has a .doThing() function that returns something that can be printed.
template <typename T>
void printThing(T t){
    std::cout << t.doThing() << std::endl;
}
```
which allows us to call code as
```c++
A a;
printThing(a); // prints "1" for true
B b;
printThing(b); // prints "2"
```
This pattern is in essence an informal version of an interface contract. Why do this instead of using formal interface contract's with abstract classes? Two reasons. First, they are much more flexible, as long as the contract is satisfied the implementations between different objects are totally separate.
Second, GPU code does not support abstract classes, so this is the best you can do (at least until c++20 concepts are widely supported).

### Type deduction
When can the compiler deduce template types? The rule of thumb is when the arguments imply a single unique type matches the template, but if there are multiple possible matches or any ambiguities deduction will fail.

Going back to the square function example, we don't have to specify which typed version is called because the compiler is able to deduce it from the function argument. Then the function argument is an int, then the  
We could however specify it with 
```c++
int i = 1;
square<int>(i); // explicitly call the version using int
square(i); // deduced template of type int from the int argument

square<long int>(i); // explicitly call the version using long integers, and will force casting the function argument to a long int
```
They usually do a very good job of type deduction for small functions like this, and when using primitive types. Once there are many template parameters, and the parameters are themselves templates the deduction can start to struggle.
When in doubt, is it never bad to specify the type.

Compiler warning for these can be dense, and but if you read the errors carefully they will tell you exactly what type it trying to apply, and the is usually not what you expect. Lot of the time, these errors will be from disagreement about being const, pointers, or reference.

### SFINAE 
This nastily looking thing stands for "Substitution Failure Is Not An Error", which I'm sure is immediately meaningful, right!? Jokes aside, what this means is when a compiler attempts type deduction, its only an error if no match can be found, but matches that run into failure themselves do not cause errors. 
https://en.cppreference.com/w/cpp/language/sfinae.html

For example
```c++
template<int I>
struct X {};
 
template<class T>
void f(typename T::Y*) {}
 
template<class T>
void g(X<T::N>*) {}

struct A {};
struct B { int Y; };
struct C { typedef int N; };

struct B1 { typedef int Y; };
struct C1 { static const int N = 0; };
 
int main()
{
    // Deduction fails in each of these cases:
    f<A>(0); // A does not contain a member Y
    f<B>(0); // The Y member of B is not a type
    g<C>(0); // The N member of C is not a non-type 
    // Deduction succeeds in each of these cases:
    f<B1>(0); // B1 contains a type Y
    g<C1>(0); // The N member of C1 is a type that satisfies the X struct
}
```

Okay interesting, but why bring this up? The real power here is `std::enable_if` which allows disabling a template when a condition is met.

For example, say I have a function 
```c++
template<int I, int J>
struct M {};
```



There are also a whole host of type traits designed for this use https://en.cppreference.com/w/cpp/header/type_traits.html

## Constexpr functions
Something that can be evaluated at compile time is considered a constexpr 
https://en.cppreference.com/w/cpp/language/constexpr.html

For a variable this is rather simple. The variable is known at compile time, and will not change. Use this for things like global or class constants.

For example, things like
```c++
// do this
constexpr int Dimensions = 2;
// no this
#DEFINE DIMENSION = 2
```


A constexpr function, is specifies the function *may* be evaluted at compile time. These have to be fairly simple functions in terms of loops and branching.
```c++
constexpr int factorial(int n)
{
    return n <= 1 ? 1 : (n * factorial(n - 1));
}

constexpr int getPiDigit(int i)
{
    constexpr int digits{3,1,4,1,5,9};
    return digits[i];
}
```
Now how you do you confirm these are actually being evaluated at compile time rather than run time?



Constexpr also supports conditional's `https://en.cppreference.com/w/cpp/language/if.html#Constexpr_if`
for example instead of 

```c++
template<int I> 
void f()
{
    std::cout << "Template value " << I << std:endl;
}

template<>
void f<0>
{
    std::cout << "Template value zero" << std:endl;
}

```
we can instead do things like 
```c++
template<int I> 
void f()
{
    std::cout << "Template value ";
    if constexpr(I == 0)
        std::cout << "zero";
    else
        std::cout << I;
    std::cout << std::endl;
}
```
Be careful, the code in a constexpr if is still checked, even though it will compile out. This code will fail to compile.
```c++
void f()
{
    if constexpr(false)
    {
        int i = 0;
        int *p = i; // Error even though in discarded statement
    }
}

```


## Parameter packs

### Looping over a tuple
This is a useful pattern I have encountered. 

## Fold expressions
