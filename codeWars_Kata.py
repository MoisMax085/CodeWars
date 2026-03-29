# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].upper() == "R": return name + " plays banjo"
    else: return name + " does not play banjo"


# Convert a Boolean to a String
def boolean_to_string(b):return ("True" if b==1 else "False")


# Beginner Series #2 Clock
def past(h, m, s):
    return 1000*(s + m*60 + h*3600)


# Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)


# You only need one - Beginner
def check(seq, elem):
    return (True if elem in seq else False)


# DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace("T", "U")


# Sum of positive
def positive_sum(arr):
    return sum(x for x in arr if x >=0)


# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if len(arr) == 0:return []
    return [len([z for z in arr if z > 0]), sum(z for z in arr if z <= 0)]


# Calculate BMI
def bmi(weight, height):
    if weight/height**2 <= 18.5: return 'Underweight'
    elif 18.5 < weight/height**2 <= 25: return 'Normal'
    elif 25 < weight/height**2 <= 30: return 'Overweight'
    elif weight/height**2 > 30: return 'Obese'


# Fake Binary
def fake_bin(x):
    return x.replace("1", "0").replace("2", "0").replace("3", "0").replace("4", "0").replace("5", "1").replace("6", "1").replace("7", "1").replace("8", "1").replace("9", "1")


# Beginner Series #1 School Paperwork
def paperwork(n, m):
    return n*m if n >0 and m > 0 else 0


# String repeat
def repeat_str(repeat, string):
    return string*repeat


# Keep Hydrated!
def litres(time):
    return int(time*0.5)


# Quarter of the year
def quarter_of(month):
    if month <=3: return 1
    elif month <=6: return 2
    elif month <=9: return 3
    elif month <=12: return 4


# Square(n) Sum
def square_sum(numbers):
    return sum(x**2 for x in numbers)


# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Highest and Lowest
def high_and_low(numbers):
    return f'{max([int(x) for x in numbers.split(" ")])} {min([int(x) for x in numbers.split(" ")])}'


# Friend or Foe?
def friend(x):
    return [z for z in x if len(z)==4]

# Remove String Spaces
def no_space(x):
    return x.replace(" ", "")


# Number of People in the Bus
def number(bus_stops):
    return sum(x[0] for x in bus_stops)-sum(x[1] for x in bus_stops)


# A Needle in the Haystack
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"


# Beginner - Lost Without a Map
def maps(a):
    return [x*2 for x in a]


# Invert values
def invert(lst):
    return[x*(-1) for x in lst]


# Exes and Ohs
def xo(s):
    return True if (s.count("x")+s.count("X")) == (s.count("O") + s.count("o")) else False


# Sum of odd numbers
def row_sum_odd_numbers(n):
    first, summa = n*(n-1) + 1, 0
    for i in range(n):summa += first;first += 2
    return summa


# Get the Middle Character
def get_middle(s):
    return s[(len(s)-1)//2] + s[(len(s))//2] if len(s) % 2 == 0 else s[len(s)//2]


# Odd or Even?
def odd_or_even(arr):
    return "odd" if sum(arr) % 2 == 1 else "even"


# String ends with?
def solution(text, ending):
    return True if text[len(text)-len(ending):] == ending else False


# Opposite number
def opposite(number):
  return -1*number


# Is a number prime?
def is_prime(num):
    if num <= 1: return False
    if num == 2: return True
    for i in range(2, int(num**0.5)+2):
        if num % i == 0: return False
    return True


# Stop gninnipS My sdroW!
def spin_words(sentence):
    arr, st = sentence.split(" "), ""
    for x in arr:
        if len(x) >= 5:st += x[::-1] + " "
        else:st += x + " "
    return st[:-1]


# Rot13
def rot13(message):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    for i in message:
        if i in alphabet_lower:
            new_message += alphabet_lower[alphabet_lower.index(i) + 13]
        elif i in alphabet_upper:
            new_message += alphabet_upper[alphabet_upper.index(i) + 13]
        else:
            new_message += i
    return new_message


# First non-repeating character
def first_non_repeating_letter(s):
    for i in range(len(s.lower())):
        if s.lower().count(s.lower()[i]) == 1: return s[i]
    return ""


# Scramblies
def scramble(s1, s2):
    for i in set(s2):
        if s2.count(i) > s1.count(i): return False
    return True


# Sum of a sequence
def sequence_sum(begin_number, end_number, step):
    return sum([x for x in range(begin_number, end_number+1, step)])


#Extract the domain name from a URL
def domain_name(url):
    return url.replace("http://", "https://").replace("https://", "").replace("www.", "")[:url.replace("http://", "https://").replace("https://", "").replace("www.", "").index(".")]


# Make Me Slow
import time
def make_me_slow():
    time.sleep(7)
    pass