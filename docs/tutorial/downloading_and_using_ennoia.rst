Downloading and using Ennoia for the first time
===============================================
This is a step-by-step tutorial that will guide you through:

- Downloading Ennoia from GitHub

- Running Ennoia on your computer

- Creating your profile

- Adding your first book

Ennoia is a local web app. This means that you access it through a broswer, but it runs on your own computer.

There are various ways you can download Ennoia and use it, but this tutorial will cover the simplest way to get started.

To complete this tutorial, you need:

- An internet connection

- A web browser

- Access to a terminal

Downloading Ennoia from GitHub
------------------------------
The only way to access Ennoia (for now) is through GitHub. If you do not have a Git or a GitHub profile, that is okay. You do not need one to download and use Ennoia.

1. In a web browser, go to https://github.com/jaketanis/ennoia.

2. To download the code, select **Code**, and then select **Download ZIP**. You should see a folder downloading in your browser.

3. Open your downloads folder, copy the ZIP file, and then paste it into a folder you want the app in.

4. Extract the pasted ZIP file. You should see a folder named **ennoia-main**.

Running Ennoia on your computer
-------------------------------
Since Ennoia is a local web app, you need to run it on your own computer. This is done in the terminal.

1. Open your terminal. This is where we will run Ennoia.

2. We need to now go to the folder where Ennoia is. In the terminal, change folders to where Ennoia is by using the ``cd`` command, and then press **Enter**.

3. After navigating to Ennoia, we now need to create a virtual environment. Virtual environments allows us to install the necessary components to run the app. Type ``python3 -m venv .venv``, and then press **Enter**. This creates a folder named **.venv**.

4. After creating the virtual environment folder, we now need to activate it. Type ``. ./.venv/bin/activate``, and then press **Enter**. If **(.venv)** appears in the command line, this means you have activated the virtual environment.

5. We can now install the components needed for the app. These are listed in **requirements.txt**. To install these components, type ``pip install -r requirments.txt``, and then press **Enter**. You should see downloads occurring in the terminal.

6. We can now run the app. Type ``waitress-serve --host 127.0.0.1 --call ennoia:create_app``. The command line should show **Serving on http:127.0.0.1:8080**, which means the app is running.

7. In the command line, hover over the URL with your mouse, and then type ``Ctrl + C``. Ennoia opens in your browser.

.. container:: image-2

    .. image:: ../images/login_window.png

Creating your profile
---------------------
Before we create a profile, we need to setup the database. After we do that, we can then create a profile, login, and then add some books.

1. In the command line, type ``flask --app ennoia init-db``. The command line should display **Initialized the database**.

2. In Ennoia, click **Create**. The Create profile window opens.

.. container:: image-2

    .. image:: ../images/create_profile_window.png

3. Type a **Username** and a **Password**.

4. Click **Create**. The Login window opens.

5. Enter your credentials, and then click **Login**. Ennoia opens.

.. container:: image-2

    .. image:: ../images/ennoia_window.png

Adding your first book
----------------------
Setup is complete. We can now use Ennoia and add books to our new profile.

1. Click **Add**. Ennoia opens a window for you to add a book.

2. Type the **Title** of a book you are reading.

3. Type the **Author** of the same book.

4. In **Notes**, type your current thoughts on the book so far. What is most compelling? What has surprised you? What are you having a hard time with?

5. After writing out your thoughts, click **Add**. Ennoia displays the book and your thoughts along with it.

.. container:: image-2

    .. image:: ../images/added_book.png
