![GitHub](https://img.shields.io/github/license/MichaelSasser/devhelpers?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/MichaelSasser/devhelpers/Build%20and%20Tests?style=flat-square)

# DevHelpers

DevHelpers is a loose collection of python development helpers.
It is not made to be included or used in a finished product.

# Toolbox

- The `@timeit` decorator to time the runtime of a function or method.
  With `@timit(1000)` the function or method will be timed 1000 times
  and prints afterword a small statistic.

## Semantic Versioning

This repository uses [SemVer](https://semver.org/) for its release cycle.

## Branching Model

This repository uses the
[git-flow](https://danielkummer.github.io/git-flow-cheatsheet/index.html)
branching model by [Vincent Driessen](https://nvie.com/about/). It has two branches with infinite lifetime:

* [master](https://github.com/MichaelSasser/devhelpers/tree/master)
* [develop](https://github.com/MichaelSasser/devhelpers/tree/develop)

The master branch gets updated on every release. The develop branch is the merging branch.

## License

Copyright &copy; 2021 Michael Sasser <Info@MichaelSasser.org>. Released under the GPLv3 license.
