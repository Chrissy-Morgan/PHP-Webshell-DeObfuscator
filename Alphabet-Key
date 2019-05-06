import re

#Key
# PLEASE MAKE SURE THAT ALL HEX CODES ARE CORRECT. IF YOU HAVE ANY ERRORS ADD A 0 , FOR EXAMPLE \xd WILL BE \x0d . There are known occurances.

Alphabet=" ENTER ALPHABET HERE "

# this is the obfuscated code we need to extract the numbers from
obs = "ENTER TO OBFUSCATED CODE HERE"

# This will take all numbers and convert to the correct character.
# It will print to the console the converted code. Please copy this code for further conversion. 

# New Code
# ========

# First, find all the numbers that are contained within two square brackets
# e.g. the "[62]" in $tf7ebf['l94b537e'][62]
obs_numbers = re.findall(r'\[(\d+)\]', obs)
print "Identified numbers: {obs_numbers}".format(obs_numbers = obs_numbers)

# Loop through each number from the previous step, and replace every
# "[{num}]" with the char from the corresponding index in `Alphabet`

# As these are string values and not integers, PHP will be expecting them
# to appear in quotation marks, as if you had the value [a] - that would cause
# a syntax error in PHP.
processed_obs = obs
for num in obs_numbers:
  search_for = '[{num}]'.format(num = num)
  replace_with = "['{c}']".format(c = Alphabet[int(num)])
  processed_obs = processed_obs.replace(search_for, replace_with)
  print 'Replaced `{num}` with `{c}`'.format(num = num, c = Alphabet[int(num)])

print '------'
print 'Original: {obs}'.format(obs = obs)
print 'Processed: {obs}'.format(obs = processed_obs)

search_for2 = '[$GLOBALS[$GLOBALS]]'.format(obs = obs)
replace_with2 = "['{c}']".format(c = '')
processed_obs2 = processed_obs.replace(search_for2, replace_with2)

print 'Processed: {obs}'.format(obs = processed_obs2)
