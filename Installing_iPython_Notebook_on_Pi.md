How to Install iPython Notebook on the Raspberry Pi
=======================================================
Before installing and using iPython Notebook, make sure you are:
- [x] Connected to the internet.

**To install iPython notebook, enter the following command in the LXTerminal on your Pi:**
```linux
sudo apt-get -y install ipython-notebook
sudo apt-get -y install python-matplotlib python-scipy \
                 python-pandas python-sympy python-nose
```
**Once the installation is complete, run the following command in your LXTerminal to open the iPython notebook:**
```linux
ipython notebook
```
