============
Installation
============

Install galmorph from source
----------------------------

:code:`galmorph` is developed and tested with Python 3.10-3.12. In the
following, we assume you have a working python installation, `python pip
<https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing>`_,
and `git <https://git-scm.com/>`_. 

Clone the repository, install the requirements, and then install the software:

.. code-block:: console

    $ git clone git@github.com:ImPriyatam/galmorph.git
    $ cd galmorph/
    $ pip install .

Once you have run these steps, you have :code:`galmorph` installed.

Installing dependencies
================================

.. _installing-python:

Installing python
-----------------

Most computers/clusters have a system installed python version. You may choose
to use this, but here we describe an alternative. In particular, how to install
the `anaconda distribution python package
<https://www.anaconda.com/download/#linux>`_. Firstly, download the install
file, you can do this from the link above, or run the command

.. code-block:: console

   $ wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh

this will download a linux installer for python, for other versions check
the `anaconda page <https://www.anaconda.com/download/#linux>`_.
Then, `run the command
<https://conda.io/docs/user-guide/install/linux.html>`_

.. code-block:: console

   $ bash Anaconda3-5.2.0-Linux-x86_64.sh

and follow the prompts on the install screen.  After this process, you should
have a directory :code:`~/anaconda3` in your home directory. This contains your
python installation. In particular, if you run the command

.. code-block:: console

   $ which python
   $ /home/users/USER/anaconda3/bin/python

The output here (with a suitable replacement of the path) indicates that you
are using the anaconda install of python. If instead, the output says something
like :code;`/usr/bin/python`, then this is not the anaconda installation, but
instead the system python.

If you are finding that you have run the above steps, but :code:`python` is
not pointing to your anaconda install, make sure that (a) you have appended a
line like this to your :code:`.bashrc` file

.. code-block:: console

   $ export PATH="${HOME}/anaconda3/bin:$PATH"

and (b) that you have restarted bash for this line to take effect (i.e., run
:code:`$ bash`).

.. note::

    Using your own installation of python has several advantages: its generally
    easier to debug, avoids conflicts with other packages, and if you end up
    with a broken installation you can just delete the directory and start
    again.

You may need to separately install :code:`numpy` and :code:`pandas`. Installation
instructions are provided below.

.. _installing-numpy:

Installing numpy
----------------

.. code-block:: console

    $ pip install numpy

To verify that :code:`numpy` has been correctly installed on your system:

.. code-block:: console

    $ import numpy as np
    $ print(np.__version__)

.. _installing-pandas:

Installing pandas
-----------------

.. code-block:: console

    $ pip install pandas

.. note::
    If your Python environment does not have pip installed, you can install it separately:
    
    .. code-block:: console

        $ python -m ensurepip --upgrade