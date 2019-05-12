# PHP-Webshell-DeObfuscator

A Tool written in Python to help de-obfuscate the $GLOBALS type malware. 

Will work on malware: hexedglobals.3793 | Kidslug | php.obfuscated! | php.malware.GLOBALS.003 | php.malware.GLOBALS.004


# How does it work
The first part of the script will take the alphabet and will match it to the relevant number within the code.
Thanks to @iamrasting for his help on this part.
The remainder of the code will deobfuscate a file entered and produce the file output.txt after it has been processed.

## Instructions:

1. Find the hex alphabet within the code. 
it will look something like this  
```python
"\x59\x4f\x45\x54\x38\x3a\x23\x30\x24\x40\x3b\x7c\x2f\x37\x66\x42\x09\x35\x72\x43\x0a\x2a\x2e\x4c\x29\x6f\x2d\x53\x4e\x44\x34\x5b\x41\x4a\x33\x74\x68\x76\x4d\x3e\x60\x36\x26\x6b\x67\x56\x20\x32\x7e\x22\x7a\x61\x70\x28\x58\x6a\x27\x57\x71\x39\x25\x51\x46\x7d\x48\x5f\x5e\x73\x0d\x79\x2c\x62\x75\x5a\x78\x21\x2b\x4b\x63\x6c\x31\x50\x3f\x77\x47\x6e\x69\x3c\x64\x49\x6d\x65\x5d\x52\x3d\x5c\x7b\x55"
```
2. Copy and paste the alphabet into Alphabet Soup at the top.
3. Check that all hex characters are formed correctly they should all be in the format \x01

Where hex is not formed correctly ie \xd please add a starting 0, otherwise the code will fail.Look out for characters xd x9 and xa which seem to be the ones not correct.

TIP - IF YOU WANT NICE LOOKING CODE ON OUTPUT - STICK CODE PRIOR TO PROCESSING THROUGH A PHP FORMATTER

4. Enter the name of the webshell file in the 

```python
with open('globals.php') as infile:
    for obs in infile:
```
5. Run the script 
6. Open output.txt for your deobfuscated code. 


DEMO SCRIPT

I have experimental code where I have converted some further values in hex to python. https://repl.it/repls/UnlawfulGreatLinks
It is currently in devlopment, but you can insert the file in and hex alphabet and it will print out the file
- Not great formatting currently. This is a step closer to complete automation.


Enjoy
@5w0rdfish
