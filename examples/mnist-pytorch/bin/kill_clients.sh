docker kill $(docker ps -aq --filter "name=client")
docker rm $(docker ps -aq --filter "name=client")
sudo rm -rf data/clients/