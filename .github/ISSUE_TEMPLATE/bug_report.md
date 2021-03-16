---
name: Bug report about: Create a report to help us improve title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Code to reproduce the behavior and error message:

```python
from devhelpers import timeit

@timeit(100)
def foo(a):
    return a * a

a()
```

```console
The complete traceback here.
```

**Expected behavior**
A clear and concise description of what you expected to happen.

**Desktop (please complete the following information):**

- OS: [e.g. Windows 10 x64 Workstation Build: 19042.746 (20H2)]
- Version of devhelpers [e.g. 0.1.0]

**Additional context**
Add any other context about the problem here.
