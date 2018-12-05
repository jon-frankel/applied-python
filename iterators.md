# Iteration

* A simple definition: Looping over items
    ``` python
    a = [2,4,10,37,62]
    # Iterate over a
    for x in a:
      # ...
    ```
* A very common pattern
* Loops, list comprehensions, etc.
* Most programs do a huge amount of iteration

---

### Many different objects support iteration

``` python
a = 'hello'
for c in a:       # Loop over characters in a
...

b = { 'name': 'Dave', 'password':'foo'}
for k in b:      # Loop over keys in dictionary
...

c = [1,2,3,4]
for i in c:      # Loop over items in a list/tuple
...

f = open('foo.txt')
for x in f:     # Loop over lines in a file
...
```
------------------

### An inside look at the for statement

        for x in obj:
            # statements
            # ...

* Underneath the covers:

        _iter = obj.__iter__() while True:
        # Get iterator object
        try:
             x = _iter.__next__() # Get next item
        except StopIteration:     # No more items
             break
        # statements
        # ...

* Objects that work with the for-loop all implement this low-level iteration protocol

* Example: Manual iteration over a list

  ``` python
  >>> x = [1,2,3]
  >>> it = x.__iter__()
  >>> it
  <listiterator object at 0x590b0>
  >>> it.__next__()
  1
  >>> it.__next__()
  2
  >>> it.__next__()
  3
  >>> it.__next__()
  Traceback (most recent call last):
                File "<stdin>", line 1, in ?
              StopIteration
              >>>
  ```

## Example: Custom Containers

``` python
class Portfolio(object):
   def __init__(self):
       self.holdings = []
   def __iter__(self):
       return self.holdings.__iter__()
...

portfolio = Portfolio()
...

for stock in portfolio:
  # ....
```
