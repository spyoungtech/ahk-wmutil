# ahk-wmutil

This is an extension package intended to be used with the Python [ahk](https://github.com/spyoungtech/ahk) package. 
It adds functionality provided by the [`wmutil`](https://github.com/spyoungtech/wmutil) package into a convenient 
ahk extension.

## Installation

```
pip install ahk-wmutil
```

## Usage


```python
from ahk import AHK
import wmutil
from ahk_wmutil import wmutil_extension

ahk = AHK(extensions=[wmutil_extension])

win = ahk.active_window

primary_monitor = wmutil.get_primary_monitor()

# move a window to a given monitor
win.move_to_monitor(primary_monitor)

# Get the monitor the window is using
mon = win.get_monitor() 
assert mon == primary_monitor # True

# Get the monitor that the mouse cursor is on
mon = ahk.monitor_from_mouse_position()
```


Possible future work:

- [ ] A customized `Monitor` class that provides additional functionality, like listing all windows on a monitor
- [ ] Easy positioning of windows within a monitor (e.g., split left/right, quadrants, etc.)
