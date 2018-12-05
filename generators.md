# Generators

Custom iterators are cool, but what if you don't know the collection ahead of time?

``` python
>>> for x in countdown(10):
    ... print(x, end=' ')
    ...
10 9 8 7 6 5 4 3 2 1
>>>
```

The answer is: generators!

---
* A function that defines iteration:

  ``` python
  def countdown(n):
     while n > 0:
        yield n
        n -= 1

  >>> for i in countdown(5):
      ... print(i, end=' ')
      ...
  5 4 3 2 1

  >>>
  ```
* Any function that uses `yield` is a generator

* Behavior is different than normal function
* Calling a generator function creates a generator object. _It does not start running the function._

``` python
def countdown(n):
   print('Counting down from', n)
   while n > 0:
     yield n
     n -= 1

 >>> x = countdown(10) # No output!
>>> x
<generator object at 0x58490>
```

* Function only executes on `__next__()`:

``` python
>>> x = countdown(10)
>>> x
<generator object at 0x58490> >>> x.__next__() # Function starts executing here
   Counting down from 10
10
>>>
```


* `yield` produces a value, but suspends function
* Function resumes on next call to `__next__()`
  ``` python
  >>> x.__next__()
  9
  >>> x.__next__()
  8
  >>>
  ```

> **Observation**
>
> A generator function implements the same low-level protocol that the for statement uses on lists, tuples, dicts, files, etc.

## Why use generators?

* Many problems are much more clearly expressed in terms of iteration
* Looping over a collection of items and performing some kind of operation (searching, replacing, modifying, etc.)
* Processing pipelines can be applied to a wide range of data processing problems
* Better memory efficiency
* Only produce values when needed
* Contrast to constructing giant lists
* Can operate on streaming data
