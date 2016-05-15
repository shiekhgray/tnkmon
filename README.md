# tnkmon

To get started:

pip install flask

cd /tmp
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build

cd /tmp
git clone --recursive https://github.com/WiringPi/WiringPi-Python.git
sudo apt-get install python-dev python-setuptools swig
cd WiringPi-Python
swig2.0 -python wiringpi.i
sudo python setup.py install

