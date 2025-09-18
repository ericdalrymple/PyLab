<img align="left" width="70" height="70" src="https://raw.githubusercontent.com/ericdalrymple/PyLab/refs/heads/main/res/icons/pylab.png" style="float:left;">

# PyLab
## Acknowledgements
* PyLab icon: [Beaker icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/beaker)
* PyLab core functionality: [Pygame](https://www.pygame.org)

## Overview
PyLab is an attempt at providing an evironment conducive to introducing Python to a younger audience via a very basic game engine with several streamlined interfaces. Learners can use more advnaced interfaces to do the same things as they learn more and more of the basics of Python.

The project contains the following:
* <ins>__PyLab Hub:__</ins> A batch file that provides basic options for browsing lessons, creating small games from a template, sharing games created with PyLab with friends with zero setup.

* <ins>__Lessons:__</ins> A series of lessons and exercises That gradually covers the basics of Python and game making.

* <ins>__PyLab Engine:__</ins> A rudimentary 2D game engine built on top the [Pygame](https://www.pygame.org). It provides multiple ways of achieving the same outcomes. Beginners are expected to do things the more basic yet less scalable way and can gradually use the more advanced more powerful interfaces as they learn.
    * __Beginners:__ Draw game contents directly and manipulate them using variables. All callbacks (draw, update, input handlers, etc.) and variables would typically be in the main module.

    * __Intermediate:__ Use objects to encapsulate behaviour and drawing of game elements.

    * __Advanced:__ Add components to encapsulate behaviours and drawing and combine them into entities to define game elements. 

## Requirements
- __Windows 10/11:__ - This project could support other operating systems fairly easily, but is limited to Windows for simplicity.

## Setup
### 1 - Setup the PyLab package
In this step, we’ll download “PyLab”, which is a collection of scripts that we’ll use to learn and practice programming in Python. It also includes the installers for Python and VS Code and a setup script to configure your environment for development.
1. Download the latest [PyLab deployment](.packaged/PyLab.zip) from the repository.

2. Place the PyLab zip file in a folder of your choice (preferably under your user folder) and extract the files.

3. (Optional) Delete the zip file once you’ve extracted the files from it.

4. Double-click on the `setup.bat` file inside the PyLab folder.
    * This will download and run the installers for __Python 3.13__ and __Visual Studio Code__. Follow the default setup instructions.

    * After the installers, the script will do more Python-related setup. Once the setup is completed, press any key to close the terminal.

    * Setup is now complete, we’re almost ready to run some code.
  
---

### 2 - Configure Visual Studio Code
#### 2.1 - Open Visual Studio Code
You should now be able to search for and open Visual Studio Code from your Start Menu.

#### 2.2 - Install the Python extension
Installing the Python extension for Visual Studio Code will let Visual Studio Code run and debug your Python scripts and will provide handy features like auto-complete, syntax colouring, and highlighting errors and warnings as you type code
* Go to the extensions tab in the left-hand bar and search for “Python”.
* Click the “Install” button on the extension simply titled ”Python”.
* Once the extension installation is complete, close Visual Studio Code.</br></br><img width="660" height="600" alt="VSCode Python extension screenshot" src="https://github.com/user-attachments/assets/c4998adf-076b-408b-8524-aab763914c1a" />

#### 2.3 - Test your dev environment
Let’s open PyLab in Visual Studio Code and make sure we can run our scripts properly.
* Launch PyLab from your Start Menu **OR** double-click the PyLab shortcut in your PyLab folder.

* You will be presented with a list of options. Choose `1. Open lessons` options by typing __1__ and pressing __Enter__.</br></br><img width="1115" height="322" alt="image" src="https://github.com/user-attachments/assets/be9d84a9-f583-486e-a437-9cddfdc3e0b1" />

* This will open basic Python lessons in Visual Studio Code. From the explorer tab in the left-hand bar, select the file __lessons > Stage 1 - The Basics of Python > Level 01 - Printing > example.py__</br></br><img width="1207" height="800" alt="Untitled" src="https://github.com/user-attachments/assets/3c1fe9b1-c228-4e1f-b577-fa71f37a05bb" />

* Open the dropdown next to the “Play” button in the top-right and select the “__Python Debugger: Debug Python File__” option</br></br><img width="1200" height="800" alt="Untitled" src="https://github.com/user-attachments/assets/5b569021-d631-47ac-9469-4df95cf942e1" />

* Visual Studio Code should switch to the Terminal view in the bottom pane and should print the message “Hello World!”.</br></br><img width="1200" height="800" alt="Untitled" src="https://github.com/user-attachments/assets/db8f521f-95d7-43a0-93ff-98a3652f1a92" />

---

### 3 - Have Fun!
You’re now ready to start programming in Python! Happy learning!

## Using PyLab
### Launching PyLab Hub
To use the various features of PyLab, launch PyLab from your Start Menu **OR** double-click PyLab shortcut in the directory where PyLab is installed.

After doing this, you will see a menu of options.

<img width="808" height="362" alt="image" src="https://github.com/user-attachments/assets/45963522-ecad-4603-b4d6-bacf7f93925f" />

To choose an option, type the number assigned to it and hit `Enter`. To exit the PyLab Hub, select the "Nothing" option.

In the rest of this section, we will go over the options and what they do in a bit more detail.

### 1. Open Lessons
Choosing this option will open the "lessons" directory in Visual Studio Code, letting you browse the various coding lessons. These lessons can be run individually without other distractions.

### 2. Create a new game
Choosing this option will create the files and directories needed for a basic new 2D game using the PyLab engine and opens the game project in Visual Studio Code once created.

After this option is chosen, you will be prompted to enter a name for the game they want to create. If the name matches a previously created game, you will be asked to choose a different one.

### 3. Open an existing game
Choosing this option will open the project for a previously created game in Visual Studio Code.

When this option is selected, PyLab Hub will show a list of available games that were previously created using the option above. To select the desired game, type any part of its name an hit `Enter`. PyLab will choose the first game down the list starting with what was typed. Let's look at an example:

<img width="808" height="419" alt="image" src="https://github.com/user-attachments/assets/d69dfc7c-c959-491d-b367-fd62cf503faa" />

Here we have 4 available games: Avalanche, DemoGame, Froyo and Melting Point. And the user has typed `d`. Because "DemoGame" is the first game in the list that starts with 'd', "DemoGame" will be selected when the user hits `Enter`.

### 4. Share a game
Choosing this option will create a .zip file that contains a game chosen by the user. This zip file can then be sent to someone else, who can unzip the file and run the game in Windows with no other setup. This option exists so that students can share the things they make with other people, which can hopefully provide motivation to make cool things and get ideas from their friends.

When selecting this option, the user will be asked to select a game among those already created the same way they would for opening a game project (see previous sub-section).

Let's look at an example and decide to share the game "Froyo":

<img width="808" height="419" alt="image" src="https://github.com/user-attachments/assets/b19d2240-2c48-4cde-8a03-8cc92b23c0ec" />


Hitting `Enter` on the screen above will start the "sharing" process for the game "Froyo" because it is the first game in the list starting with `f`. This will take some time depending on the size of the game. Please be patient; the screen will tell you when the job is done.

<img width="808" height="476" alt="image" src="https://github.com/user-attachments/assets/45e5ca7b-069b-4ac1-96c8-863bcfe1e0a1" />


When complete, PyLab will open a window showing the zip file.

<img width="769" height="356" alt="image" src="https://github.com/user-attachments/assets/4a97b983-518f-45c1-b459-22f52ae996b4" />


This file can then be sent to someone else. To play the game, the person must extract (unzip) the zip file. One way of doing this is right-clicking the file and picking "Extract All...".

<img width="690" height="484" alt="image" src="https://github.com/user-attachments/assets/b0ebfd69-6e6c-496a-a239-b1dd84f48892" />


Once unzipped, the following files will be available. Now the person can just double-click `Froyo.exe` to run the game.

<img width="668" height="269" alt="image" src="https://github.com/user-attachments/assets/ece81fbb-462e-4f6e-b58d-25e792c3db57" />


### 5. Nothing
Selecting this option will close the PyLab Hub.






