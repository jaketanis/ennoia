Starting Ennoia
===============

After installing Ennoia, run the app in the command line.

1. Open your terminal.

2. Open the ``ennoia-main`` folder.

3. Activate the virtual environment.

.. code-block:: python

   . ./.venv/bin/activate

5. In the command line, start the app through waitress:

.. code-block::

    waitress-serve --host 127.0.0.1 --call ennoia:create_app

7. In the command line, hover over the URL with your mouse, and then type ``Ctrl + C``. Ennoia opens in your browser.