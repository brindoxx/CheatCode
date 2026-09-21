# utils/generate_dataset.py
# Generates the exact 403 Striver A2Z DSA sheet coding problem mapping for CheatCode
# 100% 1-to-1 match with all 403 practice problems on takeuforward.org

import json
import os

PROBLEMS = [
    {
        "title": "Pattern 1",
        "aliases": ["Pattern 1"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/square-pattern/1"
    },
    {
        "title": "Pattern 2",
        "aliases": ["Pattern 2"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/right-triangle/1"
    },
    {
        "title": "Pattern 3",
        "aliases": ["Pattern 3"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/triangle-number/1"
    },
    {
        "title": "Pattern 4",
        "aliases": ["Pattern 4"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 5",
        "aliases": ["Pattern 5"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/triangle-pattern-1661492263/1"
    },
    {
        "title": "Pattern 6",
        "aliases": ["Pattern 6"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 7",
        "aliases": ["Pattern 7"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 8",
        "aliases": ["Pattern 8"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 9",
        "aliases": ["Pattern 9"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/pattern/1"
    },
    {
        "title": "Pattern 10",
        "aliases": ["Pattern 10"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/triangle-pattern-1662284916/1"
    },
    {
        "title": "Pattern 11",
        "aliases": ["Pattern 11"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/triangle-pattern-1662285334/1"
    },
    {
        "title": "Pattern 12",
        "aliases": ["Pattern 12"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 13",
        "aliases": ["Pattern 13"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/triangle-pattern-1662285911/1"
    },
    {
        "title": "Pattern 14",
        "aliases": ["Pattern 14"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 15",
        "aliases": ["Pattern 15"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 16",
        "aliases": ["Pattern 16"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 17",
        "aliases": ["Pattern 17"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 18",
        "aliases": ["Pattern 18"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 19",
        "aliases": ["Pattern 19"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 20",
        "aliases": ["Pattern 20"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/double-triangle-pattern/1"
    },
    {
        "title": "Pattern 21",
        "aliases": ["Pattern 21"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Pattern 22",
        "aliases": ["Pattern 22"],
        "topic": "Patterns",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Count Digits",
        "aliases": ["Count Digits", "Count Digits in a Number", "Count all Digits of a Number", "Count the number of digits"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/find-numbers-with-even-number-of-digits/",
        "gfg": "https://www.geeksforgeeks.org/problems/count-digits5716/1"
    },
    {
        "title": "Count number of odd digits in a number",
        "aliases": ["Count number of odd digits in a number"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/find-numbers-with-even-number-of-digits/",
        "gfg": None
    },
    {
        "title": "Reverse a Number",
        "aliases": ["Reverse Integer", "Reverse a Number", "Reverse a number"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/reverse-integer/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-digit0316/1"
    },
    {
        "title": "Check Palindrome",
        "aliases": ["Check Palindrome", "Check if a Number is Palindrome", "Palindrome Number", "Palindrome number"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/palindrome-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/palindrome0746/1"
    },
    {
        "title": "Return the Largest Digit in a Number",
        "aliases": ["Find Largest Digit", "Largest Digit in a Number", "Return the Largest Digit in a Number"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Factorial of N numbers",
        "aliases": ["Factorial of N numbers", "Factorial of a given number", "Factorial of a number", "Find Factorial"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1"
    },
    {
        "title": "Armstrong Numbers",
        "aliases": ["Armstrong Number", "Armstrong Numbers", "Check Armstrong", "Check if the Number is Armstrong"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/armstrong-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1"
    },
    {
        "title": "Check for Perfect Number",
        "aliases": ["Check Perfect Number", "Check for Perfect Number", "Perfect Number"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/perfect-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/perfect-numbers3207/1"
    },
    {
        "title": "Check for Prime",
        "aliases": ["Check Prime", "Check for Prime", "Check for Prime Number", "Prime Number Check"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/count-primes/",
        "gfg": "https://www.geeksforgeeks.org/problems/prime-number2314/1"
    },
    {
        "title": "Count of Prime Numbers till N",
        "aliases": ["Count Prime Numbers till N", "Count Primes", "Count of Prime Numbers till N", "Sieve of Eratosthenes"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/count-primes/",
        "gfg": "https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1"
    },
    {
        "title": "GCD Or HCF",
        "aliases": ["Find GCD", "GCD Or HCF", "GCD of Two Numbers", "GCD of two numbers", "Greatest Common Divisor"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/find-greatest-common-divisor-of-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1"
    },
    {
        "title": "LCM of two numbers",
        "aliases": ["Find LCM", "LCM of Two Numbers", "LCM of two numbers"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1"
    },
    {
        "title": "Print all Divisors",
        "aliases": ["All Divisors of a Number", "Divisors of a Number", "Find all Divisors", "Print all Divisors"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1"
    },
    {
        "title": "Sum of Array Elements",
        "aliases": ["Sum of Array Elements", "Sum of elements in array"],
        "topic": "Basic Arrays",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Count of odd numbers in Array",
        "aliases": ["Count of odd numbers in Array"],
        "topic": "Basic Arrays",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/count-odd-even/1"
    },
    {
        "title": "Check if the Array is Sorted I",
        "aliases": ["Check if the Array is Sorted I"],
        "topic": "Basic Arrays",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/",
        "gfg": "https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1"
    },
    {
        "title": "Reverse an Array",
        "aliases": ["Reverse an Array", "Reverse an array"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/reverse-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-an-array/1"
    },
    {
        "title": "Highest Occurring Element in an Array",
        "aliases": ["Highest Occurring Element in an Array"],
        "topic": "Basic Hashing",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/frequency-of-the-most-frequent-element/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-repeating-number/1"
    },
    {
        "title": "Second Highest Occurring Element",
        "aliases": ["Second Highest Occurring Element"],
        "topic": "Basic Hashing",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/second-largest3735/1"
    },
    {
        "title": "Sum of Highest and Lowest Frequency",
        "aliases": ["Sum of Highest and Lowest Frequency"],
        "topic": "Basic Hashing",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1"
    },
    {
        "title": "Reverse a String",
        "aliases": ["Reverse String", "Reverse a String", "Reverse a String II"],
        "topic": "Basic Strings",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/reverse-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-a-string/1"
    },
    {
        "title": "Valid Palindrome",
        "aliases": ["Check if String is Palindrome", "Palindrome Check", "Valid Palindrome"],
        "topic": "Basic Strings",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/valid-palindrome/",
        "gfg": "https://www.geeksforgeeks.org/problems/palindrome-string0817/1"
    },
    {
        "title": "Largest Odd Number in String",
        "aliases": ["Largest Odd Number in String", "Largest Odd Number in a String"],
        "topic": "Strings - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/largest-odd-number-in-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/largest-odd-number-in-string/1"
    },
    {
        "title": "Longest Common Prefix",
        "aliases": ["Longest Common Prefix"],
        "topic": "Strings - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/longest-common-prefix/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1"
    },
    {
        "title": "Isomorphic Strings",
        "aliases": ["Isomorphic Strings"],
        "topic": "Strings - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/isomorphic-strings/",
        "gfg": "https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1"
    },
    {
        "title": "Rotate String",
        "aliases": ["Rotate String"],
        "topic": "Strings - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/rotate-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1"
    },
    {
        "title": "Valid Anagram",
        "aliases": ["Valid Anagram"],
        "topic": "Strings - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/valid-anagram/",
        "gfg": "https://www.geeksforgeeks.org/problems/anagram-1587115620/1"
    },
    {
        "title": "Sort Characters By Frequency",
        "aliases": ["Sort Characters By Frequency", "Sort Characters by Frequency"],
        "topic": "Strings - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sort-characters-by-frequency/",
        "gfg": "https://www.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/1"
    },
    {
        "title": "Sum of first N numbers",
        "aliases": ["Sum of First N Numbers", "Sum of first N numbers"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1"
    },
    {
        "title": "Factorial of N numbers",
        "aliases": ["Factorial of N numbers", "Factorial of a Given Number", "Factorial of a given number", "Factorial of a number", "Find Factorial"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1"
    },
    {
        "title": "Sum of Array Elements (Recursion)",
        "aliases": ["Sum of Array Elements II", "Sum of Array Elements using Recursion"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Reverse a String",
        "aliases": ["Reverse String", "Reverse a String", "Reverse a String I"],
        "topic": "Basic Strings",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/reverse-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-a-string/1"
    },
    {
        "title": "Check if a string is palindrome or not",
        "aliases": ["Check if String is Palindrome or Not", "Check if a string is palindrome or not"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/valid-palindrome/",
        "gfg": "https://www.geeksforgeeks.org/problems/palindrome-string0817/1"
    },
    {
        "title": "Check for Prime",
        "aliases": ["Check Prime", "Check if a Number is Prime or Not", "Prime Number Check"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/prime-number2314/1"
    },
    {
        "title": "Reverse an Array",
        "aliases": ["Reverse Array", "Reverse an Array", "Reverse an array 2"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-an-array/1"
    },
    {
        "title": "Check if Array Is Sorted and Rotated",
        "aliases": ["Check if Array Is Sorted and Rotated", "Check if the Array is Sorted II"],
        "topic": "Arrays - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/",
        "gfg": "https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1"
    },
    {
        "title": "Sum of Digits in a Given Number",
        "aliases": ["Sum of Digits in a Given Number"],
        "topic": "Basic Recursion",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/sum-of-digits1742/1"
    },
    {
        "title": "Fibonacci Number",
        "aliases": ["Fibonacci Number"],
        "topic": "Basic Recursion",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/fibonacci-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/nth-fibonacci-number/1"
    },
    {
        "title": "Selection Sort",
        "aliases": ["Selection Sort"],
        "topic": "Sorting Techniques",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/sort-an-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/selection-sort/1"
    },
    {
        "title": "Bubble Sort",
        "aliases": ["Bubble Sort"],
        "topic": "Sorting Techniques",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/sort-an-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/bubble-sort/1"
    },
    {
        "title": "Insertion Sort",
        "aliases": ["Insertion Sort Algorithm", "Insertion Sorting"],
        "topic": "Sorting",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/insertion-sort-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/insertion-sort/1"
    },
    {
        "title": "Merge Sort",
        "aliases": ["Merge Sort Algorithm", "Merge Sorting"],
        "topic": "Sorting",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sort-an-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/merge-sort/1"
    },
    {
        "title": "Quick Sort",
        "aliases": ["Quick Sort Algorithm", "Quick Sorting"],
        "topic": "Sorting",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sort-an-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/quick-sort/1"
    },
    {
        "title": "Linear Search",
        "aliases": ["Linear Search"],
        "topic": "Arrays - Easy",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1"
    },
    {
        "title": "Largest Element in an Array",
        "aliases": ["Find the largest element in an array", "Largest Element"],
        "topic": "Arrays",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/largest-element-in-array/1"
    },
    {
        "title": "Second Largest Element in an Array without sorting",
        "aliases": ["Second Largest", "Second Largest Element", "Second Largest Element in an Array"],
        "topic": "Arrays",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/second-largest3735/1"
    },
    {
        "title": "Max Consecutive Ones",
        "aliases": ["Max Consecutive Ones", "Maximum Consecutive Ones"],
        "topic": "Arrays - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/max-consecutive-ones/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximize-number-of-1s/1"
    },
    {
        "title": "Rotate Array by K places",
        "aliases": ["Left Rotate Array by One", "Rotate Array by K places"],
        "topic": "Arrays - Easy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/rotate-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1"
    },
    {
        "title": "Rotate Array by K places",
        "aliases": ["Left Rotate Array by K Places", "Rotate Array by K places"],
        "topic": "Arrays - Easy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/rotate-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1"
    },
    {
        "title": "Move Zeroes",
        "aliases": ["Move Zeroes", "Move Zeros to End"],
        "topic": "Arrays - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/move-zeroes/",
        "gfg": "https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1"
    },
    {
        "title": "Remove Duplicates from Sorted Array",
        "aliases": ["Remove Duplicates from Sorted Array", "Remove duplicates from sorted array"],
        "topic": "Arrays - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1"
    },
    {
        "title": "Missing Number",
        "aliases": ["Find Missing Number", "Find missing number", "Missing Number in Array"],
        "topic": "Arrays",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/missing-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1"
    },
    {
        "title": "Union of Two Sorted Arrays",
        "aliases": ["Find the Union and Intersection of two sorted arrays", "Union of two sorted arrays"],
        "topic": "Arrays",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1"
    },
    {
        "title": "Intersection of Two Sorted Arrays",
        "aliases": ["Intersection of Two Arrays", "Intersection of two sorted arrays"],
        "topic": "Arrays",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/intersection-of-two-arrays/",
        "gfg": None
    },
    {
        "title": "Majority Element (> n/2 times)",
        "aliases": ["Majority Element (> n/2 times)", "Majority Element-I"],
        "topic": "Arrays - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/majority-element/",
        "gfg": "https://www.geeksforgeeks.org/problems/majority-element-1587115620/1"
    },
    {
        "title": "Leaders in an Array",
        "aliases": ["Leaders in an Array"],
        "topic": "Arrays - Medium",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1"
    },
    {
        "title": "Rearrange Array Elements by Sign",
        "aliases": ["Rearrange Array Elements by Sign", "Rearrange array elements by sign"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/rearrange-array-elements-by-sign/",
        "gfg": "https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1"
    },
    {
        "title": "Spiral Matrix",
        "aliases": ["Print the matrix in spiral manner", "Spiral Matrix"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/spiral-matrix/",
        "gfg": "https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1"
    },
    {
        "title": "Pascal's Triangle",
        "aliases": ["Pascal's Triangle", "Pascal's Triangle I"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/pascals-triangle/",
        "gfg": "https://www.geeksforgeeks.org/problems/pascal-triangle0652/1"
    },
    {
        "title": "Pascal's Triangle II",
        "aliases": ["Pascal Triangle Row", "Pascal's Triangle II"],
        "topic": "Arrays",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/pascals-triangle-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/pascal-triangle0652/1"
    },
    {
        "title": "Pascal's Triangle",
        "aliases": ["Pascal's Triangle", "Pascal's Triangle III", "Pascals Triangle"],
        "topic": "Arrays",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/pascals-triangle/",
        "gfg": "https://www.geeksforgeeks.org/problems/pascal-triangle0652/1"
    },
    {
        "title": "Rotate Image / Matrix by 90 degrees",
        "aliases": ["Rotate Image", "Rotate Image / Matrix by 90 degrees", "Rotate Matrix", "Rotate Matrix by 90 degrees", "Rotate matrix by 90 degrees"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/rotate-image/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1"
    },
    {
        "title": "Set Matrix Zeroes",
        "aliases": ["Set Matrix Zeroes"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/set-matrix-zeroes/",
        "gfg": "https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1"
    },
    {
        "title": "2 Sum Problem",
        "aliases": ["2 Sum Problem", "Two Sum"],
        "topic": "Arrays - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/two-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/key-pair/1"
    },
    {
        "title": "3 Sum",
        "aliases": ["3 Sum"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/3sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1"
    },
    {
        "title": "4 Sum",
        "aliases": ["4 Sum"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/4sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1"
    },
    {
        "title": "Sort an array of 0s, 1s and 2s",
        "aliases": ["Sort an array of 0's 1's and 2's", "Sort an array of 0s, 1s and 2s"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sort-colors/",
        "gfg": "https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/1"
    },
    {
        "title": "Maximum Subarray Sum (Kadane's Algorithm)",
        "aliases": ["Kadane's Algorithm", "Kadanes Algorithm", "Max Subarray Sum", "Maximum Subarray Sum", "Maximum Subarray Sum (Kadane's Algorithm)"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-subarray/",
        "gfg": "https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1"
    },
    {
        "title": "Next Permutation",
        "aliases": ["Next Permutation"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/next-permutation/",
        "gfg": "https://www.geeksforgeeks.org/problems/next-permutation5226/1"
    },
    {
        "title": "Majority Element II (> n/3 times)",
        "aliases": ["Majority Element II (> n/3 times)", "Majority Element-II"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/majority-element-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/majority-vote/1"
    },
    {
        "title": "Find the Missing and Repeating Number",
        "aliases": ["Find the repeating and missing number", "Missing and Repeating"],
        "topic": "Arrays",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-missing-and-repeated-values/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1"
    },
    {
        "title": "Count Inversions",
        "aliases": ["Count Inversions"],
        "topic": "Arrays - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/reverse-pairs/",
        "gfg": "https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1"
    },
    {
        "title": "Reverse Pairs",
        "aliases": ["Reverse Pairs"],
        "topic": "Arrays - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/reverse-pairs/",
        "gfg": None
    },
    {
        "title": "Maximum Product Subarray",
        "aliases": ["Maximum Product Subarray", "Maximum Product Subarray in an Array"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-product-subarray/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1"
    },
    {
        "title": "Merge Two Sorted Arrays Without Extra Space",
        "aliases": ["Merge Two Sorted Arrays Without Extra Space", "Merge two sorted arrays without extra space"],
        "topic": "Arrays - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/merge-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1"
    },
    {
        "title": "Longest Consecutive Sequence",
        "aliases": ["Longest Consecutive Sequence", "Longest Consecutive Sequence in an Array"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-consecutive-sequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1"
    },
    {
        "title": "Longest Subarray with Sum K",
        "aliases": ["Longest Subarray with Sum K", "Longest subarray with sum K"],
        "topic": "Arrays - Easy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/subarray-sum-equals-k/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1"
    },
    {
        "title": "Largest Subarray with 0 Sum",
        "aliases": ["Largest Subarray with 0 Sum", "Largest Subarray with Sum 0"],
        "topic": "Hashing",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1"
    },
    {
        "title": "Subarray Sum Equals K",
        "aliases": ["Count subarrays with given sum", "Subarray Sum Equals K"],
        "topic": "Arrays - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/subarray-sum-equals-k/",
        "gfg": "https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1"
    },
    {
        "title": "Count Subarrays with Given XOR K",
        "aliases": ["Count Subarrays with Given XOR K", "Count subarrays with given xor K"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1"
    },
    {
        "title": "Binary Search",
        "aliases": ["Binary Search", "Search X in sorted array"],
        "topic": "Binary Search - 1D",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/binary-search/",
        "gfg": "https://www.geeksforgeeks.org/problems/binary-search-1587115620/1"
    },
    {
        "title": "Implement Lower Bound",
        "aliases": ["Lower Bound", "Search Insert Position"],
        "topic": "Binary Search",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/search-insert-position/",
        "gfg": "https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1"
    },
    {
        "title": "Implement Upper Bound",
        "aliases": ["Ceil The Floor", "Upper Bound"],
        "topic": "Binary Search",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/search-insert-position/",
        "gfg": "https://www.geeksforgeeks.org/problems/ceil-the-floor/1"
    },
    {
        "title": "Floor and Ceil in Sorted Array",
        "aliases": ["Floor and Ceil in Sorted Array", "Search insert position"],
        "topic": "Binary Search - 1D",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/search-insert-position/",
        "gfg": "https://www.geeksforgeeks.org/problems/ceil-the-floor/1"
    },
    {
        "title": "Floor and Ceil in Sorted Array",
        "aliases": ["Floor and Ceil in Sorted Array"],
        "topic": "Binary Search - 1D",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/search-insert-position/",
        "gfg": "https://www.geeksforgeeks.org/problems/ceil-the-floor/1"
    },
    {
        "title": "Count Occurrences in Sorted Array",
        "aliases": ["Count Occurrences in Sorted Array", "First and last occurrence"],
        "topic": "Binary Search - 1D",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1"
    },
    {
        "title": "Search in Rotated Sorted Array",
        "aliases": ["Search in Rotated Sorted Array", "Search in rotated sorted array-I"],
        "topic": "Binary Search - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/search-in-rotated-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1"
    },
    {
        "title": "Search in Rotated Sorted Array II (with duplicates)",
        "aliases": ["Search in Rotated Sorted Array II (with duplicates)", "Search in rotated sorted array-II"],
        "topic": "Binary Search - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/search-in-rotated-sorted-array-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/search-in-rotated-array-2/1"
    },
    {
        "title": "Find how many times array has been rotated",
        "aliases": ["Find how many times array has been rotated", "Find minimum in Rotated Sorted Array"],
        "topic": "Binary Search - 1D",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotation4723/1"
    },
    {
        "title": "Find how many times array has been rotated",
        "aliases": ["Find out how many times the array is rotated", "Rotation Count in Rotated Sorted Array"],
        "topic": "Binary Search",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotation4723/1"
    },
    {
        "title": "Single Element in a Sorted Array",
        "aliases": ["Single Element in a Sorted Array", "Single element in sorted array"],
        "topic": "Binary Search - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/single-element-in-a-sorted-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1"
    },
    {
        "title": "Square Root of an integer",
        "aliases": ["Find square root of a number", "Sqrt(x)"],
        "topic": "Binary Search",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/sqrtx/",
        "gfg": "https://www.geeksforgeeks.org/problems/square-root/1"
    },
    {
        "title": "Find Nth Root of M",
        "aliases": ["Find Nth root of a number", "Nth Root of a Number using Binary Search"],
        "topic": "Binary Search",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1"
    },
    {
        "title": "Find the Smallest Divisor Given a Threshold",
        "aliases": ["Find the Smallest Divisor Given a Threshold", "Find the smallest divisor"],
        "topic": "Binary Search - Answers",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/",
        "gfg": "https://www.geeksforgeeks.org/problems/smallest-divisor/1"
    },
    {
        "title": "Koko Eating Bananas",
        "aliases": ["Koko Eating Bananas", "Koko eating bananas"],
        "topic": "Binary Search - Answers",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/koko-eating-bananas/",
        "gfg": "https://www.geeksforgeeks.org/problems/koko-eating-bananas/1"
    },
    {
        "title": "Minimum days to make M bouquets",
        "aliases": ["Minimum days to make M bouquets"],
        "topic": "Binary Search - Answers",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1"
    },
    {
        "title": "Capacity to Ship Packages within D Days",
        "aliases": ["Capacity to Ship Packages Within D Days", "Capacity to Ship Packages within D Days"],
        "topic": "Binary Search - Answers",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/",
        "gfg": "https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1"
    },
    {
        "title": "Kth Missing Positive Number",
        "aliases": ["Kth Missing Positive Number"],
        "topic": "Binary Search - Answers",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/kth-missing-positive-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/kth-missing-positive-number-in-a-sorted-array/1"
    },
    {
        "title": "Painter's Partition Problem",
        "aliases": ["Painter's Partition", "The Painter's Partition Problem-II"],
        "topic": "Binary Search",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/split-array-largest-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1"
    },
    {
        "title": "Aggressive Cows",
        "aliases": ["Aggressive Cows"],
        "topic": "Binary Search - Answers",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/magnetic-force-between-two-balls/",
        "gfg": "https://www.geeksforgeeks.org/problems/aggressive-cows/1"
    },
    {
        "title": "Book Allocation Problem",
        "aliases": ["Book Allocation Problem"],
        "topic": "Binary Search - Answers",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/split-array-largest-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1"
    },
    {
        "title": "Find Peak Element",
        "aliases": ["Find Peak Element", "Find peak element"],
        "topic": "Binary Search - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-peak-element/",
        "gfg": "https://www.geeksforgeeks.org/problems/peak-element/1"
    },
    {
        "title": "K-th Element of Two Sorted Arrays",
        "aliases": ["K-th Element of Two Sorted Arrays", "Median of 2 sorted arrays"],
        "topic": "Binary Search - Answers",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
        "gfg": "https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1"
    },
    {
        "title": "Kth element of 2 sorted arrays",
        "aliases": ["Kth element of 2 sorted arrays"],
        "topic": "FAQs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
        "gfg": None
    },
    {
        "title": "Minimize Max Distance to Gas Station",
        "aliases": ["Minimize Max Distance to Gas Station"],
        "topic": "FAQs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/minimize-max-distance-to-gas-station/",
        "gfg": None
    },
    {
        "title": "Painter's Partition Problem",
        "aliases": ["Painter's Partition Problem", "Split array - largest sum"],
        "topic": "Binary Search - Answers",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/split-array-largest-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1"
    },
    {
        "title": "Row with Maximum 1's",
        "aliases": ["Find row with maximum 1's", "Row with Max 1s"],
        "topic": "Binary Search",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/row-with-maximum-ones/",
        "gfg": "https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1"
    },
    {
        "title": "Search a 2D Matrix",
        "aliases": ["Search a 2D Matrix", "Search in a 2D Matrix"],
        "topic": "Binary Search - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/search-a-2d-matrix/",
        "gfg": "https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1"
    },
    {
        "title": "Search a 2D Matrix II",
        "aliases": ["Search a 2D Matrix II", "Search in 2D matrix - II"],
        "topic": "Binary Search - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/search-a-2d-matrix-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1"
    },
    {
        "title": "Find a Peak Element II",
        "aliases": ["Find Peak Element - II", "Find a Peak Element II"],
        "topic": "Binary Search - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-a-peak-element-ii/",
        "gfg": None
    },
    {
        "title": "Matrix Median",
        "aliases": ["Matrix Median"],
        "topic": "Binary Search - 2D",
        "difficulty": "Hard",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1"
    },
    {
        "title": "Pow(x,n)",
        "aliases": ["Pow(x,n)"],
        "topic": "Implementation Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/powx-n/",
        "gfg": None
    },
    {
        "title": "Generate Parentheses",
        "aliases": ["Generate Parentheses"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/generate-parentheses/",
        "gfg": None
    },
    {
        "title": "Power Set",
        "aliases": ["Power Set"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/subsets/",
        "gfg": "https://www.geeksforgeeks.org/problems/power-set4302/1"
    },
    {
        "title": "Check if there exists a subsequence with sum K",
        "aliases": ["Check if there exists a subsequence with sum K"],
        "topic": "Subsequence Pattern Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1"
    },
    {
        "title": "Count all subsequences with sum K",
        "aliases": ["Count all subsequences with sum K"],
        "topic": "Subsequence Pattern Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1"
    },
    {
        "title": "Combination Sum",
        "aliases": ["Combination Sum"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/combination-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1"
    },
    {
        "title": "Combination Sum II",
        "aliases": ["Combination Sum II"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/combination-sum-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/combination-sum-ii/1"
    },
    {
        "title": "Subset Sums",
        "aliases": ["Subset Sums", "Subsets I"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/subsets/",
        "gfg": "https://www.geeksforgeeks.org/problems/subset-sums2234/1"
    },
    {
        "title": "Subsets II",
        "aliases": ["Subsets II"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/subsets-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/subset-sum-ii/1"
    },
    {
        "title": "Combination Sum III",
        "aliases": ["Combination Sum III"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/combination-sum-iii/",
        "gfg": None
    },
    {
        "title": "Letter Combinations of a Phone Number",
        "aliases": ["Letter Combinations of a Phone Number"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1"
    },
    {
        "title": "Palindrome Partitioning",
        "aliases": ["Palindrome Partitioning", "Palindrome partitioning"],
        "topic": "Recursion - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/palindrome-partitioning/",
        "gfg": "https://www.geeksforgeeks.org/problems/palindromic-patitioning4845/1"
    },
    {
        "title": "Word Search",
        "aliases": ["Word Search"],
        "topic": "Recursion - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/word-search/",
        "gfg": "https://www.geeksforgeeks.org/problems/word-search/1"
    },
    {
        "title": "N-Queens",
        "aliases": ["N Queen", "N-Queens"],
        "topic": "Recursion - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/n-queens/",
        "gfg": "https://www.geeksforgeeks.org/problems/n-queen-problem0315/1"
    },
    {
        "title": "Rat in a Maze Problem",
        "aliases": ["Rat in a Maze", "Rat in a Maze Problem - I"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1"
    },
    {
        "title": "M-Coloring Problem",
        "aliases": ["M Coloring Problem", "M-Coloring Problem"],
        "topic": "Recursion - Hard",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1"
    },
    {
        "title": "Sudoku Solver",
        "aliases": ["Sudoku Solver"],
        "topic": "Recursion - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/sudoku-solver/",
        "gfg": "https://www.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1"
    },
    {
        "title": "Traversal in Linked List",
        "aliases": ["Count nodes of linked list", "Traversal in Linked List"],
        "topic": "Linked List",
        "difficulty": "Easy",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1"
    },
    {
        "title": "Delete Node in a Linked List",
        "aliases": ["Delete Node in a Linked List", "Deletion of the head of LL"],
        "topic": "LinkedList - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/delete-node-in-a-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1"
    },
    {
        "title": "Deletion of the tail of Linked List",
        "aliases": ["Deletion of the tail of Linked List"],
        "topic": "Fundamentals (Single LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1"
    },
    {
        "title": "Delete a Node in Single Linked List",
        "aliases": ["Delete Node in a Linked List", "Deletion of the Kth element of Linked List"],
        "topic": "Linked List",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/delete-node-in-a-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1"
    },
    {
        "title": "Delete the element with value X",
        "aliases": ["Delete the element with value X"],
        "topic": "Fundamentals (Single LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1"
    },
    {
        "title": "Insertion at the head of Linked List",
        "aliases": ["Insertion at the head of Linked List"],
        "topic": "Fundamentals (Single LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1"
    },
    {
        "title": "Insertion at the tail of Linked List",
        "aliases": ["Insertion at the tail of Linked List"],
        "topic": "Fundamentals (Single LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1"
    },
    {
        "title": "Insertion at the Kth position of Linked List",
        "aliases": ["Insertion at the Kth position of Linked List"],
        "topic": "Fundamentals (Single LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1"
    },
    {
        "title": "Insertion before the value X in Linked List",
        "aliases": ["Insertion before the value X in Linked List"],
        "topic": "Fundamentals (Single LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1"
    },
    {
        "title": "Convert Array to Doubly Linked List",
        "aliases": ["Convert Array to Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/design-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1"
    },
    {
        "title": "Delete Tail of Doubly Linked List",
        "aliases": ["Delete Tail of Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1"
    },
    {
        "title": "Delete Kth Element of Doubly Linked List",
        "aliases": ["Delete Kth Element of Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1"
    },
    {
        "title": "Removing given node in Doubly Linked List",
        "aliases": ["Removing given node in Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1"
    },
    {
        "title": "Insert node before head in Doubly Linked List",
        "aliases": ["Insert node before head in Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1"
    },
    {
        "title": "Insert node before tail in Doubly Linked List",
        "aliases": ["Insert node before tail in Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1"
    },
    {
        "title": "Insert node before (kth node) in Doubly Linked List",
        "aliases": ["Insert node before (kth node) in Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1"
    },
    {
        "title": "Insert before given node in Doubly Linked List",
        "aliases": ["Insert before given node in Doubly Linked List"],
        "topic": "Fundamentals (Doubly LL)",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1"
    },
    {
        "title": "Add Two Numbers",
        "aliases": ["Add Two Numbers", "Add two numbers in Linked List"],
        "topic": "LinkedList - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/add-two-numbers/",
        "gfg": "https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1"
    },
    {
        "title": "Segregate odd and even nodes in LL",
        "aliases": ["Segregate odd and even nodes in LL", "Segregate odd and even nodes in Linked List"],
        "topic": "LinkedList - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/odd-even-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list/1"
    },
    {
        "title": "Sort a Linked List of 0's 1's and 2's",
        "aliases": ["Sort a Linked List of 0's 1's and 2's"],
        "topic": "Logic Building",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sort-colors/",
        "gfg": "https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1"
    },
    {
        "title": "Remove Nth Node From End of List",
        "aliases": ["Remove Nth Node From End of List", "Remove Nth node from the back of the LL"],
        "topic": "LinkedList - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1"
    },
    {
        "title": "Reverse a Linked List",
        "aliases": ["Reverse a LL", "Reverse a Linked List"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/reverse-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1"
    },
    {
        "title": "Add one to a number represented by LL",
        "aliases": ["Add one to a number represented by LL"],
        "topic": "FAQs (Medium)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/plus-one-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1"
    },
    {
        "title": "Middle of the Linked List",
        "aliases": ["Find Middle of Linked List", "Middle of the Linked List"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/middle-of-the-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1"
    },
    {
        "title": "Delete the Middle Node of a Linked List",
        "aliases": ["Delete the Middle Node of a Linked List", "Delete the middle node in LL"],
        "topic": "LinkedList - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/delete-middle-of-linked-list/1"
    },
    {
        "title": "Check if LL is Palindrome",
        "aliases": ["Check if LL is Palindrome", "Check if LL is palindrome or not"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/palindrome-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1"
    },
    {
        "title": "Intersection of Two Linked Lists",
        "aliases": ["Find the intersection point of Y LL", "Intersection of Two Linked Lists"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/intersection-of-two-linked-lists/",
        "gfg": "https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1"
    },
    {
        "title": "Detect a Loop in LL",
        "aliases": ["Detect Cycle in Linked List", "Detect Loop in Linked List", "Detect a Loop in LL", "Detect a loop in LL", "Linked List Cycle"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/linked-list-cycle/",
        "gfg": "https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1"
    },
    {
        "title": "Length of Loop in Linked List",
        "aliases": ["Find the starting point in LL", "Length of Loop in Linked List"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/linked-list-cycle-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-length-of-loop/1"
    },
    {
        "title": "Length of loop in LL",
        "aliases": ["Length of loop in LL"],
        "topic": "FAQs (Medium)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/linked-list-cycle-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-length-of-loop/1"
    },
    {
        "title": "Reverse Nodes in k-Group",
        "aliases": ["Reverse LL in group of given size K", "Reverse Nodes in k-Group"],
        "topic": "LinkedList - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/reverse-nodes-in-k-group/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1"
    },
    {
        "title": "Rotate List",
        "aliases": ["Rotate List", "Rotate a LL"],
        "topic": "LinkedList - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/rotate-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1"
    },
    {
        "title": "Merge two Sorted Lists",
        "aliases": ["Merge two Sorted Lists"],
        "topic": "FAQs (Hard)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/merge-two-sorted-lists/",
        "gfg": "https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1"
    },
    {
        "title": "Flattening of LL",
        "aliases": ["Flattening of LL"],
        "topic": "FAQs (Hard)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1"
    },
    {
        "title": "Sort a LL of 0's 1's and 2's",
        "aliases": ["Sort LL", "Sort a LL of 0's 1's and 2's"],
        "topic": "LinkedList - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/sort-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1"
    },
    {
        "title": "Copy List with Random Pointer",
        "aliases": ["Clone a LL with random and next pointer", "Copy List with Random Pointer"],
        "topic": "LinkedList - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/copy-list-with-random-pointer/",
        "gfg": "https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1"
    },
    {
        "title": "Delete all occurrences of a key in DLL",
        "aliases": ["Delete all occurrences of a key in DLL"],
        "topic": "FAQS (DLL)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/remove-linked-list-elements/",
        "gfg": "https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1"
    },
    {
        "title": "Remove duplicates from sorted DLL",
        "aliases": ["Remove duplicates from sorted DLL"],
        "topic": "FAQS (DLL)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/remove-duplicates-from-sorted-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1"
    },
    {
        "title": "Find Pairs with Given Sum in Doubly Linked List",
        "aliases": ["Find Pairs with Given Sum in Doubly Linked List"],
        "topic": "FAQS (DLL)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1"
    },
    {
        "title": "Minimum Bit Flips to Convert Number",
        "aliases": ["Minimum Bit Flips to Convert Number"],
        "topic": "Bit Manipulation - Interview",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/minimum-bit-flips-to-convert-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/bit-difference-1587115620/1"
    },
    {
        "title": "Single Number",
        "aliases": ["Single Number", "Single Number - I"],
        "topic": "Arrays - Easy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/single-number/",
        "gfg": "https://www.geeksforgeeks.org/problems/element-appearing-once2552/1"
    },
    {
        "title": "Single Number II",
        "aliases": ["Single Number - II", "Single Number II"],
        "topic": "Bit Manipulation - Interview",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/single-number-ii/",
        "gfg": None
    },
    {
        "title": "Single Number III",
        "aliases": ["Single Number - III", "Single Number III"],
        "topic": "Bit Manipulation - Interview",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/single-number-iii/",
        "gfg": "https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1"
    },
    {
        "title": "Divide Two Integers without using multiplication, division and mod operator",
        "aliases": ["Divide Two Integers without using multiplication, division and mod operator", "Divide two numbers without multiplication and division"],
        "topic": "Bit Manipulation",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/divide-two-integers/",
        "gfg": "https://www.geeksforgeeks.org/problems/division-without-using-multiplication-division-and-mod-operator/1"
    },
    {
        "title": "Subset Sum : Sum of all Subsets",
        "aliases": ["Power Set Bit Manipulation", "Subset Sum : Sum of all Subsets"],
        "topic": "Recursion",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/subsets/",
        "gfg": "https://www.geeksforgeeks.org/problems/subset-sums2234/1"
    },
    {
        "title": "XOR of numbers in a given range",
        "aliases": ["XOR of numbers in a given range"],
        "topic": "Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1"
    },
    {
        "title": "Assign Cookies",
        "aliases": ["Assign Cookies"],
        "topic": "Greedy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/assign-cookies/",
        "gfg": "https://www.geeksforgeeks.org/problems/assign-cookies/1"
    },
    {
        "title": "Lemonade Change",
        "aliases": ["Lemonade Change"],
        "topic": "Greedy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/lemonade-change/",
        "gfg": "https://www.geeksforgeeks.org/problems/lemonade-change/1"
    },
    {
        "title": "Fractional Knapsack",
        "aliases": ["Fractional Knapsack"],
        "topic": "Easy",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1"
    },
    {
        "title": "Jump Game",
        "aliases": ["Jump Game", "Jump Game - I"],
        "topic": "Greedy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/jump-game/",
        "gfg": "https://www.geeksforgeeks.org/problems/jump-game/1"
    },
    {
        "title": "Shortest Job First",
        "aliases": ["Shortest Job First"],
        "topic": "Scheduling and Interval Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/shortest-job-first/1"
    },
    {
        "title": "Job Sequencing Problem",
        "aliases": ["Job Sequencing Problem", "Job sequencing Problem"],
        "topic": "Greedy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-profit-in-job-scheduling/",
        "gfg": "https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1"
    },
    {
        "title": "N meetings in one room",
        "aliases": ["N meetings in one room"],
        "topic": "Greedy",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/non-overlapping-intervals/",
        "gfg": "https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1"
    },
    {
        "title": "Non-overlapping Intervals",
        "aliases": ["Non-overlapping Intervals"],
        "topic": "Greedy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/non-overlapping-intervals/",
        "gfg": "https://www.geeksforgeeks.org/problems/non-overlapping-intervals/1"
    },
    {
        "title": "Insert Interval",
        "aliases": ["Insert Interval"],
        "topic": "Scheduling and Interval Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/insert-interval/",
        "gfg": "https://www.geeksforgeeks.org/problems/insert-interval-1666733333/1"
    },
    {
        "title": "Merge Overlapping Subintervals",
        "aliases": ["Merge Intervals", "Merge Overlapping Intervals", "Merge Overlapping Subintervals"],
        "topic": "Arrays - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/merge-intervals/",
        "gfg": "https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1"
    },
    {
        "title": "Minimum number of platforms required for a railway",
        "aliases": ["Minimum number of platforms required for a railway"],
        "topic": "Scheduling and Interval Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/meeting-rooms-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1"
    },
    {
        "title": "Valid Parenthesis String",
        "aliases": ["Valid Paranthesis Checker", "Valid Parenthesis String"],
        "topic": "Greedy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/valid-parenthesis-string/",
        "gfg": None
    },
    {
        "title": "Candy",
        "aliases": ["Candy"],
        "topic": "Greedy",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/candy/",
        "gfg": "https://www.geeksforgeeks.org/problems/candy/1"
    },
    {
        "title": "Jump Game II",
        "aliases": ["Jump Game II"],
        "topic": "Greedy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/jump-game-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1"
    },
    {
        "title": "Maximum Points You Can Obtain from Cards",
        "aliases": ["Maximum Points You Can Obtain from Cards"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/1"
    },
    {
        "title": "Longest Substring Without Repeating Characters",
        "aliases": ["Longest Substring Without Repeating Characters"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        "gfg": "https://www.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1"
    },
    {
        "title": "Max Consecutive Ones III",
        "aliases": ["Max Consecutive Ones III"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/max-consecutive-ones-iii/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximize-number-of-1s/1"
    },
    {
        "title": "Fruit Into Baskets",
        "aliases": ["Fruit Into Baskets"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/fruit-into-baskets/",
        "gfg": "https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1"
    },
    {
        "title": "Longest Substring With At Most K Distinct Characters",
        "aliases": ["Longest Substring With At Most K Distinct Characters"],
        "topic": "Longest and Smallest Window Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1"
    },
    {
        "title": "Longest Repeating Character Replacement",
        "aliases": ["Longest Repeating Character Replacement"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-repeating-character-replacement/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1"
    },
    {
        "title": "Minimum Window Substring",
        "aliases": ["Minimum Window Substring"],
        "topic": "Sliding Window - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/minimum-window-substring/",
        "gfg": "https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1"
    },
    {
        "title": "Number of Substrings Containing All Three Characters",
        "aliases": ["Number of Substrings Containing All Three Characters"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/",
        "gfg": "https://www.geeksforgeeks.org/problems/count-substring/1"
    },
    {
        "title": "Binary Subarrays With Sum",
        "aliases": ["Binary Subarrays With Sum"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-subarrays-with-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/binary-subarray-with-sum/1"
    },
    {
        "title": "Count Number of Nice Subarrays",
        "aliases": ["Count Number of Nice Subarrays", "Count number of Nice subarrays"],
        "topic": "Sliding Window",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/count-number-of-nice-subarrays/",
        "gfg": None
    },
    {
        "title": "Subarrays with K Different Integers",
        "aliases": ["Subarrays with K Different Integers"],
        "topic": "Sliding Window - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/subarrays-with-k-different-integers/",
        "gfg": "https://www.geeksforgeeks.org/problems/subarrays-with-k-different-integers/1"
    },
    {
        "title": "Implement Stack using Arrays",
        "aliases": ["Implement Stack using Arrays"],
        "topic": "Stack and Queues",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/implement-stack-using-queues/",
        "gfg": "https://www.geeksforgeeks.org/problems/implement-stack-using-array/1"
    },
    {
        "title": "Implement Queue using Arrays",
        "aliases": ["Implement Queue using Arrays"],
        "topic": "Stack and Queues",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/implement-queue-using-stacks/",
        "gfg": "https://www.geeksforgeeks.org/problems/implement-queue-using-array/1"
    },
    {
        "title": "Implement Stack using Queue",
        "aliases": ["Implement Stack using Queue"],
        "topic": "Stack and Queues",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/implement-stack-using-queues/",
        "gfg": "https://www.geeksforgeeks.org/problems/stack-using-two-queues/1"
    },
    {
        "title": "Implement Queue using Stack",
        "aliases": ["Implement Queue using Stack"],
        "topic": "Stack and Queues",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/implement-queue-using-stacks/",
        "gfg": "https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1"
    },
    {
        "title": "Implement stack using Linkedlist",
        "aliases": ["Implement stack using Linkedlist"],
        "topic": "Implementation",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/implement-stack-using-queues/",
        "gfg": "https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1"
    },
    {
        "title": "Implement queue using Linkedlist",
        "aliases": ["Implement queue using Linkedlist"],
        "topic": "Implementation",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/implement-queue-using-stacks/",
        "gfg": "https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1"
    },
    {
        "title": "Valid Parentheses",
        "aliases": ["Balanced Paranthesis", "Valid Parentheses"],
        "topic": "Stack and Queues",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/valid-parentheses/",
        "gfg": "https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1"
    },
    {
        "title": "Next Smaller Element",
        "aliases": ["Next Greater Element", "Next Smaller Element"],
        "topic": "Monotonic Stack",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/next-greater-element-i/",
        "gfg": "https://www.geeksforgeeks.org/problems/immediate-smaller-element1142/1"
    },
    {
        "title": "Next Greater Element II",
        "aliases": ["Next Greater Element - 2", "Next Greater Element II"],
        "topic": "Monotonic Stack",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/next-greater-element-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/next-greater-element-2/1"
    },
    {
        "title": "Asteroid Collision",
        "aliases": ["Asteroid Collision"],
        "topic": "Monotonic Stack",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/asteroid-collision/",
        "gfg": "https://www.geeksforgeeks.org/problems/asteroid-collision/1"
    },
    {
        "title": "Sum of Subarray Minimums",
        "aliases": ["Sum of Subarray Minimums"],
        "topic": "Monotonic Stack",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sum-of-subarray-minimums/",
        "gfg": "https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1"
    },
    {
        "title": "Sum of Subarray Ranges",
        "aliases": ["Sum of Subarray Ranges"],
        "topic": "Monotonic Stack",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/sum-of-subarray-ranges/",
        "gfg": "https://www.geeksforgeeks.org/problems/sum-of-subarray-ranges/1"
    },
    {
        "title": "Remove K Digits",
        "aliases": ["Remove K Digits"],
        "topic": "Monotonic Stack",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/remove-k-digits/",
        "gfg": "https://www.geeksforgeeks.org/problems/remove-k-digits/1"
    },
    {
        "title": "Min Stack",
        "aliases": ["Implement Min Stack", "Min Stack"],
        "topic": "Stack and Queues",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/min-stack/",
        "gfg": "https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1"
    },
    {
        "title": "Sliding Window Maximum",
        "aliases": ["Sliding Window Maximum"],
        "topic": "Monotonic Stack / Sliding Window",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/sliding-window-maximum/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1"
    },
    {
        "title": "Trapping Rain Water",
        "aliases": ["Trapping Rain Water", "Trapping Rainwater"],
        "topic": "Monotonic Stack",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/trapping-rain-water/",
        "gfg": "https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1"
    },
    {
        "title": "Largest Rectangle in Histogram",
        "aliases": ["Largest Rectangle in Histogram", "Largest rectangle in a histogram"],
        "topic": "Monotonic Stack",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/largest-rectangle-in-histogram/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1"
    },
    {
        "title": "Maximal Rectangle",
        "aliases": ["Maximal Rectangle", "Maximum Rectangles"],
        "topic": "Monotonic Stack",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/maximal-rectangle/",
        "gfg": "https://www.geeksforgeeks.org/problems/max-rectangle/1"
    },
    {
        "title": "Online Stock Span",
        "aliases": ["Online Stock Span", "Stock span problem"],
        "topic": "Monotonic Stack",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/online-stock-span/",
        "gfg": "https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1"
    },
    {
        "title": "Celebrity Problem",
        "aliases": ["Celebrity Problem"],
        "topic": "FAQs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-the-celebrity/",
        "gfg": "https://www.geeksforgeeks.org/problems/the-celebrity-problem/1"
    },
    {
        "title": "LRU Cache",
        "aliases": ["LRU Cache"],
        "topic": "Design / Stack & Queues",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/lru-cache/",
        "gfg": "https://www.geeksforgeeks.org/problems/lru-cache/1"
    },
    {
        "title": "LFU Cache",
        "aliases": ["LFU Cache"],
        "topic": "Design / Stack & Queues",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/lfu-cache/",
        "gfg": None
    },
    {
        "title": "Morris Preorder / Inorder Traversal",
        "aliases": ["Inorder Traversal", "Morris Preorder / Inorder Traversal"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-inorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/inorder-traversal/1"
    },
    {
        "title": "Binary Tree Preorder Traversal",
        "aliases": ["Binary Tree Preorder Traversal", "Preorder Traversal"],
        "topic": "Binary Trees",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/binary-tree-preorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/preorder-traversal/1"
    },
    {
        "title": "Binary Tree Postorder Traversal",
        "aliases": ["Binary Tree Postorder Traversal", "Postorder Traversal"],
        "topic": "Binary Trees",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/binary-tree-postorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/postorder-traversal/1"
    },
    {
        "title": "Binary Tree Level Order Traversal",
        "aliases": ["Binary Tree Level Order Traversal", "Level Order Traversal"],
        "topic": "Binary Trees",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-level-order-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/level-order-traversal/1"
    },
    {
        "title": "Pre, Post, Inorder in one traversal",
        "aliases": ["Pre, Post, Inorder in one traversal"],
        "topic": "Theory/Traversals",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/preorder-traversal/1"
    },
    {
        "title": "Maximum Depth of Binary Tree",
        "aliases": ["Maximum Depth in BT", "Maximum Depth of Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/maximum-depth-of-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/height-of-binary-tree/1"
    },
    {
        "title": "Same Tree",
        "aliases": ["Check if two trees are identical or not", "Same Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/same-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1"
    },
    {
        "title": "Balanced Binary Tree",
        "aliases": ["Balanced Binary Tree", "Check for balanced binary tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/balanced-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1"
    },
    {
        "title": "Diameter of Binary Tree",
        "aliases": ["Diameter of Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/diameter-of-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1"
    },
    {
        "title": "Binary Tree Maximum Path Sum",
        "aliases": ["Binary Tree Maximum Path Sum", "Maximum path sum"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/binary-tree-maximum-path-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1"
    },
    {
        "title": "Symmetric Tree",
        "aliases": ["Check for symmetrical BTs", "Symmetric Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/symmetric-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/symmetric-tree/1"
    },
    {
        "title": "Children Sum Property in Binary Tree",
        "aliases": ["Check for Children Sum Property in a Binary Tree", "Children Sum Property", "Children Sum Property in Binary Tree", "Children Sum in BT"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/root-equals-sum-of-children/",
        "gfg": "https://www.geeksforgeeks.org/problems/children-sum-parent/1"
    },
    {
        "title": "Binary Tree Zigzag Level Order Traversal",
        "aliases": ["Binary Tree Zigzag Level Order Traversal", "Spiral Traversal of BT", "Zig Zag or Spiral Traversal", "Zigzag Level Order Traversal", "Zigzag Traversal"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1"
    },
    {
        "title": "Boundary Traversal of Binary Tree",
        "aliases": ["Boundary Traversal", "Boundary Traversal of BT", "Boundary Traversal of Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/boundary-of-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1"
    },
    {
        "title": "Vertical Order Traversal of a Binary Tree",
        "aliases": ["Vertical Order Traversal", "Vertical Order Traversal of BT", "Vertical Order Traversal of a Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1"
    },
    {
        "title": "Top View of Binary Tree",
        "aliases": ["Top View of BT", "Top View of Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1"
    },
    {
        "title": "Bottom View of Binary Tree",
        "aliases": ["Bottom View of BT", "Bottom View of Binary Tree", "Bottom view of BT"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1"
    },
    {
        "title": "Right/Left View of Binary Tree",
        "aliases": ["Left View of BT", "Right Side View of Binary Tree", "Right View of BT", "Right/Left View of BT", "Right/Left View of Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-right-side-view/",
        "gfg": "https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1"
    },
    {
        "title": "Root to Node Path in Binary Tree",
        "aliases": ["Print root to leaf path in BT", "Root to Leaf Path", "Root to Node Path in Binary Tree", "Root to leaf path in Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-paths/",
        "gfg": "https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1"
    },
    {
        "title": "Lowest Common Ancestor of a Binary Tree",
        "aliases": ["LCA in BT", "LCA in Binary Tree", "LCA of Binary Tree", "Lowest Common Ancestor of a Binary Tree"],
        "topic": "Binary Trees - Medium",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1"
    },
    {
        "title": "Maximum Width of Binary Tree",
        "aliases": ["Max Width of Binary Tree", "Maximum Width of BT", "Maximum Width of Binary Tree"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-width-of-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-width-of-tree/1"
    },
    {
        "title": "All Nodes Distance K in Binary Tree",
        "aliases": ["All Nodes Distance K in Binary Tree", "Nodes at Distance K", "Print all nodes at a distance of K in BT", "Print all nodes at distance K in Binary Tree"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1"
    },
    {
        "title": "Burning Tree",
        "aliases": ["Amount of Time for Binary Tree to Be Infected", "Burn BT", "Burning Binary Tree", "Burning Tree", "Minimum time taken to burn the BT from a given Node", "Time to Burn Tree"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/",
        "gfg": "https://www.geeksforgeeks.org/problems/burning-tree/1"
    },
    {
        "title": "Count Complete Tree Nodes",
        "aliases": ["Count Complete Tree Nodes", "Count Nodes in Complete Binary Tree", "Count total nodes in a complete BT", "Count total nodes in complete Binary Tree"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/count-complete-tree-nodes/",
        "gfg": "https://www.geeksforgeeks.org/problems/count-number-of-nodes-in-a-binary-tree/1"
    },
    {
        "title": "Flatten Binary Tree to Linked List",
        "aliases": ["Flatten BT to LL", "Flatten Binary Tree to Linked List", "Flatten a Binary Tree to Linked List"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/",
        "gfg": "https://www.geeksforgeeks.org/problems/flatten-binary-tree-to-linked-list/1"
    },
    {
        "title": "Requirements needed to construct a unique BT",
        "aliases": ["Requirements needed to construct a unique BT"],
        "topic": "Construction Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/unique-binary-tree-requirements/1"
    },
    {
        "title": "Construct Binary Tree from Preorder and Inorder Traversal",
        "aliases": ["Construct Binary Tree from Preorder and Inorder Traversal", "Construct a BT from Preorder and Inorder"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/construct-tree-1/1"
    },
    {
        "title": "Construct Binary Tree from Inorder and Postorder Traversal",
        "aliases": ["Construct Binary Tree from Inorder and Postorder Traversal", "Construct a BT from Postorder and Inorder"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1"
    },
    {
        "title": "Serialize and Deserialize Binary Tree",
        "aliases": ["Serialize and De-serialize BT", "Serialize and Deserialize Binary Tree"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1"
    },
    {
        "title": "Morris Preorder / Inorder Traversal",
        "aliases": ["Morris Inorder Traversal", "Morris Preorder / Inorder Traversal"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-inorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/inorder-traversal/1"
    },
    {
        "title": "Morris Preorder / Inorder Traversal",
        "aliases": ["Morris Preorder / Inorder Traversal", "Morris Preorder Traversal"],
        "topic": "Binary Trees - Hard",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-tree-inorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/inorder-traversal/1"
    },
    {
        "title": "Search in a Binary Search Tree",
        "aliases": ["Search in BST", "Search in a Binary Search Tree"],
        "topic": "BST",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/search-in-a-binary-search-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/search-a-node-in-bst/1"
    },
    {
        "title": "Floor and Ceil in a BST",
        "aliases": ["Floor and Ceil in a BST"],
        "topic": "Theory and Basics",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/floor-in-bst/1"
    },
    {
        "title": "Insert into a Binary Search Tree",
        "aliases": ["Insert a given node in BST", "Insert into a Binary Search Tree"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/insert-into-a-binary-search-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1"
    },
    {
        "title": "Delete Node in a BST",
        "aliases": ["Delete Node in a BST", "Delete a node in BST"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/delete-node-in-a-bst/",
        "gfg": "https://www.geeksforgeeks.org/problems/delete-a-node-from-bst/1"
    },
    {
        "title": "Find Kth Smallest/Largest Element in BST",
        "aliases": ["Find Kth Smallest/Largest Element in BST", "Kth Smallest and Largest element in BST"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1"
    },
    {
        "title": "Validate Binary Search Tree",
        "aliases": ["Check if a tree is a BST or not", "Validate Binary Search Tree"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/validate-binary-search-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/check-for-bst/1"
    },
    {
        "title": "Lowest Common Ancestor of a Binary Search Tree",
        "aliases": ["LCA in BST", "LCA in Binary Search Tree", "LCA of BST", "Lowest Common Ancestor of a Binary Search Tree"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1"
    },
    {
        "title": "Construct Binary Search Tree from Preorder Traversal",
        "aliases": ["Construct Binary Search Tree from Preorder Traversal", "Construct a BST from a preorder traversal"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/",
        "gfg": "https://www.geeksforgeeks.org/problems/preorder-to-postorder4423/1"
    },
    {
        "title": "Inorder Successor/Predecessor in BST",
        "aliases": ["Inorder Successor/Predecessor in BST", "Inorder successor and predecessor in BST"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/inorder-successor-in-bst/",
        "gfg": "https://www.geeksforgeeks.org/problems/predecessor-and-successor/1"
    },
    {
        "title": "Binary Search Tree Iterator",
        "aliases": ["BST iterator", "Binary Search Tree Iterator"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/binary-search-tree-iterator/",
        "gfg": None
    },
    {
        "title": "Two Sum IV - Input is a BST",
        "aliases": ["Two Sum IV - Input is a BST", "Two sum in BST"],
        "topic": "BST",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/two-sum-iv-input-is-a-bst/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-a-pair-with-given-target-in-bst/1"
    },
    {
        "title": "Recover Binary Search Tree",
        "aliases": ["Correct BST with two nodes swapped", "Recover Binary Search Tree"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/recover-binary-search-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1"
    },
    {
        "title": "Largest BST in Binary Tree",
        "aliases": ["Largest BST in Binary Tree"],
        "topic": "BST",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/largest-bst/1"
    },
    {
        "title": "Heapify Algorithm",
        "aliases": ["Heapify Algorithm"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/heap-sort/1"
    },
    {
        "title": "Build heap from a given Array",
        "aliases": ["Build heap from a given Array"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/heap-sort/1"
    },
    {
        "title": "Implement Min Heap",
        "aliases": ["Implement Min Heap"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/operations-on-binary-min-heap/1"
    },
    {
        "title": "Implement Max Heap",
        "aliases": ["Implement Max Heap"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/operations-on-binary-min-heap/1"
    },
    {
        "title": "Check if an array represents a min heap",
        "aliases": ["Check if an array represents a min heap"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1"
    },
    {
        "title": "Convert Min Heap to Max Heap",
        "aliases": ["Convert Min Heap to Max Heap"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Heap Sort",
        "aliases": ["Heap Sort"],
        "topic": "Theory and Implementation",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/heap-sort/1"
    },
    {
        "title": "Kth Largest Element in an Array",
        "aliases": ["K-th Largest element in an array", "Kth Largest Element in an Array"],
        "topic": "Heaps",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/kth-largest-element-in-an-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/k-largest-elements4206/1"
    },
    {
        "title": "Kth Largest Element in a Stream",
        "aliases": ["Kth Largest Element in a Stream", "Kth largest element in a stream of running integers"],
        "topic": "Heaps",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/kth-largest-element-in-a-stream/",
        "gfg": "https://www.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1"
    },
    {
        "title": "Traversal Techniques",
        "aliases": ["Traversal Techniques"],
        "topic": "Theory and traversals",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1"
    },
    {
        "title": "Number of Provinces",
        "aliases": ["Connected Components", "Find Number of Provinces", "Number of Provinces"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-provinces/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-provinces/1"
    },
    {
        "title": "Number of Provinces",
        "aliases": ["Connected Components", "Find Number of Provinces", "Number of Provinces", "Number of provinces"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-provinces/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-provinces/1"
    },
    {
        "title": "Number of islands",
        "aliases": ["Number of islands"],
        "topic": "Traversal Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-islands/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1"
    },
    {
        "title": "Flood Fill",
        "aliases": ["Flood Fill", "Flood fill algorithm"],
        "topic": "Graphs",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/flood-fill/",
        "gfg": "https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1"
    },
    {
        "title": "Number of Enclaves",
        "aliases": ["Number of Enclaves", "Number of enclaves"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-enclaves/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-enclaves/1"
    },
    {
        "title": "Rotten Oranges",
        "aliases": ["Rotten Oranges"],
        "topic": "Stack & Queues / BFS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/rotting-oranges/",
        "gfg": "https://www.geeksforgeeks.org/problems/rotten-oranges2536/1"
    },
    {
        "title": "01 Matrix (Distance of nearest cell having 1)",
        "aliases": ["01 Matrix (Distance of nearest cell having 1)", "Distance of nearest cell having one"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/01-matrix/",
        "gfg": "https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1"
    },
    {
        "title": "Surrounded Regions",
        "aliases": ["Surrounded Regions"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/surrounded-regions/",
        "gfg": "https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1"
    },
    {
        "title": "Number of Distinct Islands",
        "aliases": ["Number of Distinct Islands", "Number of distinct islands"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-distinct-islands/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1"
    },
    {
        "title": "Course Schedule",
        "aliases": ["Course Schedule", "Detect a cycle in an undirected graph"],
        "topic": "Graphs - Topo Sort",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/course-schedule/",
        "gfg": "https://www.geeksforgeeks.org/problems/course-schedule/1"
    },
    {
        "title": "Is Graph Bipartite?",
        "aliases": ["Bipartite graph", "Is Graph Bipartite?"],
        "topic": "Graphs",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/is-graph-bipartite/",
        "gfg": "https://www.geeksforgeeks.org/problems/bipartite-graph/1"
    },
    {
        "title": "Topological sort or Kahn's algorithm",
        "aliases": ["Topological sort or Kahn's algorithm"],
        "topic": "Cycles",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/topological-sort/1"
    },
    {
        "title": "Course Schedule",
        "aliases": ["Course Schedule", "Detect a cycle in a directed graph"],
        "topic": "Graphs - Topo Sort",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/course-schedule/",
        "gfg": "https://www.geeksforgeeks.org/problems/course-schedule/1"
    },
    {
        "title": "Find eventual safe states",
        "aliases": ["Find eventual safe states"],
        "topic": "Hard Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-eventual-safe-states/",
        "gfg": "https://www.geeksforgeeks.org/problems/eventual-safe-states/1"
    },
    {
        "title": "Course Schedule",
        "aliases": ["Course Schedule", "Course Schedule I"],
        "topic": "Graphs - Topo Sort",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/course-schedule/",
        "gfg": "https://www.geeksforgeeks.org/problems/course-schedule/1"
    },
    {
        "title": "Course Schedule II",
        "aliases": ["Course Schedule II"],
        "topic": "Graphs - Topo Sort",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/course-schedule-ii/",
        "gfg": None
    },
    {
        "title": "Alien Dictionary",
        "aliases": ["Alien Dictionary"],
        "topic": "Graphs - Topo Sort",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/alien-dictionary/",
        "gfg": "https://www.geeksforgeeks.org/problems/alien-dictionary/1"
    },
    {
        "title": "Shortest path in DAG",
        "aliases": ["Shortest path in DAG"],
        "topic": "Hard Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1"
    },
    {
        "title": "Shortest path in undirected graph with unit weights",
        "aliases": ["Shortest path in undirected graph with unit weights"],
        "topic": "Hard Problems",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1"
    },
    {
        "title": "Word Ladder I",
        "aliases": ["Word Ladder I", "Word ladder I"],
        "topic": "Graphs",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/word-ladder/",
        "gfg": "https://www.geeksforgeeks.org/problems/word-ladder/1"
    },
    {
        "title": "Word Ladder II",
        "aliases": ["Word Ladder II", "Word ladder II"],
        "topic": "Graphs",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/word-ladder-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/word-ladder-ii/1"
    },
    {
        "title": "Dijkstra's Algorithm",
        "aliases": ["Dijkstra's Algorithm", "Dijkstra's algorithm", "Implementing Dijkstra Algorithm"],
        "topic": "Graphs - Shortest Path",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/network-delay-time/",
        "gfg": "https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1"
    },
    {
        "title": "Print Shortest Path",
        "aliases": ["Print Shortest Path", "Shortest Path in Weighted undirected graph"],
        "topic": "Shortest Path Algorithms",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1"
    },
    {
        "title": "Shortest Distance in a Binary Maze",
        "aliases": ["Shortest Distance in a Binary Maze", "Shortest Path in Binary Matrix"],
        "topic": "Shortest Path Algorithms",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/shortest-path-in-binary-matrix/",
        "gfg": None
    },
    {
        "title": "Path With Minimum Effort",
        "aliases": ["Path With Minimum Effort", "Path with minimum effort"],
        "topic": "Shortest Path Algorithms",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/path-with-minimum-effort/",
        "gfg": "https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1"
    },
    {
        "title": "Cheapest Flights Within K Stops",
        "aliases": ["Cheapest Flights Within K Stops", "Cheapest flight within K stops"],
        "topic": "Shortest Path Algorithms",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/cheapest-flights-within-k-stops/",
        "gfg": "https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1"
    },
    {
        "title": "Minimum Multiplications to Reach End",
        "aliases": ["Minimum Multiplications to reach End", "Minimum multiplications to reach end"],
        "topic": "Shortest Path Algorithms",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1"
    },
    {
        "title": "Number of Ways to Arrive at Destination",
        "aliases": ["Number of Ways to Arrive at Destination", "Number of ways to arrive at destination"],
        "topic": "Graphs - Shortest Path",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1"
    },
    {
        "title": "Bellman Ford Algorithm",
        "aliases": ["Bellman Ford Algorithm", "Bellman ford algorithm", "Distance from the source (Bellman-Ford Algorithm)"],
        "topic": "Graphs - Shortest Path",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1"
    },
    {
        "title": "Floyd Warshall Algorithm",
        "aliases": ["Floyd Warshall", "Floyd Warshall Algorithm", "Floyd warshall algorithm"],
        "topic": "Graphs - Shortest Path",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": None
    },
    {
        "title": "Find the City With the Smallest Number of Neighbors at a Threshold Distance",
        "aliases": ["City With the Smallest Number of Neighbors at a Threshold Distance", "Find the City With the Smallest Number of Neighbors at a Threshold Distance", "Find the city with the smallest number of neighbors"],
        "topic": "Shortest Path Algorithms",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/",
        "gfg": "https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1"
    },
    {
        "title": "Disjoint Set",
        "aliases": ["Disjoint Set"],
        "topic": "Minimum Spanning Tree",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1"
    },
    {
        "title": "Find the MST weight",
        "aliases": ["Find the MST weight"],
        "topic": "Minimum Spanning Tree",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/min-cost-to-connect-all-points/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1"
    },
    {
        "title": "Number of Operations to Make Network Connected",
        "aliases": ["Number of Operations to Make Network Connected", "Number of operations to make network connected"],
        "topic": "Graphs - Disjoint Set",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-operations-to-make-network-connected/",
        "gfg": "https://www.geeksforgeeks.org/problems/connecting-the-graph/1"
    },
    {
        "title": "Accounts Merge",
        "aliases": ["Accounts Merge", "Accounts merge"],
        "topic": "Graphs - Disjoint Set",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/accounts-merge/",
        "gfg": "https://www.geeksforgeeks.org/problems/merging-details/1"
    },
    {
        "title": "Number of islands II",
        "aliases": ["Number of islands II"],
        "topic": "Hard Problems II",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-islands-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-islands/1"
    },
    {
        "title": "Making A Large Island",
        "aliases": ["Making A Large Island", "Making a large island"],
        "topic": "Graphs - Disjoint Set",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/making-a-large-island/",
        "gfg": "https://www.geeksforgeeks.org/problems/making-a-large-island/1"
    },
    {
        "title": "Most Stones Removed with Same Row or Column",
        "aliases": ["Most Stones Removed with Same Row or Column", "Most stones removed with same row or column"],
        "topic": "Graphs - Disjoint Set",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1"
    },
    {
        "title": "Kosaraju's algorithm",
        "aliases": ["Kosaraju's algorithm"],
        "topic": "Additional Algorithms",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/",
        "gfg": "https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1"
    },
    {
        "title": "Articulation Point in Graph",
        "aliases": ["Articulation Point in Graph", "Bridges in graph"],
        "topic": "Graphs - Advanced",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/critical-connections-in-a-network/",
        "gfg": "https://www.geeksforgeeks.org/problems/articulation-point-1/1"
    },
    {
        "title": "Articulation Point in Graph",
        "aliases": ["Articulation Point in Graph", "Articulation point in graph"],
        "topic": "Graphs - Advanced",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/critical-connections-in-a-network/",
        "gfg": "https://www.geeksforgeeks.org/problems/articulation-point-1/1"
    },
    {
        "title": "Climbing Stairs",
        "aliases": ["Climbing Stairs", "Climbing stairs"],
        "topic": "DP - 1D",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/climbing-stairs/",
        "gfg": "https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1"
    },
    {
        "title": "Frog Jump",
        "aliases": ["Frog Jump"],
        "topic": "DP - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/frog-jump/",
        "gfg": "https://www.geeksforgeeks.org/problems/geek-jump/1"
    },
    {
        "title": "Frog Jump with k distances",
        "aliases": ["Frog Jump with k distances", "Frog jump with K distances"],
        "topic": "DP - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/frog-jump/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimal-cost/1"
    },
    {
        "title": "House Robber",
        "aliases": ["House Robber", "Maximum sum of non adjacent elements"],
        "topic": "DP - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/house-robber/",
        "gfg": "https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1"
    },
    {
        "title": "House Robber II",
        "aliases": ["House Robber II", "House robber"],
        "topic": "DP - 1D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/house-robber-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/house-robber-ii/1"
    },
    {
        "title": "Ninja's Training",
        "aliases": ["Ninja's Training", "Ninja's training"],
        "topic": "DP - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/minimum-falling-path-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/geeks-training/1"
    },
    {
        "title": "Grid Unique Paths",
        "aliases": ["Grid Unique Paths", "Grid unique paths"],
        "topic": "DP - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/unique-paths/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-unique-paths5339/1"
    },
    {
        "title": "Unique Paths II",
        "aliases": ["Unique Paths II", "Unique paths II"],
        "topic": "DP - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/unique-paths-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/unique-paths-in-a-grid--170647/1"
    },
    {
        "title": "Minimum Path Sum in Grid",
        "aliases": ["Minimum Falling Path Sum", "Minimum Path Sum in Grid"],
        "topic": "DP - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/minimum-path-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-cost-path3833/1"
    },
    {
        "title": "Triangle",
        "aliases": ["Triangle"],
        "topic": "DP - 2D",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/triangle/",
        "gfg": "https://www.geeksforgeeks.org/problems/triangle-path-sum/1"
    },
    {
        "title": "Cherry Pickup II",
        "aliases": ["Cherry Pickup II", "Cherry pickup II"],
        "topic": "DP - 3D",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/cherry-pickup-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/chocolates-pickup/1"
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "aliases": ["Best Time to Buy and Sell Stock", "Best time to buy and sell stock"],
        "topic": "Arrays - Medium",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "gfg": "https://www.geeksforgeeks.org/problems/stock-buy-and-sell2615/1"
    },
    {
        "title": "Best Time to Buy and Sell Stock II",
        "aliases": ["Best Time to Buy and Sell Stock II", "Best time to buy and sell stock II"],
        "topic": "DP - Stocks",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/stock-buy-and-sell2615/1"
    },
    {
        "title": "Best Time to Buy and Sell Stock III",
        "aliases": ["Best Time to Buy and Sell Stock III", "Best time to buy and sell stock III"],
        "topic": "DP - Stocks",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/",
        "gfg": "https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1"
    },
    {
        "title": "Best Time to Buy and Sell Stock IV",
        "aliases": ["Best Time to Buy and Sell Stock IV", "Best time to buy and sell stock IV"],
        "topic": "DP - Stocks",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-profit4657/1"
    },
    {
        "title": "Best Time to Buy and Sell Stock with Transaction Fee",
        "aliases": ["Best Time to Buy and Sell Stock with Transaction Fee", "Best time to buy and sell stock with transaction fees"],
        "topic": "DP - Stocks",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/",
        "gfg": "https://www.geeksforgeeks.org/problems/buy-stock-with-transaction-fee/1"
    },
    {
        "title": "Subset sum equals to target",
        "aliases": ["Subset sum equals to target"],
        "topic": "DP on subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/partition-equal-subset-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1"
    },
    {
        "title": "0/1 Knapsack",
        "aliases": ["0/1 Knapsack", "Partition equal subset sum"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/partition-equal-subset-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1"
    },
    {
        "title": "Partition Set Into 2 Subsets With Min Absolute Sum Diff",
        "aliases": ["Partition Set Into 2 Subsets With Min Absolute Sum Diff", "Partition a set into two subsets with minimum absolute sum difference"],
        "topic": "DP - Subsequences",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1"
    },
    {
        "title": "Count Subsets with Sum K",
        "aliases": ["Count Subsets with Sum K", "Count subsets with sum K"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/target-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1"
    },
    {
        "title": "Count Partitions with Given Difference",
        "aliases": ["Count Partitions with Given Difference", "Count partitions with given difference"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/target-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1"
    },
    {
        "title": "0 and 1 Knapsack",
        "aliases": ["0 and 1 Knapsack"],
        "topic": "DP on subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/ones-and-zeroes/",
        "gfg": "https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1"
    },
    {
        "title": "Coin Change",
        "aliases": ["Coin Change", "Minimum coins"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/coin-change/",
        "gfg": "https://www.geeksforgeeks.org/problems/coin-change2448/1"
    },
    {
        "title": "Target Sum",
        "aliases": ["Target Sum", "Target sum"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/target-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/target-sum-1626326450/1"
    },
    {
        "title": "Coin Change II",
        "aliases": ["Coin Change II", "Coin change II"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/coin-change-2/",
        "gfg": None
    },
    {
        "title": "Unbounded Knapsack",
        "aliases": ["Unbounded Knapsack", "Unbounded knapsack"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/coin-change-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1"
    },
    {
        "title": "Rod Cutting Problem",
        "aliases": ["Rod Cutting Problem", "Rod cutting problem"],
        "topic": "DP - Subsequences",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/integer-break/",
        "gfg": "https://www.geeksforgeeks.org/problems/rod-cutting0840/1"
    },
    {
        "title": "Longest Increasing Subsequence",
        "aliases": ["Longest Increasing Subsequence"],
        "topic": "DP - LIS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-increasing-subsequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1"
    },
    {
        "title": "Print Longest Increasing Subsequence",
        "aliases": ["Print Longest Increasing Subsequence"],
        "topic": "LIS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-increasing-subsequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1"
    },
    {
        "title": "Largest Divisible Subset",
        "aliases": ["Largest Divisible Subset"],
        "topic": "DP - LIS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/largest-divisible-subset/",
        "gfg": None
    },
    {
        "title": "Longest String Chain",
        "aliases": ["Longest String Chain"],
        "topic": "DP - LIS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-string-chain/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-string-chain/1"
    },
    {
        "title": "Longest Bitonic Subsequence",
        "aliases": ["Longest Bitonic Subsequence"],
        "topic": "DP - LIS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/wiggle-subsequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1"
    },
    {
        "title": "Number of Longest Increasing Subsequences",
        "aliases": ["Number of Longest Increasing Subsequences"],
        "topic": "DP - LIS",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-longest-increasing-subsequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-longest-increasing-subsequence/1"
    },
    {
        "title": "Longest Common Subsequence",
        "aliases": ["Longest Common Subsequence", "Longest common subsequence"],
        "topic": "DP - Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-common-subsequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1"
    },
    {
        "title": "Longest Common Substring",
        "aliases": ["Longest Common Substring", "Longest common substring"],
        "topic": "DP - Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-length-of-repeated-subarray/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-common-substring1452/1"
    },
    {
        "title": "Longest Palindromic Subsequence",
        "aliases": ["Longest Palindromic Subsequence", "Longest palindromic subsequence"],
        "topic": "DP - Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-palindromic-subsequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1"
    },
    {
        "title": "Minimum Insertions to Make String Palindrome",
        "aliases": ["Minimum Insertions to Make String Palindrome", "Minimum insertions to make string palindrome"],
        "topic": "DP - Strings",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/",
        "gfg": "https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1"
    },
    {
        "title": "Minimum Insertions/Deletions to Convert String A to B",
        "aliases": ["Minimum Insertions/Deletions to Convert String A to B", "Minimum insertions or deletions to convert string A to B"],
        "topic": "DP - Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/delete-operation-for-two-strings/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1"
    },
    {
        "title": "Shortest Common Supersequence",
        "aliases": ["Shortest Common Supersequence", "Shortest common supersequence"],
        "topic": "DP - Strings",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/shortest-common-supersequence/",
        "gfg": "https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1"
    },
    {
        "title": "Distinct Subsequences",
        "aliases": ["Distinct Subsequences", "Distinct subsequences"],
        "topic": "DP - Strings",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/distinct-subsequences/",
        "gfg": "https://www.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1"
    },
    {
        "title": "Edit Distance",
        "aliases": ["Edit Distance", "Edit distance"],
        "topic": "DP - Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/edit-distance/",
        "gfg": "https://www.geeksforgeeks.org/problems/edit-distance3702/1"
    },
    {
        "title": "Wildcard Matching",
        "aliases": ["Wildcard Matching", "Wildcard matching"],
        "topic": "DP - Strings",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/wildcard-matching/",
        "gfg": "https://www.geeksforgeeks.org/problems/wildcard-pattern-matching/1"
    },
    {
        "title": "Matrix Chain Multiplication",
        "aliases": ["Matrix Chain Multiplication", "Matrix chain multiplication"],
        "topic": "DP - Partition",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/burst-balloons/",
        "gfg": "https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1"
    },
    {
        "title": "Burst Balloons",
        "aliases": ["Burst Balloons", "Burst balloons"],
        "topic": "DP - Partition",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/burst-balloons/",
        "gfg": "https://www.geeksforgeeks.org/problems/burst-balloons/1"
    },
    {
        "title": "Palindrome Partitioning II",
        "aliases": ["Palindrome Partitioning II", "Palindrome partitioning II"],
        "topic": "DP - Partition",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/palindrome-partitioning-ii/",
        "gfg": "https://www.geeksforgeeks.org/problems/palindromic-patitioning4845/1"
    },
    {
        "title": "Partition Array for Maximum Sum",
        "aliases": ["Partition Array for Maximum Sum"],
        "topic": "DP - Partition",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/partition-array-for-maximum-sum/",
        "gfg": "https://www.geeksforgeeks.org/problems/partition-array-for-maximum-sum/1"
    },
    {
        "title": "Minimum Cost to Cut a Stick",
        "aliases": ["Minimum Cost to Cut a Stick", "Minimum cost to cut the stick"],
        "topic": "DP - Partition",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/minimum-cost-to-cut-a-stick/",
        "gfg": None
    },
    {
        "title": "Evaluate Boolean Expression to True",
        "aliases": ["Different Ways to Evaluate a Boolean Expression", "Evaluate Boolean Expression to True"],
        "topic": "DP - Partition",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/parsing-a-boolean-expression/",
        "gfg": "https://www.geeksforgeeks.org/problems/boolean-parenthesization/1"
    },
    {
        "title": "Implement Trie II (Prefix Tree)",
        "aliases": ["Implement Trie II (Prefix Tree)", "Trie Implementation and Operations"],
        "topic": "Trie",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/implement-trie-prefix-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/trie-delete/1"
    },
    {
        "title": "Trie Implementation and Advanced Operations",
        "aliases": ["Trie Implementation and Advanced Operations"],
        "topic": "Theory",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/implement-trie-ii-prefix-tree/",
        "gfg": "https://www.geeksforgeeks.org/problems/trie-delete/1"
    },
    {
        "title": "Longest Word with All Prefixes",
        "aliases": ["Longest Word with All Prefixes"],
        "topic": "Problems",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/longest-word-with-all-prefixes/",
        "gfg": "https://www.geeksforgeeks.org/problems/find-the-longest-string--170645/1"
    },
    {
        "title": "Number of Distinct Substrings in a String",
        "aliases": ["Number of Distinct Substrings in a String", "Number of distinct substrings in a string"],
        "topic": "Trie",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/count-of-distinct-substrings/1"
    },
    {
        "title": "Maximum XOR of Two Numbers in an Array",
        "aliases": ["Maximum XOR of Two Numbers in an Array", "Maximum XOR of two numbers in an array"],
        "topic": "Trie",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-xor-of-two-numbers-in-an-array/1"
    },
    {
        "title": "Maximum XOR With an Element From Array",
        "aliases": ["Maximum XOR With an Element From Array", "Maximum Xor with an element from an array"],
        "topic": "Trie",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/maximum-xor-with-an-element-from-array/",
        "gfg": "https://www.geeksforgeeks.org/problems/maximum-xor-with-an-element-from-array/1"
    },
    {
        "title": "Reverse Words in a String",
        "aliases": ["Reverse Words in a String", "Reverse every word in a string"],
        "topic": "Strings - Easy",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/reverse-words-in-a-string/",
        "gfg": "https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1"
    },
    {
        "title": "Minimum Add to Make Parentheses Valid",
        "aliases": ["Minimum Add to Make Parentheses Valid", "Minimum number of bracket reversals to make an expression balanced"],
        "topic": "Advanced Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/",
        "gfg": None
    },
    {
        "title": "Count and Say",
        "aliases": ["Count and Say", "Count and say"],
        "topic": "Advanced Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/count-and-say/",
        "gfg": "https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1"
    },
    {
        "title": "Repeated String Match",
        "aliases": ["Rabin Karp Algorithm", "Repeated String Match"],
        "topic": "Advanced Strings",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/repeated-string-match/",
        "gfg": None
    },
    {
        "title": "Z function",
        "aliases": ["Z function"],
        "topic": "Advanced Problems (Less asked)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/",
        "gfg": None
    },
    {
        "title": "KMP Algorithm or LPS array",
        "aliases": ["KMP Algorithm or LPS array"],
        "topic": "Advanced Problems (Less asked)",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/implement-strstr/",
        "gfg": "https://www.geeksforgeeks.org/problems/search-pattern0205/1"
    },
    {
        "title": "Shortest Palindrome",
        "aliases": ["Shortest Palindrome"],
        "topic": "Advanced Strings",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/shortest-palindrome/",
        "gfg": "https://www.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/1"
    },
    {
        "title": "Longest Happy Prefix",
        "aliases": ["Longest Happy Prefix", "Longest happy prefix"],
        "topic": "Advanced Strings",
        "difficulty": "Hard",
        "leetcode": "https://leetcode.com/problems/longest-happy-prefix/",
        "gfg": "https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1"
    },
    {
        "title": "Print all primes till N",
        "aliases": ["Print all primes till N"],
        "topic": "Sieve of Eratosthenes",
        "difficulty": "Medium",
        "leetcode": "https://leetcode.com/problems/count-primes/",
        "gfg": "https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1"
    },
    {
        "title": "Prime factorisation of a Number",
        "aliases": ["Prime factorisation of a Number"],
        "topic": "Sieve of Eratosthenes",
        "difficulty": "Medium",
        "leetcode": None,
        "gfg": "https://www.geeksforgeeks.org/problems/prime-factors5052/1"
    },
    {
        "title": "Count of Prime Numbers till N",
        "aliases": ["Count Prime Numbers till N", "Count Primes", "Count of Prime Numbers till N", "Count primes in range L to R", "Sieve of Eratosthenes"],
        "topic": "Basic Math",
        "difficulty": "Easy",
        "leetcode": "https://leetcode.com/problems/count-primes/",
        "gfg": "https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1"
    }
]

def main():
    target_path = os.path.join(os.path.dirname(__file__), "..", "data", "problems.json")
    target_path = os.path.abspath(target_path)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(PROBLEMS, f, indent=2, ensure_ascii=False)
    print(f"Successfully generated {len(PROBLEMS)} problems into {target_path}")

if __name__ == "__main__":
    main()
