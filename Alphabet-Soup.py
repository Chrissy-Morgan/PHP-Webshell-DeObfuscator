###############################################
# Version  3                                  #
# Deobfuscation of numbers: @Iamrasting       #
# Deobfuscation of script: @5w0rdfish         #
###############################################

import re

#Key

Alphabet="ENTER YOUR ALPHABET HERE"
# this is the first part of obfuscated code we need to extract the numbers from

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
   
      search_for2 = '[$GLOBALS[$GLOBALS]]'.format(obs = obs)
      replace_with2 = "['{c}']".format(c = '')
      processed_obs2 = processed_obs.replace(search_for2, replace_with2)

      #print 'Processed: {obs}'.format(obs = processed_obs2)

      string = processed_obs2
    
    # Deobfuscation of script
    # First remove newlines
      string = string.rstrip("\n\r")
    # We are going to remove all $GLOBALS that are not required 
      s = string
      e = {"\$([GLOBALS]\w+)\S\[\'([a-z]\w+)\'\]" : ""}

      def find_replace_multi(string, dictionary):
          for item in dictionary.keys():
              # sub item for item's paired value in string
              string = re.sub(item, dictionary[item], string)
              return string

      string = find_replace_multi(s, e)

      # We remove any other characters not required
      bad_chars = ['[', ']','.','\''] 
      # Translate these to our blank space     
      string = string.translate(None, ''.join(bad_chars)) 
      #Add new lines and spaces for formatting
      string = re.sub(";", ";\n", string)
      string = re.sub("\$([GLOBALS]\w+)", "$GLOBALS ", string)
      print ("Deobfuscated Code : " + string) 
      #Output to file
      f = open("output.txt","a+")
      
      f.write(string)
     
f.close() 

infile.close()

print "\n ########################################################################## \n # Please open and view the output.txt, the deobufscated code is in there # \n ##########################################################################"
