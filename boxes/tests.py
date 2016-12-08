"""
Path

Write a function that provides change directory (cd) function for an 
abstract file system.

Notes:

Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).
For example:

path = Path('/a/b/c/d')
print(path.cd('../x').current_path)
should display '/a/b/c/x'.

Note: Do not use built-in path-related functions. 


AreAnagramas

An anagram is a word formed from another by rearranging its letters, 
using all the original letters exactly once; for example, orchestra can
be rearranged into carthorse.

Write a function that checks if two words are anagrams of each other.

For example, are_anagrams('neural', 'unreal') should return true as arguments 
are anagrams of each other.


Palindrome

Write a function that checks if a given sentence is a palindrome. 
A palindrome is a word, phrase, verse, or sentence that reads the same 
ackward or forward. Only the order of English alphabet letters (A-Z and a-z) 
should be considered, other characters should be ignored.

For example, is_palindrome('Noel sees Leon.') should return true as 
spaces, period, and case should be ignored resulting with "noelseesleon" 
which is a palindrome since it reads same backward and forward.

"""

