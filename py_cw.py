# HAMZA MOORAJ
# H00390746              <--- so we know who you are
# EDINBURGH              <--- Edinburgh, Dubai, or Malaysia 
# F28PL Coursework 1, Python         <--- leave this line unchanged 

# Deadline is Wednesday 26 October 2022 at 15:30, local time for your campus (Edinburgh / Dubai / Malaysia).

# It is not your marker's role to debug basic syntax errors.
# Therefore, if your script won't compile then it might not be marked.
# In other words: if `python3 py_cw.py` won't execute, then your marker is not obliged to mark your answers. 

# To do this coursework, FORK, THEN CLONE the gitlab project.

# If you do it the other way around, then you'll have cloned *my* project (which you can't `git push` to), rather than cloned *your fork* of the project (which you can `git push` to).  
# Any questions, don't guess: ask.

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# The test file test_cw.py is not exhaustive. 
# Just because your answer passes it does not mean it's correct.
# You would do well to consider where errors might be lurking and to add these to test_cw.py.   
# You are not marked directly on the quality of additional tests, however your marker may be
# able to assign marks for understanding as demonstrated in any tests you may write, 
# even if the code itself isn't quite right. 

# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  

# Before submitting this coursework please complete the Student authorship declaration here:
#   https://canvas.hw.ac.uk/courses/20804/assignments/102574 
 

# Do not delete the text from here ... 
################################################################################
# Question 1   

"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here


#####################################
# Question 1a

def cadd(c1, c2):
    return ((c1[0] + c2[0]) , (c1[1] + c2[1]))

#Multiply the complex numbers using the idea of vectors.
def cmult(c1,c2):
    x1, x2, y1, y2 = c1[0], c1[1], c2[0], c2[1]
    return ((x1*y1 - x2*y2) , (x1*y2 + x2*y1))


#####################################
# Question 1b

def tocomplex(x1, y1):
    y1 *= 1j #creates a complex number where y1 is the imaginary value
    return (x1 + y1)


def fromcomplex(c):
    return ((c.real) , (c.imag))


# END ANSWER TO Question 1
################################################################################



################################################################################
# Question 2

"""
2a. Using def, write iterative functions 
* seqandi and 
* seqxori 
that implement pointwise AND (https://en.wikipedia.org/wiki/Logical_conjunction) and XOR (https://en.wikipedia.org/wiki/Exclusive_or) of boolean sequences.
For instance
 seqandi([True,True,False],[True,False,True])
should compute
 [True, False, False]
and
 seqxori([True,True,False],[True,False,True])
should compute
 [False, True, True]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqandr and seqxorr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqandlc and seqxorlc.
"""
#####################################
# Question 2a

def seqandi(l1, l2):
    l3 = []
    for count in range (0, len(l1)):
        l3.append(l1[count] and l2[count]) 

    return (l3)       


def seqxori(l1, l2):
    l3 = []
    for count in range (0, len(l1)):
        if (l1[count] == l2[count]):
            l3.append(False)

        else:
            l3.append(True) 

    return (l3)


#####################################
# Question 2b

def seqandr(l1 , l2 , l3 = [] , idx = 0):
    if (idx < len(l1)): #idx is used to access list of boolean values
        #recursive case
        l3.append(l1[idx] and l2[idx])
        return(seqandr(l1 , l2 , l3 , idx+1))

    else:
        #Base Case
        return l3
        


def seqxorr(l1, l2, l3 = [] , idx = 0):
    if (idx < len(l1)): #idx is used to access list of boolean values
        #recursive case
        [l3.append(False) if (l1[idx] == l2[idx]) else l3.append(True)]
        return(seqxorr(l1, l2, l3, idx+1))

    else:
        #base case
        return l3
    

#####################################
# Question 2c

def seqandlc(l1,l2):
    l3 = []
    [l3.append(l1[count] and l2[count]) for count in range (0, len(l1))]
    return (l3)  


def seqxorlc(l1,l2):
    l3 = []
    [l3.append(False) if (l1[count] == l2[count]) else l3.append(True) for count in range (0, len(l1))]
    return (l3)


# END ANSWER TO Question 2
################################################################################


###############################################################################
# Question 3

"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
a. Mutable vs immutable types. Give at least two examples of each, with explanation.
b. Integer vs float types.
c. Assignment = vs equality == vs identity is.
d. The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
e. Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""
#################################################################################
#ANSWER TO Question 3:

"""
Data is essential for any programming language, and every programming language has its own way of representing that data. In python, there are many types of data such as integers, 
floats, strings, lists, tuples, dictionaries etc. These types of data have attributes that differ one from another, and are represented in different ways.

One attribute of data in Python that is very important is mutability. Data types such as dictionaries and lists are mutable, whereas types such as strings and tuples are immutable.
Mutable data types are data types that have methods to change the data in place.
    Lists are mutable arrays, represented using square brackets, and elements are separated by commas:
        [0, 1, 2] and ["Hello", "World" , "!"]
        Lists have methods such as list.append() which adds elements to the end of the list, and list.reverse() which reverses the order of the elements. Lists can also be modified
        by accessing the elements in the list using their index:
            x = [0, 3, 7]
            x[1] = 4
            print(x) #which will output...
            >>> [0, 4, 7]
    Dictionaries represent unordered sets of key-value pairs. They are written as below:
        rooms = {
            1: "Jack",
            2: "John"
        }
        Dictionaries can be edited by accessing the values using the keys. For example, rooms[1] = "David" will change the value assigned to key 1, from "Jack" to "David".
    In these ways, the values in the lists and dictionaries can be modified permanently in place.
Immutable data types cannot be changed in place. For example:
    With strings such as, "Hello World", we can access separate characters using [], but we cannot change the characters in the string in place. We would have to write a new string
    if we were to make any changes, as is the same with tuples, which are represented with regular brackets: (1, 3, 4)

Integers and Floats are two types of data that represent numbers, however, integers are only whole numbers i.e. 45, 56 or 32. And floats are numbers with decimal points i.e. 1.0, 2.1,
or 43.653. There is another difference between them: integers have infinite precision, and floats do not. This means that Python will always try to compute integer computations, no
matter how much memory is being used, whereas float computations will give an OverFlowError. Infinite precision can also cause a rounding error when converting integers to floats.
For example:
    10**60 #will give us 1000000000000000000000000000000000000000000000000000000000000
    int(1e60) #will give us 999999999999999949387135297074018866963645011013410073083904
    10**60 - int(1e60) #will give us 50612864702925981133036354988986589926916096
    10**60 == int(1e60) #will give us False
    This means that there will be a rounding error of 50612864702925981133036354988986589926916096.

Variables are an important part of any programming language. In python, variables are simply pointers to locations in memory.
    x = 32 #this stores the value 32 in the memory, and assigns x as its pointer. Now whenever x is called, Python will return 32.
When writing programs in Python, we often use == in conditional statements. We also sometimes use the keyword 'is'.
    x = []
    y = []
    x == y #The == compares the values that x and y are pointing to, thus...
    >>> True
    x is y #The 'is' keyword however, tests if two variables refer to the same object, thus...
    >>> False
In the case below:
    x = []
    y = x #This line assigns y to point at the memory location that x is pointing at. This means that x and y both point to the same memory location
    x is y #Therefore this line will return True
    >>> True

Another data type that is often used in Python programming is range; it is also a function. The range function generates a computation for a range of numbers. It does not generate a 
list of numbers, but a computation, which can be thought of as an idea of a list of numbers. For example:
    range(0, 10) #This generates a computation of a range of numbers starting from 0(inclusive) to 10(exclusive)
    >>> range(0, 10) #This is the output of the above line, proving that it is not a list.
    list(range(0,10)) #Wrapping range() in list() will list out the computation that range generates.
    >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #This is the output of the range() wrapped in list()

Slicing is a method that is used to get part of an indexed data type such as, lists and strings. Slicing is done as follows:
    x = "Hello World"
    x[0:3] #This is a slice of the string pointed by x, from its 0th element to its 2th element(as the second value in the slice is excluded). Thus the output is...
    >>> 'Hel'
Slicing can also be done on lists, and can be especially useful to get the last value without knowing the length of a list:
    x = list(range(randint(1,10))) #This line lists a range of numbers from 0 to a random integer from 1 to 10 inclusive
    x[-1] #A slice with -1 means the last value. In this way, we can get the last element in the list, without knowing how long it is.
    >>> 4 #That means the random integer generated was 5, and the list's last element is 4
Despite list(range(10**10)[10:10]) and list(range(10**10))[10:10] resulting [], there is a significant difference between the two.
    list(range(10**10)[10:10]) preforms the slice before the range is listed
    Whereas, list(range(10**10))[10:10] preforms the slice after the list of the range is created.
    This is important because, a value such as 10**10( = 10000000000) to be listed would take a lot of memory, which even 12GB of RAM cannot handle. Having the slice inside the list()
    allows the computer to list out the sliced list rather than giving a MemoryError

"""
# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4

"""
Recall that `map(f, l)` applies a function pointwise to a list, so that 
   map(f, [x, y, z]) 
computes 
   [f(x), f(y), f(z)]
Call a *datum* something that is either an integer, or a list of data (datums).
Write a generalised mapping function `supermap` that applyies `f` pointwise to any integers inside a datum. 

So for example:
* supermap(f, -5) should return 'f(-5)'
* supermap(f, []) should return '[]'
* supermap(f, [5, [5]]) should return '[f(5), [f(5)]]'. 

You may find it useful to consider `isinstance` or the following code fragment
   type(5) == int 

An answer that guts the question (e.g. by calling a supermap-like function in a Python library) may score no marks.
"""


def supermap(f, dat):
    if(isinstance(dat, int)): #Checks if dat is an int
        return(f(dat))

    elif(isinstance(dat, list)): #Checks if data is a list
        if(dat == []):
            return(dat)

        else:
            return([supermap(f, i) for i in dat]) #recursively applies supermap using for loop to access dat

# END ANSWER TO Question 4
################################################################################



###############################################################################
# Question 5

"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""


def fenc(i):
    if(i == 0):
        return []

    else:
        return [fenc(i-1), [fenc(i-1)]]


def fdec(l, n=0): #Counts the number of times list needs to be accessed to reach an empty list
    if(l == []):
        return n

    else:
        l = l[0]
        return fdec(l, n+1)


# END ANSWER TO Question 5
################################################################################



###############################################################################
# Question 6

"""
Implement a generator `love` such that if we assign
 x = love()
then repeated calls to
 next(x)
return the strings 
 I love you 
 You love that I love you
 I love that you love that I love you
 You love that I love that you love that I love you
 I love that you love that I love that you love that I love you
 ...
For full marks, your answer should respect correct capitalisation, as above.

Note that this question is not asking you to program an endless loop that prints these values; your answer should be a generator that yields these values.
"""

def love():
    sel = ["You love that ", "I love that you love that "] #To fit capitalisation
    #Use two sentences so that You can be capitalised in one scenario and uncapitalised in the next
    sentence1 = "I love you" #For capital Y
    sentence2 = "I love you" #For small y
    yield sentence1
    index = 0 #index flips between 1 and 0 to access list 'sel'
    while True:
        if (index == 0):
            sentence1 = sel[index] + sentence1
            index += 1
            yield sentence1

        elif (index == 1):
            sentence2 = sel[index] + sentence2
            index -= 1
            sentence1 = sentence2 #So that next yield would have small y already.
            yield sentence1


# END ANSWER TO Question 6
################################################################################



#################################################################################
# Question 7

"""
Consider functions that remove all instances of an integer `i` from a list of integers `l`, implemented in three distinct ways:

1. `removeall_oo` repeatedly applies the list .remove method until there are no instances of `i` left (you may use other programming constructs, such as counting the number of integers in `l`, or using exception raisers and handles).  
2. `removeall_ft` uses `import functools` and `filter`.  
3. `removeall_rd` uses `import functools` and `reduce` (but not filter). 

So for example, 
   removeall_oo(0, [0, 0, 1])
should return
   [1]
and
   removeall_oo(0, [0, 0])
should return
   []
"""

def removeall_oo(n, l):
    for i in l:
        l.remove(n)

    return (l)
    
def removeall_ft(n, l):
    return(list(filter(lambda x: x != n, l)))


def removeall_rd(n, l):
    from functools import reduce
    reduce(lambda a, b: l.remove(n), l, 0) #Use reduce to run through list two elements at a time, and remove instance of n when it comes up. Defaults 0 in the event both a and b are != n
    return (l)


# END ANSWER TO Question 7
################################################################################



##########################################################
# Question 8

"""
The *Sudan* function is documented here:
   https://en.wikipedia.org/wiki/Sudan_function
Implement the Sudan function as a Python function `sudan(n, x, y)` by orienting the equalities and making recursive calls as appropriate.

Be careful: even `sudan(2,2,2)` freezes up my machine.
"""

def sudan(n, x, y):
    if(n == 0):
        return(x+y)

    elif(y == 0):
        return(x)

    else:
        return(sudan(n-1, sudan(n, x, y-1), sudan(n, x, y-1)+y))


# END ANSWER TO Question 8
################################################################################



###############################################################################
# Question 9 

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""


"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 

#################################################################################
#ANSWER TO Question 9:

"""
Python is one of the slower programming languages of today. Yet, it stands in the top 2 among popular ranking indexes, as of 2022. (Rankings: https://distantjob.com/wp-content/uploads/2022/01/Top-Programming-Languages-comparison-table.jpg)

Python was built on the DRY(Don't Repeat Yourself) principle. This enhances its readability, which grouped with its robust string manipulation, massive collection of libraries and
easy shell access makes it a useful tool for automating repetitive tasks. Python is, therefore, a very popular option for Artificial Intelligence/Machine Learning and Data Science
applications. 

The libraries available for Python only help it's case in being a very popular language for many applications. A few well known Python libraries in the science world are:
    - SciPy which is used for advanced computing
    - Pandas which is used for general-purpose data analysis
    - Matplotlib and Seaborn for data visualization
    - Keras, Tensorflow, SciKit-Learn for Machine Learning applications
    - NumPy for high-performance scientific computing and data analysis
Apps such as FreeCAD(a #D modelling software) and Abaqus(a finite element method software) are coded in Python. Python also has libraries such as PyQt and Tkinter which allows Python
to be a popular option for GUI focused programming(such as Desktop GUIs and even Operating Systems). Python also has access to PySoy and PyGame, which have been used for Game Development
for popular titles such as Battlefield 2 and Civilization-IV. 

Due to Python's cross-platform functionality, it can be used to develop all sorts of apps such as, web apps, gaming apps, and ML apps, to name a few. This also allows Python to be a
portable language. This means that Python code written for a Windows or Linux machine, can be run on MacOS, iOS and vice versa(of course as long as there is no system-dependent features), 
making it a popular option for app development.

Python is an interpreted object-oriented and functional programming language. This means that unlike Java and C++(whose code is run as a whole after compilation), its code is run line
by line making it easier to debug, once again making it popular amongst Programmers across the board. It can model real-world data being object-oriented, and can make use of functions
being a functional language. This in turn opens Python up to even more applications. 

Python was created by Guido Van Rossum while he was working for CWI. Rossum used to use a language called ABC. He wanted to correct some of ABC's problems, and keep some of its useful
features. He was working on the Amoeba distributed OS group and wanted a scripting language with a syntax like ABC's but with access to System calls. Therefore, he started to work on
an extensible language which he later called Python.

Python has faced a few issues. Being a relatively new language, it was unfamiliar to many, although after a few days of using Python, one would find it quite easy to use. Python has 
gaps in its documentation compared to other languages; obviously due to its young age. Python is a popular language because of its libraries. The downside to all of this is that these
libraries require installation, and further learning. Python lacks the prepackaged solutions that other languages such as PHP have.

Despite all this, Python has a very powerful community of developers, who are available on forums such as StackOverflow. These developers also aid in the creation of libraries, and with
Python's rising popularity, there is no deceleration in its release of new libraries. Python is being taught in education institutions all over the world, and is in fact the preferred
language for the CAIEs which is an Assessment used all over the world. 
"""

# END ANSWER TO Question 9 
###############################################################################



###############################################################################
# Question 10

"""
a. Explain in words the difference between 
   ([],[],[]) 
and 
   [[]]*3.
b. Explain in words what x points to in memory after we execute the following two commands:
     x = []
     x.append(x)
"""

#################################################################################
#ANSWER TO Question 10:
"""
a. Firstly, [[]]*3 creates the list: [[],[],[]]. The difference between the two is that:
    1. ([],[],[]) is a tuple of three empty lists. And [[]]*3 is a list of three empty lists.
    2. This means the first is immutable, and the second is mutable.

b. x initially points to an empty list. When we append x with x, now x points to a list containing x (which in turn points to a list containing x). We can think of it like the
infinity mirror (i.e. when two mirrors face each other). It is thus infinitely recursive.
"""

# END ANSWER TO Question 10 
###############################################################################



###############################################################################
# Question 11

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    n = str(n) #Change n to a string so I can access digits one by one
    l = []
    if(n == '0'):
        return l

    else:
        for i in n:
            i = int(i)
            l.insert(0, i)

        return l


# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    if(I == []):
        return(0)

    else:
        I.reverse() #reverse list so digits are in correct order
        n = '' #concatenate digits in string form
        for x in I:
            x = str(x)
            n += x
        I.reverse() #reverse list back so that after pint(I) is executed, I remains unchanged
        return int(n)


# add two infinite integers
# e.g. iadd([5], [5]) = [0,1]
def iadd(I,J,count=0,rem=0):
    if(I == [] and J == []): #Case if both I and J are empty(i.e. 0)
        return []

    elif(I==[] or J==[]): #Case if either I or J is empty(i.e. 0)
        if(I == []): #Case: I is empty
            return J
        else: #Case: J is empty
            return I

    else: #Case: Neither I nor J are empty
        odd = len(I) - len(J) #Calculate difference in length of I and J in case one has more elements than the other

        if(odd > 0): #If odd is > 0, that means I has more elements than J
            J += [0] * odd #Add [0] odd amount of times to J so that I and J are of equal length now - This would be the same as adding 0s in front of an integer (7 == 07 and 134 == 0134)
            return iadd(I,J) #Restart function with I and J having equal lengths

        elif(odd < 0): #If odd is < 0, that means J has more elements than I
            odd *= -1 #Cancel out negative to allow for multiplication below
            I += [0] * odd
            return iadd(I,J)

        #We make all changes to I... Can be done with J as well..
        elif(odd == 0): #If odd == 0 then I and J have equal lengths. If function is restarted above, then I and J will have equal lengths and skip first two if cases.
            #Base Case
            if(count >= len(I)): #Keep a count to allow us to have a base case for recursion - If count surpasses len(I), then that means function has been applied to all elements in I and J
                if(rem == 0): #This if..else statement is to check that rem is 0 or not. If rem is not 0 at the base case, then that means the answer has one more digit than I and J
                    return I
                else:
                    I.append(rem)
                    return I

            x = list(zip(I, J)) #Creates a list with elements in I and J with the same order "tupled" together
            x[count] = sum(x[count]) + rem #rem is the remainder that is carried forward from previous recursive step(initially rem is 0)
            #Recursive case
            if(x[count] > 9): #If sum ends up being greater than 9, then we have to increment rem, which is done in recursive step
                x[count] -= 10
                I[count] = x[count]
                return iadd(I,J, count+1, rem=1)
            else:
                I[count] = x[count]
                return iadd(I,J, count+1, rem=0)
        

# multiply two infinite integers
# e.g. imult([], [5]) = []
def imult(I,J): #Function adds I to total, J number of times, simulating multiplication(30*2 == 30+30)
    if((I == []) or (J == [])): #If either I or J is [], then anything *0 is 0
        return []

    else:
        counter = pint(J) #Change J to regular integer to be used as a counter(for above reason)
        total_num = pint(I)             #I did not do total = I, as they are lists
        total = iint(total_num)         #Therefore any changes made to total, will end up being made to I as well, throwing the entire calculation off.
        for _ in range(counter - 1):
            total = iadd(total, I)
        return total

# raise I to the power of J
def ipow(I,J): #Function multiplies I to total(which is == to I(not 'is')), J number of times, simulating power(5**2 == 5*5)
    if(J == []): #If either J is [], then anything **0 is 1
        return [1]

    else: #Implementation is same as imult(), only imult() is used instead of iadd() below
        counter = pint(J)
        total_num = pint(I)             
        total = iint(total_num)         
        for _ in range(counter - 1):
            total = imult(total, I)
        return total


# END ANSWER TO Question 11 
###############################################################################



###############################################################################
# Question 12

"""
Recall from Question 4 the notion of a *datum*.

a. Write a command `abstractsize` which inputs a datum and returns an integer measure of how much memory it occupies (cf. Question 10).
Note this measure should be in an abstract unit in which each integer occupies one unit of memory and each pair of square brackets occupies one unit of memory, modulo sharing, 
so that (for example) `[5,5]` has measure 3 --- one for the square brackets, and one for the two integer payloads.  (Do not try to return actual memory usage in bytes, since this 
will depend on implementation and on the size of the integer payload!) 

b. Write a command `compress` which inputs a datum, and outputs a datum that represents it and minimises abstract size.  Your code should be clear and well-commented with an 
explanation (if required) of the algorithm you use.

We're not looking for precise bytecounts and certainly not looking for speed or optimal performance.  Marks will be awarded for elegance, clear commenting, and understanding of the 
issues involved. 
"""
#a.
def abstractsize(datum): #Recursion is necessary in case of nested lists.
    size = 0
    if isinstance(datum, int):
        size += 1 #Memory used for integer is 1

    elif isinstance(datum, list):
        size += 1 #Memory used for [] is 1
        for element in datum:
            element_size = abstractsize(element) #Use recursion to apply abstractsize() on each element in datum, which will allow us to count memory used for any list nested in datum
            size += element_size #Add memory occupied calculated for element to final size counter

    return size

#b.
def compress(datum): #Compresses datum until its abstractsize is as small as can be(for lists, it adds elements in nested list to outermost list, and if list has one element, it removes the [])
    if(isinstance(datum, int)): #In the case datum has no [] to remove, it is already at its most compressed
        return datum
        
    elif(isinstance(datum, list)): #Nested function is required, so that the check for a list with one element does not interrupt recursion process.
        def flatten(datum): #Flattens list, so that any nested lists have the [] removed.
            if(len(datum) == 0):
                return datum
            elif(isinstance(datum[0], list)):
                return flatten(datum[0]) + flatten(datum[1:])
            return datum[:1] + flatten(datum[1:])

        flat = flatten(datum)

        if(len(flat) == 1): #Checks if the list has only one element, for which we remove the [] to get the most compressed form
            return flat[0]
        else:
            return flat


    
# END ANSWER TO Question 12 
###############################################################################



###############################################################################
# Question 13 (bonus question) 

"""
The code below to define `equals23` takes up five lines and 83 characters, by my count. 
It is also ugly, redundant, and indirect.
Rewrite it, so that it is clean, compact, direct --- and takes up one line and 23 characters.
"""

"""
Previous Code:
    def equals23(x):
    if (x == 23):
        return True
    else:
        return False
"""

equals23Length = "equals23=lambda x:x==23"
equals23=lambda x:x==23

# END ANSWER TO Question 13 
###############################################################################
