# pyHook wheels

The pyHook project was published on [sourceforge](https://sourceforge.net/projects/pyhook/), which only has releases built for python2.

The release version of pyHook that has python3 support was built by [Christoph Gohlke](https://www.lfd.uci.edu/~gohlke/). Thanks to he and his [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/) project, we can download the [pyHook wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook) from his site.

However, his site doesn't provide direct links for downloading, instead, it requires javascript enabled to download, which is not suitable for declaring them as dependencies. So I upload them to [github repository](https://github.com/WqyJh/python-wheels), which provides direct links for downloading and therefore, we can declare dependencies in our `requirements.txt` or `setup.py`.

## Usage

**pip:**
```bash
pip install https://github.com/WqyJh/python-wheels/pyHook
```

**requirements.txt**
```
--extra-index-url http://127.0.0.1:8000/
pyHook
```


