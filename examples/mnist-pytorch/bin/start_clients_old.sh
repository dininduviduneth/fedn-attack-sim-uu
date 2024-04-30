#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <combiner_ip> <benign_client_count> <malicious_client_count> <attack_type>"
    exit 1
fi

# Access the first argument
combiner_ip="$1"
benign_client_count="$2"
malicious_client_count="$3"
attack_type="$4"

# Check if the provided values are integers
if ! [[ "$benign_client_count" =~ ^[0-9]+$ ]]; then
    echo "Error: The provided value for benign client count is not an integer."
    exit 1
fi

if ! [[ "$malicious_client_count" =~ ^[0-9]+$ ]]; then
    echo "Error: The provided value for malignant client count is not an integer."
    exit 1
fi

# source .mnist-pytorch/bin/activate && python3 bin/split_data --n_splits=$((benign_client_count + malicious_client_count))

# Loop for count of clients if benign_client_count is greater than 0
if [ "$benign_client_count" -gt 0 ]; then
    for i in $(seq 1 "$benign_client_count"); do
        echo "Starting benign_client$i"
        docker run -d \
        -v $PWD/client.yaml:/app/client.yaml \
        -v $PWD/data/clients/$i:/var/data \
        -e ENTRYPOINT_OPTS="--data_path=/var/data/mnist.pt" \
        --add-host=api-server:"$combiner_ip" \
        --add-host=combiner:"$combiner_ip" \
        --name benign_client$i \
        ghcr.io/scaleoutsystems/fedn/fedn:master-mnist-pytorch run client -in client.yaml --name benign_client$i
    done
fi

# Loop for count of clients if malicious_client_count is greater than 0
if [ "$malicious_client_count" -gt 0 ]; then
    for i in $(seq 1 "$malicious_client_count"); do
        client_number=$((benign_client_count + i))
        echo "Starting malicious_client$i"
        docker run -d \
        -v $PWD/client.yaml:/app/client.yaml \
        -v $PWD/data/clients/$client_number:/var/data \
        -e ENTRYPOINT_OPTS="--data_path=/var/data/mnist.pt --malicious=True --attack=$attack_type" \
        --add-host=api-server:"$combiner_ip" \
        --add-host=combiner:"$combiner_ip" \
        --name malicious_client$i \
        ghcr.io/scaleoutsystems/fedn/fedn:master-mnist-pytorch run client -in client.yaml --name malicious_client$i
    done
fi
