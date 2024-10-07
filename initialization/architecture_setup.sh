# Cloning the fedn repository from master
# git clone https://github.com/scaleoutsystems/fedn.git
git clone https://github.com/dininduviduneth/fedn-attack-sim-uu.git

# Installing local dependencies
sudo apt -y update

# DOCKER INSTALLATION --> https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
# Add Docker's official GPG key:
sudo apt-get -y update
sudo apt-get -y install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# INSTALL DOCKER PACKAGES
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# TO MANAGE DOCKER AS A NON-ROOT USER
# Create docker group
sudo groupadd docker

# Add my user to the docker group
sudo usermod -aG docker $USER

# A LOG OUT AND LOG BACK IN IS REQUIRED SO THAT THE GROUP MEMBERSHIP IS RE-EVALUATED
echo -e 'PLEASE LOG BACK AND LOG IN FOR THE NON-ROOT USER CHANGES TO BE EFFECTIVE!'

# INSTALL DOCKER_COMPOSE
sudo apt -y install docker-compose

# INSTALL PYTHON AND PYTHON PACKAGES
sudo apt -y install python3-pip
sudo apt -y install python3.10-venv
