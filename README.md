## Here is a small explanation of Kata from codeWars that I solved.
### Total solved kata: 37

---
# Are You Playing Banjo 
### Description:
Create a function which answers the question "Are you playing banjo?".  
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
```
name + " plays banjo" 
name + " does not play banjo"
```
Names given are always valid strings.

---
# Convert a Boolean to a String
### Description:
Implement a function which convert the given boolean value into its string representation.
Note: Only valid inputs will be given.

---

# Beginner Series #2 Clock
### Description:
Clock shows `h` hours, `m` minutes and `s` seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.
## Example:

```
h = 0
m = 1
s = 1

result = 61000
```
Input constraints:

- `0 <= h <= 23`
- `0 <= m <= 59`
- `0 <= s <= 59`
---
# Find Maximum and Minimum Values of a List
### Description:
Your task is to make two functions ( `max` and `min`, or `maximum` and `minimum`, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function returns one number.
### Examples (Input -> Output)
```
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
```
### Notes
- You may consider that there will not be any empty arrays/vectors.

---
# You only need one - Beginner
### Description:

You will be given an array `a` and a value `x`. All you need to do is check whether the provided array contains the value.

`a` can contain numbers or strings. `x` can be either.

Return `true` if the array contains the value, `false` if not.

---
# DNA to RNA Conversion
### Description:
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:
```
"GCAT"  =>  "GCAU"
```

The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of `'G'`, `'C'`, `'A'` and/or `'T'`.

---
# Sum of positive
### Description:
### Task
You get an array of numbers, return the sum of all of the positives ones.

### Example
- `[1, -4, 7, 12]` => 1+7+12=201+7+12=20
### Note
If there is nothing to sum, the sum is default to `0`.

---
# Count of positives / sum of negatives
### Description:

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

# Example

For input `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]`, you should return `[10, -65]`.

---
# Calculate BMI
### Description:
	Write function bmi that calculates body mass index (bmi = weight / height2).
	if bmi <= 18.5 return "Underweight"
	if bmi <= 25.0 return "Normal"
	if bmi <= 30.0 return "Overweight"
	if bmi > 30 return "Obese"

---
# Fake Binary
### Description:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
**Note: input will never be an empty string**

---
# Beginner Series #1 School Paperwork
### Description:
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need. If `n < 0` or `m < 0` return `0`.
### Example:
```
n= 5, m=5: 25
n=-5, m=5:  0
```

Waiting for translations and Feedback! Thanks!

---
# String repeat
### Description:
Write a function that accepts a non-negative integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.
### Examples (input -> output)

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

---
# Keep Hydrated!
### Description:
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded _down_.

For example:
```
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
```

---
# Quarter of the year

### Description:
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:
- `1 <= month <= 12`

---
# Square(n) Sum

### Description:

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for `[1, 2, 2]` it should return `9` because 1^2+2^2+2^2=9

---
# Convert boolean values to strings 'Yes' or 'No'.
### Description:
Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.
