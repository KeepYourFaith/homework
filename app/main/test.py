import os
val = os.popen("ls -al")
for tmp in val.readlines():
    print(tmp)