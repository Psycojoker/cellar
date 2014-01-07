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
