# This file sets up the virtual environment.
# Run "source setup.sh" each time you want to run the app.
# This file is all the requirements needed to run the app
# Add packages here as you install to do development


if [ ! -d venv ]
then
  virtualenv -p python3.5 venv
fi

. venv/bin/activate

#Packages needed by package manager
sudo apt-get install python3-dev


#Packages needed by python


