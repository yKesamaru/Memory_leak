# Example

Here I use google mediapipe as an example where memory leak occurs.  
An official mediapipe python example is [here](https://google.github.io/mediapipe/solutions/face_detection.html).

# `examples/ex_memory_leak.py`
[Google's example](https://google.github.io/mediapipe/solutions/face_detection.html).

```python
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
```
Google's example uses the `with` syntax so that you don't forget to close it.  

![](assets/not_memory_leak.png)

In contrast, the example below which I wrote will prone to memory leaks.
```python
f = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

# some process...

f.close()
```

If forget to insert `f.close()`, it might occur memory leak.  
In the example, I compared the case where the handle `f` used for mediapipe is closed and not closed.

![](assets/memory_leak.png)

Based on the above, I prepared `ex_memory_leak.py`.
The code in this script is intentionally written to cause a memory leak.  
Whole code is [here](ex_memory_leak.py).

`ex_memory_leak.py` has the following code embedded at the top of the script.  

```python
# Import Memory_leak class
from memory_leak import Memory_leak

# Make instance
m = Memory_leak(limit = 5, key_type = 'lineno')
# m = Memory_leak(limit = 5, key_type = 'traceback', nframe = 3)

# Specify start point
m.memory_leak_analyze_start()
```

It can be traced faster by placing it at the beginning of the script.
