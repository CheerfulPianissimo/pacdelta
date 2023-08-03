import sys
import subprocess
import os
if len(sys.argv)<=1:
    print("No arguments passed")
    exit(1)

with open("patches.txt", "r") as file:
        for delta in file:
                  pkg,old_ver,_,new_ver=delta.split()
                  #print(pkg,old_ver,new_ver)
                  old_zst="/var/cache/pacman/pkg/%s-%s-x86_64.pkg.tar.zst"%(pkg,old_ver)
                  if sys.argv[1]=="--generate":
                    if os.path.exists(old_zst):
                        print(delta.strip())
                  elif sys.argv[1]=="--apply":
                    new_zst="newdb/%s-%s-x86_64.pkg.tar.zst"%(pkg,new_ver)
                    patch_file="patches/%s.patch"%delta.strip()
                    print(subprocess.run(["zstd","-d","--patch-from", old_zst,patch_file,"-o",new_zst], capture_output=True, text=True).stdout)
                    print(patch_file)
                  else:
                       print("Unknown argument %s"%sys.argv[0])
                       exit(1)
