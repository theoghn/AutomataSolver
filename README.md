# AutomataSolver

## Description
* The script gets an automata as input and outputs every word that belongs to the DFA/NFA of max length N
* The backtick is used as lambda

## Input
```
#initial state
q0

#final states
q0 q2

#all the transitions
q0 1 q1
q0 2 q3
q1 1 q0
q6 ` q0
q0 ` q6
q6 ` q2
q2 ` q6
q2 2 q3
q2 0 q5
q5 0 q2
q3 2 q2
q3 2 q0
```

## Output for N = 4
```
['00', '11', '1111', '1122', '22', '2200', '2211', '2222']
```

