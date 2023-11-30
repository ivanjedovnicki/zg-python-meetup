# zg-python-meetup

This is the repo with the source code for my talk about the limitations of the
GIL held at Zagreb. Each module illustrates one aspect of threading in
Python. The [CPU bound](cpubound.py) and [I/O bound](iobound.py) modules 
show two different kinds of problems regarding CPU load. Examples 
[7](example07.py) and [8](example08.py) test those two different kinds of 
problems, and show the impact of the GIL on both. Tweaking the GIL switch 
interval shows the effect context switches have on performance.

I hope these examples help you in understanding the GIL and its limitations 
so that you may write multithreaded code with confidence. For a light 
theoretical background on threading in Python, check out my blog post 
https://ivanjedovnicki.github.io/blog/python/multithreading/.
