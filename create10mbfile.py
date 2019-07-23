f = open('ten.png',"wb")
boyut = 1024*1024*10
f.seek(boyut-1)
f.write(b"\0")
f.close()

import os
print(os.stat("ten.png").st_size)
