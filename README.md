# Search memory leak points on Python code
`memory_leak.py` provides useful class methods for finding memory leaks in your Python code.

# Example
## Usage
```python
from face01lib.memory_leak import Memory_leak
m = Memory_leak(limit=2, key_type='lineno')
m.memory_leak_analyze_start()

# ...Your application code

m.memory_leak_analyze_stop()
```
## Output
```bash
------------------------------
Called 'memory_leak.py' with 'lineno' mode...
------------------------------

# ...

Top 2 lines
#1: File:~/bin/FACE01/face01lib/Core.py
    Line: 1253
    Size: 3.5 MiB
    frame = np.array(self.pil_img_obj)
-----
#2: File:/usr/lib/python3.8/linecache.py
    Line: 137
    Size: 3.5 MiB
    lines = fp.readlines()
-----
20483, Other: 29.4 MiB
Total allocated size: 36.4 MiB
------------------------------
Used Memory: 1.5 GiB
------------------------------

Pympler report
                       types |   # objects |   total size
============================ | =========== | ============
                       tuple |      384549 |     23.37 MB
               numpy.ndarray |         922 |     14.04 MB
                         str |       67733 |     10.87 MB
                        dict |       21341 |      8.73 MB
                        code |       22285 |      3.79 MB
                        list |        7797 |      3.66 MB
                        type |        3793 |      3.52 MB
                         set |        1645 |    896.99 KB
                       bytes |         190 |    717.59 KB
  builtin_function_or_method |        7838 |    551.11 KB
                     weakref |        7686 |    540.42 KB
     collections.OrderedDict |         224 |    401.42 KB
                 abc.ABCMeta |         263 |    307.12 KB
           inspect.Parameter |        4336 |    271.00 KB
           method_descriptor |        3785 |    266.13 KB
```

# Augments
Memory_leak class takes 3 augments.
- limit:(int)
  - Limit output lines.
- key_type:(str)
  - Select 'lineno' or 'traceback' output. Defaults to 'lineno'.
- nframe:(int, optional)
  - This can be specified only when key_type is 'traceback'. Defaults to 5.

# License
MIT license

# Reference
- tracemalloc
    - [En]
        - https://docs.python.org/3/library/tracemalloc.html#
    - [ja]
        - https://docs.python.org/ja/3/library/tracemalloc.html#
- Pympler
    - https://pympler.readthedocs.io/en/latest/