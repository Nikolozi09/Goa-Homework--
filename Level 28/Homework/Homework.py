#Sum of Two Numbers
#Write a function add_numbers(a, b) that takes two numbers and returns their sum.

#Check Even or Odd
#Write a function is_even(number) that returns True if a number is even, otherwise False.

#Find the Maximum
#Write a function find_max(a, b) that takes two numbers and returns the larger one.

#Write a function reverse_string(text) that takes a string and returns it reversed.

#Count Vowels in a String
#Write a function count_vowels(text) that counts and returns the number of vowels (a, e, i, o, u) in a given string.

#Check Divisibility
#Write a function is_divisible(a, b) that returns True if a is divisible by b, otherwise False.






def add_numbers(a, b):
    """დააბრუნებს 2-ის sum-ს"""
    return a + b


def is_even(number):
    """აბრუნებს True-ს თუ რიცხვი ლუწია, წინააღმდეგ შემთხვევაში False."""
    return number % 2 == 0


def find_max(a, b):
    """აბრუნებს ორი რიცხვიდან უფრო დიდს."""
    return max(a, b)


def reverse_string(text):
    """აბრუნებს შეყვანის სტრიქონის შებრუნებულ ვერსიას."""
    return text[::-1]


def count_vowels(text):
    """ითვლის და აბრუნებს ხმოვანთა რაოდენობას მოცემულ სტრიქონში.
    itvlis da abrunebs khmovan"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_divisible(a, b):
    """აბრუნებს True-ს, თუ "a" იყოფა "b"-ზე, წინააღმდეგ შემთხვევაში False."""
    return a % b == 0
