1. Python is a high-level general-purpose programming language that can be applied to many
different classes of problems.
    The language comes with a large standard library that covers areas such as string
processing (regular expressions, Unicode, calculating differences between files), internet
protocols (HTTP, FTP, SMTP, XML-RPC, POP, IMAP), software engineering (unit testing, logging,
profiling, parsing Python code), and operating system interfaces (system calls, filesystems,
TCP/IP sockets).

2. Python is called dynamically typed language because it doesn’t know about the type of the
variable until the code is run. So declaration is of no use. What it does is, It stores that
value at some memory location and then binds that variable name to that memory container
Moreover, it makes the contents of the container accessible through that variable name. So the
data type does not matter. As it will get to know the type of the value at run-time.

3. Pros
Beginner-friendly
Large Community
Flexible and Extensible
Extensive Libraries
Embeddable
Highly Scalable
IoT Opportunities
Portable

Cons
Issues with design
Slower than compiled languages
Security
Work Environment
High memory consumption
Dynamically-typed language
Complex multithreading
Garbage collection leads to potential memory losses

4. Top 5 domains where we can use Python
Web Development, Data Science, OS devlopment, Scientific Programming, Gaming

5. Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

Syntax: 

```
x = 5
y = "John"
print(x)
print(y)

```

6. We can take input in pyhton using the input() function.

7. By default, input returns a string. So the name and age will be stored as strings

8. Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

9. Yes. We can use functions like split(), map(), List Comprehension

Using split():

```
$a, b = input("Enter two of your lucky number: ").split() 
$print("First lucky number is: ", a) 
$print("Second lucky number is: ", b) 

```


Output:
Enter two of your lucky number: 7 1
First lucky number is: 7
Second lucky number is: 1

using map():

```
$x, y = map(int, input("Enter two values: ").split())
$print("First Number is: ", x) 
$print("Second Number is: ", y)

```


Output:
Enter two values: 7 1
First Number is: 7
Second Number is: 1

using List Comprehension

```
$x, y = [x for x in input("Enter your name and age: ").split(",")]
$print("Your name is: ", x) 
$print("Your age is: ", y)

```


Output:
Enter your name and age: FACE Prep, 8
Your name is: FACE Prep
Your age is: 8

10. Keyword is a closely related or associated word that is reserved by a program because, the word has a special meaning that defines commands and specific parameters for that code set.

11. We cannot use keywords as variable names. It's because keywords have predefined meanings.

12 Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

13. To throw (or raise) an exception, use the raise keyword.

14. Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

15. In Python programming, you can perform division in two ways. The first one is Float Division("/") and the second is Integer Division("//") or Floor Division.

16. Code: 

```
$str = "iNeuron"
$print(str*4)

```

17. 
```
$num = int(input("Please Enter the number to be checked."))
$if num % 2 == 0:
$   print("The number is even.")
$else:
$   print("The number is odd.")

```

18. Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search, resulting in more focused and productive results.

19. What will the output of the following?
```
1 or 0 = TRUE

0 and 0 = FALSE

True and False and True = FALSE

1 or 0 or 0 = TRUE

20. Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

21. The if/elif/else structure is a common way to control the flow of a program, allowing you to execute specific blocks of code depending on the value of some data.

--> if statement: If the condition following the keyword if evaluates as true, the block of code will execute. Note that parentheses are not used before and after the condition check as in other languages.

```
$if True:
$  print('If block will execute!')

```

```
$x = 5

$if x > 4:
$  print("The condition was true!") #this statement executes

```

--> else statement:You can optionally add an else response that will execute if the condition is false:

```
$if not True:
$  print('If statement will execute!')
$else:
$  print('Else statement will execute!')

```

Or you can also see this example:

```
$y = 3

$if y > 4:
$  print("I won't print!") #this statement does not execute
$else:
$  print("The condition wasn't true!") #this statement executes

```

Note that there is no condition following the else keyword - it catches all situations where the condition was false


--> elif statement: Multiple conditions can be checked by including one or more elif checks after your initial if statement. Just keep in mind that only one condition will execute:

```
$z = 7

$if z > 8:
$  print("I won't print!") #this statement does not execute
$elif z > 5:
$  print("I will!") #this statement will execute
$elif z > 6:
$  print("I also won't print!") #this statement does not execute
$else:
$  print("Neither will I!") #this statement does not execute

```

Note: only the first condition that evaluates as true will execute. Even though z > 6 is true, the if/elif/else block terminates after the first true condition. This means that an else will only execute if none of the conditions were true.

22. 
```
$age_of_a_person = int(input("Please enter your age."))
$if age_of_a_person >= 18:
$    print("I can vote")
$else:
$    print("I can't vote")

```

23. 
```
$numbers = [12, 75, 150, 180, 145, 525, 50]
$
$sum_of_evens  = 0
$for num in numbers:
$    if(num%2 == 0):
$        sum_of_evens += num
$
$print("The sum of evens in the given list is:", sum_of_evens)

```

24.
```
$a, b, c = input("Enter three numbers.").split()
$print("The maximum of three numbers are:", max(a,b,c))

```

25.
```
$numbers = [12, 75, 150, 180, 145, 525, 50]
$ans = list()
$for num in numbers:
$    if(num % 5 == 0):
$        if(num > 150 and num < 500):
$            continue
$        if(num > 500):
$            break
$        ans.append(num)
$
$print(ans)\

```

26. In Python, Strings are arrays of bytes representing Unicode characters. Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

Strings in Python can be created using single quotes or double quotes or even triple quotes. 

Syntax:
$string s1 = "This is a string."

27. You can access the characters in a string by referring to its index number inside square brackets [] .

28. 
```
string = "Big Data iNeuron"
print(string[8:])

```

29. 
```
string = "Big Data iNeuron"
print(string[-1:-8:-1])

```

30. 

```
string = "Big Data iNeuron"
reversed_string = string[-1:0:-1]

```

31. An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.

32. 
An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.

33. 
```
print("iNeuron's Big Data Course")
```

34.
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data. List items are ordered, changeable, and allow duplicate values.

35. To create a list in Python, we use square brackets ([]). Here's what a list looks like:

Method 1:
ListName = [ListItem, ListItem1, ListItem2, ListItem3, ...]

Method 2:
ListName = list()

36. Using the [] brackets we can access the elements of a list.

37. 
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])

```

38. 
```
input_list = list()

while(True):
    str = input("Enter the number you wabt to append in list. Enter \"I dont want to enter anymore\" to break the loop.")
    if (str == "I dont want to enter anymore"):
        break
    input_list.append(int(str))

print(input_list)
print("The length of the list is", len(input_list))

```

39. 
```
lst = ["Welcome", "to", "Data", "course"]
lst.insert(3,"Big")

print(lst)

```

40. Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

41. tup1 = tuple()

42. We can't add elements to a tuple because of their immutable property.

43. We can use '+' operator to append two tuples.
```
# input tuple 1
inputTuple_1 = (12, 8, 6)
# input tuple 2
inputTuple_2 = (3, 4)
# appending/concatenating 2nd tuple to the first tuple using the + operator
resultTuple = inputTuple_1 + inputTuple_2
# printing the resultant tuple after appending
print("Resultant tuple after appending inputTuple_2 to the inputTuple_1:", resultTuple)

```

44. 

```
input_tuple = (1,2,3,4,5,6,7,8,9)

print(input_tuple)
print("The length of the list is", len(input_tuple))

```

45. Sets:
    1. Sets are used to store multiple items in a single variable.
    2. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
    3. A set is a collection which is unordered, unchangeable*, and unindexed.

46. Creating a set in Python:
```
input_set = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9}

print(input_set)

```
We can declare sets using {} braces and also by using explicit type-casting.

47. 
```
input_set = {'abc', 'def', 'abc', 'Hello', 'No!'}

input_set.add('iNeuron');
print(input_set)

```

48. update() is used to add multiple values in python set.
```
input_set = {'abc', 'def', 'abc', 'Hello', 'No!'}

input_set.update(['iNeuron', 'Help'])
print(input_set)

```

49. To add one item to a set use the add() method.
To add more than one item to a set use the update() method.

50. It clears the entries of the set.

51. The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
Syntax:
    frozenset(iterable)
example:
```
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
# x.update(["strawberry"])
print(x)

```

52. In frozenset() we cannot update the set. But in set() we can add new entries, i.e; we can update the set.

53. The union() method returns a set that contains all items from the original set, and all items from the specified set(s). You can specify as many sets you want, separated by commas. It does not have to be a set, it can be any iterable object. If an item is present in more than one set, the result will contain only one appearance of this item.
Syntax:
    set.union(set1, set2...)

Example:
```
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result) 

```

54. The intersection() method returns a set that contains the similarity between two or more sets.
Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
Syntax:
    set.intersection(set1, set2 ... etc)

Example:
```
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result) 

```
55. Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

56. 

57. 
```
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

```

58. 
Output:
```
<class 'dict'>

```
59. 

