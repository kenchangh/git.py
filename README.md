Git.py
======
### Python bindings for Git

Introduction
------------
Git in Python yo! There is an emphasized focus on simplicity for this project.

Usage
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
