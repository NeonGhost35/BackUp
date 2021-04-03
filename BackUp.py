import os
import zipfile 

userdir = input ("Enter Dir to Save BackUp: ")
dirtobackup = input ("Enter Dir to BackUp: ")

backup = zipfile.ZipFile(userdir, "w")

for floder, subfloders, files in os.walk(dirtobackup):
    for file in files:
        backup.write(os.path.join(floder, file), os.path.relpath(os.path.join(floder, file), dirtobackup), compress_type = zipfile.ZIP_DEFLATED)

print ("BackUp saved to ", userdir)
