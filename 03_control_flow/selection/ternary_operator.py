"""
Ternary operators are used for in-line conditional expressions. 
It's a one-line shorthand for an if-else statement and is often used for simple conditions. 
The basic syntax in many languages, including Python, follows the pattern:

[on_true] if [condition] else [on_false]

Here, [condition] is evaluated first. 
If it's true, the expression [on_true] is executed or returned; if it's false, [on_false] is executed or returned.

example, suppose we want to quickly determine and display status as either "High" or "Normal" based on a threshold. 
We can use the ternary operator to efficiently assign the status in a single line of code.
"""

temp = 123
status = "High" if temp > 78 else "Low"
print(status)


if temp > 78:
    print("High")
else:
    print("Low")