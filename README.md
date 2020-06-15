# rofi-i3-bindsym

Displays the bindsyms (with the description, keys and command) in your i3 config and executes on selection.

![](https://i.imgur.com/xKIPLeV.gif)

## Config

Put this in your i3 config and adjust the location of the script.
```
# i3wm bindsyms
bindsym $mod+Shift+space exec --no-startup-id rofi -modi rofi-i3-bindsym:~/git/rofi-i3-bindsym/rofi-i3-bindsym.py -show rofi-i3-bindsym
```
if your i3 config is not in `~/.i3/config` you'll need to change this line:
```python
filename =  os.path.expanduser('~') + '/.i3/config' #? Change this if you have your config file located somewhere else.

If you like to see bindsyms without a decription remove line 29.
```
