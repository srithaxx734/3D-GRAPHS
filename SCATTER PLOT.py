import matplotlib.pyplot as plt
import numpy as np
a=plt.figure(figsize=(6,7))
b=plt.axes(projection="3d")
print(b)
x=[1,2,3,4,5,6,7,8,9,10]
y=[-50,-24,-64,-76,-98,-45,-46,-45,-67,-49]
v=[24,68,74,78,89,23,53,75,35,45]

f=np.random.randint(0,30,100)
g=np.random.randint(50,300,100)
h=np.random.randint(7,78,100)
#print(f)
b.set_xlabel("X AXIS")
b.set_ylabel("Y AXIS")
b.set_zlabel("Z AXIS")
b.set_title("3D SCATTER PLOT")
b.set_facecolor("black")
b.scatter(f,g,h,color="#bb8fce",marker=",")
plt.show()
