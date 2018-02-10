# This file sets up the virtual environment.
# Run "source setup.sh" each time you want to run the app.
# This file is all the requirements needed to run the app
# Add packages here as you install to do development

bash ./pythoninstall.sh

sudo apt install python-pip
sudo pip install virtualenv

if [ ! -d venv ]
then
  virtualenv -p python3.5 venv
fi

if [ ! -d ../neo-python ]
then 
    git clone https://github.com/CityOfZion/neo-python.git ../neo-python
fi

. venv/bin/activate

#Packages needed by package manager
# python3.5-dev may not be found if running ubuntu but may be needed for other debian distros
sudo apt-get install libleveldb-dev python3-pip libssl-dev python3.5-dev


#Packages needed by python
pip install -r ../neo-python/requirements.txt
pip install -e ../neo-python

#Chain sync
cd ../neo-python
python bootstrap.py
cd ../NotGameChain
