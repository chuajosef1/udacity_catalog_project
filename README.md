# Catalog Project

The second assignment in Udacity's full stack web development nanodegree program.

## Project Overview

You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system.
Registered users will have the ability to post, edit and delete their own items.

## Requirements

[Python 3](https://www.python.org/download/releases/3.0/) - The code uses ver 3.6.4\
[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager\
[VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.\
[Git](https://git-scm.com/downloads) - A free and open source distributed version control system.\

## How to run the program?

Follow these steps below to access the project:

1. Download the latest verison of python from the link above.
2. Download and install Vagrant,VirtualBox, and Git.
3. Download this Udacity provided [folder](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) with preconfigured vagrant settings.
4. Clone this repository directly into the downloaded folder `FSND-Virtual-Machine\vagrant`.
5. Once the steps above are completed right-click in the folder and select `git bash`.
6. Once 'git bash' is brought up, type `vagrant up` let it download everything, this may take some time.
7. After vagrant has downloaded everything, type `vagrant ssh` and you should see something like this `vagrant@vagrant:~\$` type `cd /vagrant`.
8. Before running the program run `database_setup.py` and then `populatedatabase.py` to create your database.
9. Navigate to the folder named after this repository and type `python loganalysis.py` to run the program.

## Troubleshooting

If you are having trouble accessing the `\vagrant` folder once you are in `vagrant ssh`, do these steps to try and fix the error.

1. First press `ctrl+d` to exit vagrant.
2. Type `vagrant halt` this will completely shutdown the virtual machine.
3. Check `task manager` to make sure no other `Virtual Box` programs are running.
4. Close all programs involving any files contained within the folder `FSND-Virtual-Machine`.
5. Close out `Git Bash`.
6. Once that is done, open up the `FSND-Virtual-Machine\vagrant` and right-click to select `Git Bash` .
7. Type 'vagrant up', then `vagrant ssh`.
8. After that type `cd /vagrant` and type `ls` to check to see if you now have access to all the shared files contained within the folder.
