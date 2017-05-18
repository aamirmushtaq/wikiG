import os
import shutil

dest = '/home/aamir/Wikipedia2Text/wiki2text/onedump/'

for root, dirs, files in os.walk('./'):
   for file in files:
       if file[-4:].lower() == '.txt':
               shutil.copy(os.path.join(root, file), os.path.join(dest, file))
