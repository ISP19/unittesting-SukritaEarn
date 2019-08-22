## Unit Testing Assignment

by Bill Gates.


## Test Cases for unique

Write a table describing your test cases.

| Test case                             | Expected Result                          |
|---------------------------------------|-------------------------------------------|
| empty list                            | empty list                                |
| one item                              | list with 1 item                          |
| one item many times                   | list with 1 item                          |
| 2 items, many times, many orders      | 2 item list, items in same order          |
| no duplicated item                    | list with all items that are added        |  
| many items list                       | all items appear only once in same order  |
| two list but items inside are in      | list of 2 lists in same order             |
|          different order              |                                           |


## Test Cases for Fraction

| Test case                             | Expected Result                                    |
|---------------------------------------|----------------------------------------------------|
| str method                            | fraction in a proper form                          |
| init method                           | numerator and denominator in proper form           |
| add method                            | the sum of two fractions as a new fraction         |
| sub method                            | the difference of two fractions as a new fraction  |
| mul method                            | the product of two fractions as a new fraction     | 
| truediv method                        | the quotient of two fractions as a new fraction    |
| negative method                       | the fraction in a negative form as a new fraction  |
| equal method                          | True or False                                      |
| 0/0                                   | Indeterminate form                                 |
| 1/0                                   | Infinity                                           |
| -1/0                                  | -Infinity                                          | 
| didn't insert int to Fraction calss   | ValueError                                         |
| denominator is zero                   | 1/0 or -1/0                                        |
| numerator is zero                     | 0                                                  |
