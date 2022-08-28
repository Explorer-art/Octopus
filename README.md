# Octopus
Octopus is a program for generating passwords according to the specified parameters and for bruteforce of hashes. The program has been adopted so far only for the Windows operating system.

Author: Truzme_

ATTENTION! DO NOT USE THIS PROGRAM FOR ILLEGAL PURPORES! IT's illegal!

Use: python Octopus.py [mode] [type] [instruction] [file] [bhash] [min] [max]

Example: python Octopus.py -m G -t N -f Passwords.txt 1 3

Help: python Octopus.py --help

Arguments:

min - The minimal lenght of the generated passwords.

max - The maximal lenght of the generated passwords.

mode - The mode of operation of the program.

type - Type of password generation.

instruction - Instructions for generating passwords.

file - The file where to save the generated passwords or the file where to get passwords for brute force MD5 hashes.

bhash - MD5 hash.

Modes:

G - Generating a passwords.

B - Bruteforce MD5 hashes.

Types for the mode "G":

N - Generation passswords from numbers only.

NL - Generation passwords from letters and numbers only.

NLS - Generation passwords from letters, numbers and signs.

I - Generate passwords according to your instructions.

Types for the mode "B":

MD5 - Hash MD5.

SHA1 - Hash SHA1.

SHA224 - Hash SHA224.

SHA256 - Hash SHA256.

SHA384 - Hash SHA384.

SHA512 - Hash SHA512.
