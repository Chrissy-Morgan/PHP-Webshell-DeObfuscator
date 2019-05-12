###############################################
# Version  3                                  #
# Deobfuscation of numbers: @Iamrasting       #
# Deobfuscation of script: @5w0rdfish         #
###############################################

import re

#Key


Alphabet="\x5e\x71\x7c\x43\x7a\x6a\x23\x6d\x26\x2d\x44\x3c\x34\x27\x66\x52\x38\x4a\x29\x6f\x63\x35\x59\x0a\x51\x7e\x22\x3f\x6b\x2c\x65\x68\x61\x37\x4e\x09\x73\x3b\x76\x4d\x42\x7d\x7b\x55\x79\x4b\x56\x39\x2f\x77\x6c\x75\x6e\x2b\x78\x3d\x49\x4c\x24\x62\x21\x46\x31\x3a\x2a\x54\x70\x74\x45\x4f\x47\x64\x28\x5c\x2e\x30\x5d\x5b\x5f\x60\x3e\x67\x53\x32\x36\x69\x40\x5a\x20\x41\x57\x25\x58\x48\x0d\x50\x33\x72"
# this is the first part of obfuscated code we need to extract the numbers from


with open('globals.php') as infile:
    for obs in infile:
           
# New Code
# ========
# First, find all the numbers that are contained within two square brackets
# e.g. the "[62]" in $tf7ebf['l94b537e'][62]
      obs_numbers = re.findall(r'\[(\d+)\]', obs)
     # print "Identified numbers: {obs_numbers}".format(obs_numbers = obs_numbers)
  # Loop through each number from the previous step, and replace every
  # "[{num}]" with the char from the corresponding index in `Alphabet`
  # As these are string values and not integers, PHP will be expecting them
  
      
      processed_obs = obs
      for num in obs_numbers:
        search_for = '[{num}]'.format(num = num)
        replace_with = "['{c}']".format(c = Alphabet[int(num)])
        processed_obs = processed_obs.replace(search_for, replace_with)
      #  print 'Replaced `{num}` with `{c}`'.format(num = num, c = Alphabet[int(num)])
      print '------'
      
      
      #################################################################
      
      #find the variable defined as the Alphabet
      varName2 = re.findall(r'([\'([a-z]\w+)\'\]', processed_obs) 
      if len(varName2) > 1:
            
        alph = varName2[1]

      #turn to a string
      result = " ".join(str(x) for x in alph)
        
      print alph 
      #remove all not required 

      #return its name
      print ("#Alphabet " + str(alph))

      ################################################################     

      #find the variable defined as $GLOBALS
      varName = re.findall(r'\$([GLOBALS]\w+)\S\[\'([a-z]\w+)\'\]', processed_obs)
      #turn to a string
      result = " ".join(str(x) for x in varName)
      
      #remove all not required 
      bad_chars = [' ', ',','GLOBAL','[', ']','.','\''] 
      varName = result.translate(None, ''.join(bad_chars)) 
      #return its name
      print ("#$GLOBALS " + str(varName))
      print '------'
      ################################################################

    # We are going to remove all $GLOBALS that are not required 
      s = processed_obs
      e = {varName : ""}
      
      def find_replace_multi(string, dictionary):
          for item in dictionary.keys():
              # sub item for item's paired value in string
              string = re.sub(item, dictionary[item], string)
              return string
      string = find_replace_multi(s, e)

      # We are going to remove all $GLOBALS that are not required 
      s = string
      e = {alph : ""}
      
      def find_replace_multi(string, dictionary):
          for item in dictionary.keys():
              # sub item for item's paired value in string
              string = re.sub(item, dictionary[item], string)
              return string
      string = find_replace_multi(s, e)
      
      
      ##################################################################
      # We remove any other characters not required
      bad_chars = ['.','\''] 
      # Translate these to our blank space     
      string = string.translate(None, ''.join(bad_chars)) 
     
      #remove the extra $ signs
      string = re.sub("[(\[\])(\[.\])]", "", string)
      string = re.sub("[.(?<!\$)]", "", string)
     
      #Add new lines and spaces for formatting
      string = re.sub(";", ";\n", string)
      #Add new lines and spaces for formatting
      string = re.sub("global", ";\n", string)
      #Output to file
      f = open("output.txt","a+")
      
     # result = re.sub(r"(.*\w) = chr;", r"varible_1 = chr", string)
      
      print string
      
      
     # print string
      
      f.write(string)
     
f.close() 
infile.close()
print "\n ########################################################################## \n # Please open and view the output.txt, the deobufscated code is in there # \n ##########################################################################"
