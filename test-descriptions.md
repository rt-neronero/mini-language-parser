Test cases for the `.lt2` mini-programming language. These test cases cover variable declarations, print statements, conditionals, and comments to ensure the correct behavior of the language.

### Test Case 1: Simple Variable Declaration and Print
**Input:**
```
x : 10
pout(x)
pout(x + x)
pout(x + 5)
```
**Expected Output:**
```
10
20
15
```
**Explanation:**  
This test declares a variable `x` with the value `10` and prints it using `pout(x)`.

---

### Test Case 2: Multiple Variable Declaration and Print
**Input:**
```
a, b : 15
pout(a)
pout(b)
```
**Expected Output:**
```
15
15
```
**Explanation:**  
Both `a` and `b` are assigned the value `15`. The program should print the value of both variables.

---

### Test Case 3: Simple If Statement with Condition
**Input:**
```
x : 7
if x > 5
    pout(x)
```
**Expected Output:**
```
7
```
**Explanation:**  
Since `x` is greater than `5`, the if condition is true, and the value of `x` will be printed.

---

### Test Case 4: If-Elif-Else Statement
**Input:**
```
y : 5
if y > 10
    pout(y)
elif y == 5
    pout(y)
else
    // Nothing happens
```
**Expected Output:**
```
5
```
**Explanation:**  
The first condition (`y > 10`) is false, but the `elif` condition (`y == 5`) is true, so the value of `y` will be printed.

---

### Test Case 5: If-Else Block with No Elif
**Input:**
```
z : 3
if z > 5
    pout(z)
else
    pout(z)
```
**Expected Output:**
```
3
```
**Explanation:**  
Since `z` is not greater than `5`, the `else` block is executed and prints the value of `z`.

---

### Test Case 6: Using Arithmetic in Variable Declarations
**Input:**
```
x : 10 + 5
y : x * 2
pout(y)
```
**Expected Output:**
```
30
```
**Explanation:**  
The first expression assigns `x` the value `15`. Then, `y` is calculated as `x * 2` which results in `30`.

---

### Test Case 7: Nested Arithmetic in Expressions
**Input:**
```
a : (5 + 10) * 2
pout(a)
```
**Expected Output:**
```
30
```
**Explanation:**  
The expression in parentheses is evaluated first: `(5 + 10) = 15`, and then it is multiplied by `2`, giving `30`.

---

### Test Case 8: Comment Ignored in Execution
**Input:**
```
// This is a comment
x : 20
pout(x)
```
**Expected Output:**
```
20
```
**Explanation:**  
The comment line should be ignored, and only the value of `x` should be printed.

---

### Test Case 9: Variable Comparison in If-Statement
**Input:**
```
x : 4
y : 6
if x < y
    pout(x)
else
    pout(y)
```
**Expected Output:**
```
4
```
**Explanation:**  
Since `x < y` is true, the if block is executed, and `x` is printed.

---

### Test Case 10: Multiple Elif Conditions
**Input:**
```
a : 8
if a > 10
    pout(a)
elif a == 8
    pout(a)
elif a == 7
    pout(a)
else
    // No output
```
**Expected Output:**
```
8
```
**Explanation:**  
The second condition (`a == 8`) is true, so the value of `a` is printed, and no further conditions are checked.

---

### Test Case 11: Division and Subtraction in Expressions
**Input:**
```
x : 20 / 4
y : x - 2
pout(y)
```
**Expected Output:**
```
3
```
**Explanation:**  
`x` is calculated as `20 / 4 = 5`, then `y` is `x - 2 = 3`, so the value `3` is printed.

---

### Test Case 12: Printing Variables with the Same Value
**Input:**
```
a, b : 9
pout(a)
pout(b)
```
**Expected Output:**
```
9
9
```
**Explanation:**  
Both `a` and `b` are declared with the same value, so the program should print `9` twice.

---

These test cases cover a wide range of functionality, including variable declaration, arithmetic operations, conditional branching, and comments. You can use them to ensure the correct implementation of the `.lt2` language interpreter.