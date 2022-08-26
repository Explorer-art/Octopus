# Octopus
Octopus is a program for generating passwords according to the specified parameters.
The program has been adapted so far only for the Windows operating system.

Use: python Octopus.py [min] [max] [mode] [save]

Example: python Octopus.py 1 3 N -s s

Help: python Octopus.py --help

min - The minimal lenght of the generated passwords.

max - The maximal lenght of the generated passwords.

mode - Password generation mode.

save - Save the generated passwords to a file.

Modes:

N - Generation a passswords from numbers only.

NL - Generation a passwords from letters and numbers only.

NLS - Generation a passwords from letters, numbers and signs.
