Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import maplotlib.pyplot as plpt
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import maplotlib.pyplot as plpt
ModuleNotFoundError: No module named 'maplotlib'
>>> import maptlotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import maptlotlib.pyplot as plt
ModuleNotFoundError: No module named 'maptlotlib'
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> from sklearn.cluster import KMeans
>>> f="C:\\Users\\user\\Desktop\\parrot.jpg"
>>> a=cv2.imread(f)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a=cv2.imread(f)
NameError: name 'cv2' is not defined
>>> import cv2
>>> a=cv2.imread(f)
>>> 
>>> a
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
>>> a.shape
(650, 850, 3)
>>> x=a.reshape((650*850),3)
>>> x.shape
(552500, 3)
>>> k=kmeans()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    k=kmeans()
NameError: name 'kmeans' is not defined
>>> k=KMeans()
>>> d=k.fit(x)
>>> d
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=8, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)
>>> out=d.predict(x)
>>> out
array([1, 1, 1, ..., 1, 1, 1])
>>> plt.scatter(x[:,0],x[:,1],x[:,2],c=out)
<matplotlib.collections.PathCollection object at 0x080D8750>
>>> plt.show()
