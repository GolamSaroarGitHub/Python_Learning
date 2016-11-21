from PIL import Image
import time

for i in range(1,6):


        img=Image.open(str(i)+'.jpg')

        print(str(i))
        img.show()

        time.sleep(5)