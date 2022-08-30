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
20865, Other: 30.6 MiB
Total allocated size: 37.6 MiB
------------------------------
Used Memory: 1.3 GiB
------------------------------

Pympler report
<Summary>
                       types |   # objects |   total size
============================ | =========== | ============
                       tuple |      422214 |     25.70 MB
               numpy.ndarray |         922 |     14.02 MB
                         str |       74797 |     11.38 MB
                        dict |       21407 |      9.17 MB
                        list |       14535 |      4.58 MB
                        code |       22431 |      3.82 MB
                        type |        3820 |      3.54 MB
                         set |        1649 |    899.34 KB
                       bytes |         190 |    705.78 KB
  builtin_function_or_method |        7831 |    550.62 KB
                     weakref |        7700 |    541.41 KB
     collections.OrderedDict |         235 |    406.22 KB
                 abc.ABCMeta |         263 |    307.12 KB
           inspect.Parameter |        4373 |    273.31 KB
           method_descriptor |        3801 |    267.26 KB
------------------------------
<Summary_diff>
                       types |   # objects |   total size
============================ | =========== | ============
                       tuple |      410069 |     25.02 MB
               numpy.ndarray |         847 |     14.01 MB
                        list |       24733 |     10.53 MB
                         str |       52483 |      6.66 MB
                        dict |       11524 |      4.97 MB
                        type |        2073 |      2.01 MB
                        code |       11649 |      2.00 MB
                       bytes |          78 |    700.15 KB
     collections.OrderedDict |         235 |    406.22 KB
                         set |         659 |    403.51 KB
  builtin_function_or_method |        4798 |    337.36 KB
                     weakref |        4004 |    281.53 KB
           inspect.Parameter |        4373 |    273.31 KB
                         int |        8384 |    230.48 KB
                   frozenset |         140 |    181.53 KB
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