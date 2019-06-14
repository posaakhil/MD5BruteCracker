'''credits goeas to AkhilHacker '''

import md5

counter = 1

#this part of the code is used to prompt the user for input
 
pass_in = raw_input("PLEASE ENTER THE MD5 HASH(@AkhilHacker): ")
pwfile = raw_input("PLEASE ENTER THE PASSWORD FILE NAME: ")

#this part of the code checks for correct input

try:
         pwfile = open(pwfile, "r")
except:
         print "\nFile not Found!"
         quit()
         
#THis part of the code is where the passwords are Hashed and tested in a loop intil the list  is done  or a match is found 
for  password in pwfile:
          filemd5 = md5.new(password.strip()).hexdigest()
          print "Trying password number %d %s " % (counter, password.strip())
          
          counter += 1
          
          if pass_in == filemd5:
                  print "\nMatch Found. \nPassword is: %s" % password
                  break
                  
#this part of the code is what displayed if there is no match on the password list used 
else:print "\nPassword NOT FOUND "