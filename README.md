Git.py
======
#### Python bindings for Git

Table of Content
----------------
- [Introduction](#intro)
- [Installation](#install)
- [Usage](#usage)
- [License](#license)
- [Support](#support)

Introduction<a name='intro'></a>
------------
Git in Python yo! There is an emphasized focus on simplicity for this project.

Installation<a name='install'></a>
------------
For now, it's not on PYPI yet. You can just download the zip file.

Usage<a name='usage'></a>
-----
Here is how you would use it in a script:
```python
from git import Repo
repo  = Repo('~/Desktop/awesome-repo')
repo.add()
repo.commit(['README.md', 'LICENSE', '.gitignore'])
repo.remote_add(origin = 'master')
repo.push('origin', 'master')
```
Simple isn't it?!

License<a name='license'></a>
-------
The following code is released under the MIT License.

Support<a name='support'></a>
-----------------------------
If you have any questions/concerns, please feel free to contact me.
You can mail me at guanhao3797@gmail.com or tweet to [@guanhao97](https://twitter.com/guanhao97)!
