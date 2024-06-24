# Binary Ninja - Header Font Scale Fix

This tiny plugin will normalize the 20% bigger header font size in Binary Ninja. Sadly the non constistent size in the GUI is driving me nuts during work and killed the all over experience with the tool. This plugion will fix all headers by resetting their fonstsize back to the regular UI font size. My request to add a config parameter for it was rejected. I am still confused there are settings for everything in binja, but this was left out. 

To install copy the file into your Binary Ninja plugins folder:

```
cp set_font_notify.py ~/.binaryninja/plugins/set_font_notify.py
```