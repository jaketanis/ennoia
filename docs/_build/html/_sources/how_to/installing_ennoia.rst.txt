Installing Ennoia through HTTPS
===============================

1. In a web browser, go to https://github.com/jaketanis/ennoia.

2. Click **Code**, and then copy ``https://github.com/jaketanis/ennoia.git``.

3. Open your terminal and clone the repository through git:

.. code-block:: python
   
   git clone https://github.com/jaketanis/ennoia.git

4. Open **ennoia-main**.

5. Create a virtual environment.

.. code-block:: python

   python3 -m venv .venv

6. Activate the virtual environment.

.. code-block:: python

   . ./.venv/bin/activate

7. Install the dependencies.

.. code-block:: python

   pip install -r requirments.txt