import os, sys, re
list = []
for root, dirs, files in os.walk("/home/aamir/code/onedump/"):
     for f in files:
         name = os.path.splitext(f)[0]
         if name.endswith('.'):
            print 'a'
            
         else:
             namenew = name.replace('.','_')
             
             namenew = name.replace('.','')
             
         extension = os.path.splitext(f)[1]
         old = root + name + extension
         new = root + namenew + extension
         os.rename(old,new)
