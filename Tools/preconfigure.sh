sudo apt -y update
sudo apt -y upgrade
sudo apt -y autoremove
apt -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tar.xz
tar -xf Python-3.10.2.tar.xz
cd python-3.10.2
bash ./configure --enable-optimizations
make altinstall
python3 --version
apt -y install python3-pip
cd ~/Photo-Booth

