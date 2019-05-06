###############################################
# Version  3                                  #
# Deobfuscation of numbers: @Iamrasting       #
# Deobfuscation of script: @5w0rdfish         #
###############################################

import re

#Key

Alphabet="\x59\x4f\x45\x54\x38\x3a\x23\x30\x24\x40\x3b\x7c\x2f\x37\x66\x42\x09\x35\x72\x43\x0a\x2a\x2e\x4c\x29\x6f\x2d\x53\x4e\x44\x34\x5b\x41\x4a\x33\x74\x68\x76\x4d\x3e\x60\x36\x26\x6b\x67\x56\x20\x32\x7e\x22\x7a\x61\x70\x28\x58\x6a\x27\x57\x71\x39\x25\x51\x46\x7d\x48\x5f\x5e\x73\x0d\x79\x2c\x62\x75\x5a\x78\x21\x2b\x4b\x63\x6c\x31\x50\x3f\x77\x47\x6e\x69\x3c\x64\x49\x6d\x65\x5d\x52\x3d\x5c\x7b\x55"

# this is the obfuscated code we need to extract the numbers from

obs = []

with open('globals.php') as infile:
    for obs in infile:
           
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
      #print 'Original: {obs}'.format(obs = obs)
      #print 'Processed: {obs}'.format(obs = processed_obs)

      search_for2 = '[$GLOBALS[$GLOBALS]]'.format(obs = obs)
      replace_with2 = "['{c}']".format(c = '')
      processed_obs2 = processed_obs.replace(search_for2, replace_with2)

      #print 'Processed: {obs}'.format(obs = processed_obs2)

      string = processed_obs2
      string = string.rstrip("\n\r")

      s = string
      e = {"\$([GLOBALS]\w+)\S\[\'([a-z]\w+)\'\]" : ""}

      def find_replace_multi(string, dictionary):
          for item in dictionary.keys():
              # sub item for item's paired value in string
              string = re.sub(item, dictionary[item], string)
              return string

      string = find_replace_multi(s, e)

      # initializing bad_chars_list 
      bad_chars = ['[', ']','.','\''] 
      # initializing test string  
      string = string
      # using translate() to  
      # remove bad_chars  
      string = string.translate(None, ''.join(bad_chars)) 

      string = re.sub(";", "\n", string)
      string = re.sub("\$([GLOBALS]\w+)", "$GLOBALS ", string)
      print ("Deobfuscated Code : " + string) 
    
      f = open("output.txt","a+")
      
      f.write(string)
     
f.close() 

infile.close()

print "\n ########################################################################## \n # Please open and view the output.txt, the deobufscated code is in there # \n ##########################################################################"
