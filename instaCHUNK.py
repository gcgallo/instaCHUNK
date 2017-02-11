from PIL import ImageColor
from PIL import Image

import errno    
import os


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

new_new = Image.open(raw_input("Enter the image file to clean up: "))
new_new2 = new_new.copy()
x, y = new_new.size         

print(x)
print(y)

row = y/(x/3)

print(row)

image_name = raw_input("Enter the file name of the image: ")

mkdir_p(./image_name)

for i in range(0, row+1):
	for j in range(0, 3):
		lft = j*(x/3) + 1
		rgt = (j+1)*(x/3) - 1
		top = i*(x/3) + 1
		bot = (i+1)*(x/3) - 1

		print(lft)
		print(rgt)
		print(top)
		print(bot)

		new_new3 = new_new2.crop((lft,top, rgt, bot))

		
		new_new3.save(image_name + str(i) + str(j) + ".JPG")

