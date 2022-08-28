# Octopus
Octopus is a program for generating passwords according to the specified parameters and for bruteforce of MD5 hashes. The program has been adopted so far only for the Windows operating system.

ATTENTION! DO NOT USE THIS PROGRAM FOR ILLEGAL PURPORES! IT's illegal!

Use: python Octopus.py [mode] [type] [instruction] [file] [bhash] [min] [max]

Example: python Octopus.py -m G -t N -f Passwords.txt 1 3

Help: python Octopus.py --help

min - The minimal lenght of the generated passwords.

max - The maximal lenght of the generated passwords.

mode - Password generation mode.

save - Save the generated passwords to a file.

Modes:

G - Generating a passwords.

B - Bruteforce MD5 hashes.

Types for the mode "G":

N - Generation a passswords from numbers only.

NL - Generation a passwords from letters and numbers only.

NLS - Generation a passwords from letters, numbers and signs.
