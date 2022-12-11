# bluefruit

### Chromebook

Enable Linux

- https://support.google.com/chromebook/answer/9145439?b=atlas-signed-mpkeys&visit_id=638063737208395810-3020709761&p=chromebook_linuxapps&rd=1

Install Mu

https://codewith.mu/en/howto/1.2/install_linux

```
curl -L -O https://github.com/mu-editor/mu/releases/download/v1.2.0/MuEditor-Linux-1.2.0-x86_64.tar
tar xf MuEditor-Linux-1.2.0-x86_64.tar
```

```
sudo adduser $USER dialout
# The user `simonachiang' is already a member of `dialout'.

uname -a
# Linux penguin 5.10.142-19743-gd301e86c39f7 #1 SMP PREEMPT Sun Nov 6 17:31:44 PST 2022 x86_64 GNU/Linux
```



QT_QPA_PLATFORM=wayland ./Mu_Editor-1.2.0-x86_64.AppImage
No settings file found at /home/simonachiang/.local/share/mu/venv.json; skipping
qt.qpa.wayland: Ignoring unexpected wl_surface.enter received for output with id: 7 screen name: "Screen5" screen model: "302D" This is most likely a bug in the compositor.

Shortcuts

- Ctl-shift-v paste
- ctl-shift-z redo

Connected and there was a  popup that s
## Install libraries

https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython

https://downloads.circuitpython.org/bin/circuitplayground_bluefruit/en_US/adafruit-circuitpython-circuitplayground_bluefruit-en_US-7.3.3.uf2

https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20221211/adafruit-circuitpython-bundle-7.x-mpy-20221211.zip
unzip adafruit-circuitpython-bundle-7.x-mpy-20221211.zip

https://github.com/adafruit/CircuitPython_Community_Bundle/releases/download/20221208/circuitpython-community-bundle-7.x-mpy-20221208.zip
unzip cuitpython-community-bundle-7.x-mpy-20221208.zip
