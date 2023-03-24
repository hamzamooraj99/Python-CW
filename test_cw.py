import importlib
import py

from pytest import fail  
py_cw = importlib.import_module("py_cw")


## Q1

def test_q1a():
	s = py_cw.cadd((1, 0), (0, 1))
	p = py_cw.cmult((3, 2), (9, 6))
	assert s == (1, 1) and p == (15, 36)


def test_q1b():
	assert py_cw.tocomplex(1, 2) == (1 + 2j) and py_cw.fromcomplex(1 + 1j) == (1, 1)


## Q2

def test_q2a():
	assert py_cw.seqandi([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxori([True, False, True, False], [True, True, False, False]) == [False, True, True, False]

def test_q2b():
	assert py_cw.seqandr([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorr([True, False, True, False], [True, True, False, False]) == [False, True, True, False]


def test_q2c():
	assert py_cw.seqandlc([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorlc([True, False, True, False], [True, True, False, False]) == [False, True, True, False]


## Q3 


## Q4 

def test_q4_supermap():
    assert py_cw.supermap( lambda a : 2*a, [5, [5]] ) == [10, [10]]
    assert py_cw.supermap( lambda a : 2*a, [] ) == []
    assert py_cw.supermap( lambda a : 2*a, 7 ) == 14
    assert py_cw.supermap( lambda a : 2*a, [2, 4, [5, [5]]] ) == [4, 8, [10, [10]]]
    assert py_cw.supermap( lambda a : 2*a, [1, 2, 3]) == [2, 4, 6]


## Q5 

def test_q5_fenc():
    assert py_cw.fenc(0)==[]
    assert py_cw.fenc(1)==[[], [[]]]
    assert py_cw.fenc(3)==[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]
    assert py_cw.fenc(6)==[[[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]], [[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]]], [[[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]], [[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]]]]]


def test_q5_fdec():
    assert py_cw.fdec([])==0
    assert py_cw.fdec([[], [[]]])==1
    assert py_cw.fdec([[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]])==4
    assert py_cw.fdec([[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]], [[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]]])==5


## Q6 

def test_q6_love():
   x = py_cw.love()
   assert next(x) == "I love you"
   assert next(x) == "You love that I love you"
   assert next(x) == "I love that you love that I love you"
   assert next(x) == "You love that I love that you love that I love you"
   assert next(x) == "I love that you love that I love that you love that I love you"
   assert next(x) == "You love that I love that you love that I love that you love that I love you"
   assert next(x) == "I love that you love that I love that you love that I love that you love that I love you"

## Q7

def test_q7_removeall_oo():
    assert py_cw.removeall_oo(0, [0, 0, 1, 1, 0]) == [1, 1]
    assert py_cw.removeall_oo(2, [2, 3, 4, 5, 2, 2]) == [3,4,5]

def test_q7_removeall_ft():
    assert py_cw.removeall_ft(0, [0, 0, 1, 1, 0]) == [1, 1]
    assert py_cw.removeall_ft(2, [2, 3, 4, 5, 2, 2]) == [3,4,5]

def test_q7_removeall_rd():
    assert py_cw.removeall_rd(0, [0, 0, 1, 1, 0]) == [1, 1]
    assert py_cw.removeall_rd(2, [2, 3, 4, 5, 2, 2]) == [3,4,5]

## Q8

def test_q8_sudan():
    assert py_cw.sudan(0,0,0) == 0 
    assert py_cw.sudan(1,4,3) == 43
    assert py_cw.sudan(2,2,1) == 27
    assert py_cw.sudan(2,5,1) == 440

## Q9

## Q10

## Q11

def test_q11_iint():
    assert py_cw.iint(0) == []
    assert py_cw.iint(12) == [2,1]
    assert py_cw.iint(34) == [4,3]
    assert py_cw.iint(43543) == [3,4,5,3,4]

def test_q11_pint():
    assert py_cw.pint([]) == 0
    assert py_cw.pint(py_cw.iint(12)) == 12
    assert py_cw.pint(py_cw.iint(34)) == 34
    assert py_cw.pint(py_cw.iint(43543)) == 43543

def test_q11_iadd():
    assert py_cw.iadd([], []) == []
    assert py_cw.iadd([], [2]) == [2]
    assert py_cw.iadd([2], []) == [2]

    assert py_cw.iadd([2], [3]) == [5]
    assert py_cw.iadd([5], [5]) == [0,1]
    assert py_cw.iadd([3,1], [8,2]) == [1,4]
    assert py_cw.iadd([1,4], [9,5]) == [0,0,1]

    assert py_cw.iadd([3,1], [7]) == [0,2]
    assert py_cw.iadd([4,3,1], [9]) == [3,4,1]
    assert py_cw.iadd([4,9], [6]) == [0,0,1]
    assert py_cw.iadd([2,0,1], [8,1]) == [0,2,1]

    assert py_cw.iadd([7], [3,1]) == [0,2]
    assert py_cw.iadd([9], [4,3,1]) == [3,4,1]
    assert py_cw.iadd([6], [4,9]) == [0,0,1]
    assert py_cw.iadd([8,1], [2,0,1]) == [0,2,1]

def test_q11_imult():
    assert py_cw.imult([], []) == []

    assert py_cw.imult([], [2]) == []
    assert py_cw.imult([2], []) == []

    assert py_cw.imult([5], [2]) == [0,1]
    assert py_cw.imult([2], [5]) == [0,1]

    assert py_cw.imult([2,1], [2]) == [4,2]
    assert py_cw.imult([2], [2,1]) == [4,2]

    assert py_cw.imult([2,1], [2,1]) == [4,4,1]

def test_q11_ipow():
    assert py_cw.ipow([], []) == [1]

    assert py_cw.ipow([], [2]) == []
    assert py_cw.ipow([2], []) == [1]

    assert py_cw.ipow([5], [2]) == [5,2]
    assert py_cw.ipow([2], [5]) == [2,3]

    assert py_cw.ipow([2,1], [2]) == [4,4,1]
    assert py_cw.ipow([2], [2,1]) == [6,9,0,4]
    
    assert py_cw.ipow([2,1], [2,1]) == py_cw.iint(12**12)

# At this level you should be providing your own tests

## Q12

def test_q12_abstractsize():
    assert py_cw.abstractsize(5) == 1
    assert py_cw.abstractsize([5]) == 2
    assert py_cw.abstractsize([5,5]) == 3
    assert py_cw.abstractsize([5,5,[5]]) == 5
    assert py_cw.abstractsize([5,[5,5],[[[5,5]]]]) == 10

def test_q12_compress():
    assert py_cw.compress([5,[5,5],[[[5,5]]]]) == [5,5,5,5,5]
    assert py_cw.compress([5,5,[5]]) == [5,5,5]
    assert py_cw.compress([5,5]) == [5,5]
    assert py_cw.compress([5]) == 5
    assert py_cw.compress(5) == 5
    assert py_cw.compress([1,1,[2,1,2,[3,2,1]],1,5,3]) == [1,1,2,1,2,3,2,1,1,5,3]

## Q13

def test_q13_equals23():
    assert py_cw.equals23(34) == False
    assert py_cw.equals23(23) == True
    assert len(py_cw.equals23Length) <= 23
