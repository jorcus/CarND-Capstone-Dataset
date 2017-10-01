import os
j=0
for i in os.listdir('.'):
        os.rename(i, "{}.jpg".format(j))
        j += 1
