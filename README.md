Cellar
======

Cellar is an experiment to see if I can make the 'pip of
[salt](http://docs.saltstack.com/index.html) formulas' which absence if for me
the biggest weakness of salt.

Cellar is at its **very early stage of development**.

You need git to be installed for this to run.

Installation
============

Not on pypi yet, so do:

    pip install "git+https://github.com/Psycojoker/cellar.git"

Usage
=====

Quite simple:

    cellar list  # list all available formulas (from https://github.com/saltstack-formulas)
    cellar install <list of formulas>
    cellar uninstall <list of formulas>

You can also install a formula of a custom github repository using the pattern <username>/<repository>:

    cellar install <username>/<repository>

    # stupid example
    cellar install saltstack-formulas/openssh-formula

You can also use a git url this way:

    cellar install <git url>

    # stupid example
    cellar install git@github.com:saltstack-formulas/openssh-formula.git

**Cellar is expecting the repository to have, either, a directory or a .sls file with the same name than the repository.**

If the repository name contains "-formula", it will be removed from the expected name. Meaning that you can name your repository *stuff-formula* and put inside either a *stuff* directory or a *stuff.sls*.
