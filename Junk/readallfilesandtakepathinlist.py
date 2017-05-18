import os
basePath = './'
allfiles = []
subfiles = []
for root, dirs, files in os.walk(basePath):
    for f in files:
        if f.endswith('.txt'):
            allfiles.append(os.path.join(root,f))
            if root!=basePath:
                subfiles.append(os.path.join(root, f))
  

              
            
print allfiles
