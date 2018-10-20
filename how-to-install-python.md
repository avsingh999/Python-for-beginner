This guide will teach you how to install and setup Python 3 for Linux, Windows, and Mac.

# Windows :

### Step 1: Download the Python 3 Installer

- Open a browser window and navigate to the [Download page](https://www.python.org/downloads/windows/) for Windows at [python.org](python.org).
- Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x.
- Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit.

### Step 2: Run the Installer

Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file. 

A dialog should appear.

Then just click Install Now. That should be all there is to it. A few minutes later you should have a working Python 3 installation on your system.

# Linux :

There is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3.

To find out what version(s) you have, open a terminal window and try the following commands:

``python --version``

``python2 --version``

``python3 --version``

One or more of these commands should respond with a version, as below:

``$ python3 --version``
If the version shown is Python 2.x.x or a version of Python 3 that is not the latest (3.6.5 as of this writing), then you will want to install the latest version. The procedure for doing this will depend on the Linux distribution you are running.

Note that it is frequently easier to use a tool called pyenv to manage multiple Python versions on Linux. To learn more about it, see our article here.

# macOS / Mac OS X :

The best way we found to install Python 3 on macOS is through the [Homebrew package manager](https://brew.sh/). This approach is also recommended by community guides like The [Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/starting/install3/osx/).

### Step 1: Install Homebrew (Part 1)

To get started, you first want to install Homebrew:

Open a browser and navigate to [http://brew.sh/](http://brew.sh/).

After the page has finished loading, select the Homebrew bootstrap code under “Install Homebrew”. 

Then hit Cmd+C to copy it to the clipboard.

Make sure you’ve captured the text of the complete command because otherwise the installation will fail.

Now you need to open a Terminal.app window, paste the Homebrew bootstrap code, and then hit Enter. 

This will begin the Homebrew installation.

If you’re doing this on a fresh install of macOS, you may get a pop up alert asking you to install Apple’s “command line developer tools”. You’ll need those to continue with the installation, so please confirm the dialog box by clicking on “Install”.

At this point, you’re likely waiting for the command line developer tools to finish installing, and that’s going to take a few minutes. Time to grab a coffee or tea!

### Step 2: Install Homebrew (Part 2)

You can continue installing Homebrew and then Python after the command line developer tools installation is complete:

Confirm the “The software was installed” dialog from the developer tools installer.

Back in the terminal, hit Enter to continue with the Homebrew installation.

Homebrew asks you to enter your password so it can finalize the installation. Enter your user account password and hit Enter to continue.

Depending on your internet connection, Homebrew will take a few minutes to download its required files. Once the installation is complete, you’ll end up back at the command prompt in your terminal window.

Whew! Now that the Homebrew package manager is set up, let’s continue on with installing Python 3 on your system.

### Step 3: Install Python

Once Homebrew has finished installing, return to your terminal and run the following command:

``brew install python3``

This will download and install the latest version of Python. After the Homebrew brew install command finishes, Python 3 should be installed on your system.

You can make sure everything went correctly by testing if Python can be accessed from the terminal:

Open the terminal by launching Terminal.app.

Type ``pip3`` and hit ``Enter``.

You should see the help text from Python’s “Pip” package manager. 

If you get an error message running pip3, go through the Python install steps again to make sure you have a working Python installation.

Assuming everything went well and you saw the output from Pip in your command prompt window…congratulations! 

You just installed Python on your system, and you’re all set to continue with the next section in this tutorial.

Cheers :100:
