# Python Methodizer
```
                __  __
    ____  __  __/ /_/ /_  ____  ____
   / __ \/ / / / __/ __ \/ __ \/ __ \
  / /_/ / /_/ / /_/ / / / /_/ / / / /
 / .___/\__, /\__/_/ /_/\____/_/ /_/
/_/    /____/
                   __  __              ___
   ____ ___  ___  / /_/ /_  ____  ____/ (_)___  ___  _____
  / __ `__ \/ _ \/ __/ __ \/ __ \/ __  / /_  / / _ \/ ___/
 / / / / / /  __/ /_/ / / / /_/ / /_/ / / / /_/  __/ /
/_/ /_/ /_/\___/\__/_/ /_/\____/\__,_/_/ /___/\___/_/

```
## How to start?
1. Start your terminal
2. You need to have python installed (Mac comes with python3)
3. Create a virtual environment to install all dependencies (you can skip this step, but is recommended). I am using venv, there are other options. `python3 -m venv {name_for_env}` e.g. `python3 -m venv methodizer` 
4. Activate virtual enviroment `source {name_for_env}/bin/activate` e.g. `source methodizer/bin/activate`
5. Go ahead and install python3 modules `pip install -r requirements.txt`
6. Run program `python3 main.py`
7. Read instructions and have fun.

## Methods
### Lists

Methods:

* append(): Adds an element to the end of the list.
* extend(): Extends the list by appending elements from an iterable.
* insert(): Inserts an element at a specified position.
* remove(): Removes the first occurrence of a specified value.
* pop(): Removes and returns the element at a specified index.
* index(): Returns the index of the first occurrence of a specified value.
* count(): Returns the number of occurrences of a specified element.
* sort(): Sorts the list.
* reverse(): Reverses the elements of the list.

Example:

```python
my_list = [1, 2, 3, 4, 5]

my_list.append(6)
my_list.extend([7, 8])
my_list.insert(2, 10)
my_list.remove(4)
element = my_list.pop(0)
index = my_list.index(5)
count = my_list.count(2)
my_list.sort()
my_list.reverse()

print(my_list)  # Output: [8, 7, 6, 5, 3, 2]
```

### Tuples
Methods: Tuples are immutable, so they have fewer methods compared to lists. Methods like `count()` and `index()` are available.

Example:

```python
my_tuple = (1, 2, 3, 2, 4, 2)
count = my_tuple.count(2)
index = my_tuple.index(3)

print(count)  # Output: 3
print(index)  # Output: 2
```

### Dictionaries

Methods:

* keys(): Returns a view of all keys.
* values(): Returns a view of all values.
* items(): Returns a view of all key-value pairs.
* get(): Returns the value of a specified key.
* pop(): Removes and returns the value of a specified key.
* popitem(): Removes and returns the last inserted key-value pair.
* update(): Updates the dictionary with key-value pairs from another dictionary or * iterable.

Example:
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
value = my_dict.get('b')
removed_value = my_dict.pop('a')
removed_item = my_dict.popitem()
my_dict.update({'d': 4, 'e': 5})

print(keys)  # Output: dict_keys(['a', 'b', 'c'])
print(values)  # Output: dict_values([1, 2, 3])
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
print(value)  # Output: 2
```
### Sets

Methods:

* add(): Adds an element to the set.
* update(): Updates the set with elements from another set or iterable.
* remove(): Removes a specified element from the set.
* discard(): Removes a specified element from the set if present.
* pop(): Removes and returns an arbitrary element from the set.
* clear(): Removes all elements from the set.
* union(): Returns a new set containing the union of two or more sets.
* intersection(): Returns a new set containing the intersection of two or more sets.

Example:

```python
my_set = {1, 2, 3, 4}

my_set.add(5)
my_set.update({6, 7})
my_set.remove(3)
my_set.discard(10)
element = my_set.pop()
my_set.clear()

print(my_set)  # Output: set()
```

These examples cover the basic methods of commonly used data structures in Python. They offer flexibility and versatility for various programming tasks.


