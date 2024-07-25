from fedn import APIClient
import docker
import os
import json
import requests

COMBINER_IP = ""

def get_api_server_config():
    file_path = "simulator/config/api_server_config.json"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_api_server_status(combiner_ip):
    url = f"http://{combiner_ip}:8092/get_client_config"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()  # Parse the JSON response
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        exit()
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        exit()
    except json.JSONDecodeError:
        print("Error: The response is not a valid JSON.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()

def main():
    # STEP 1 - VALIDATE
    print("Checking if the API server configurations are set...")
    api_server_config = get_api_server_config()
    if api_server_config['initialized']:
        COMBINER_IP = api_server_config['api_server_ip']
        print(f"API server configurations set - API Server at: {COMBINER_IP}")
    else:
        print("API server configurations are not set!")
        exit()

    # STEP 2 - CHECK API SERVER STATUS
    print("Checking if the API server is running..")
    api_server_status = get_api_server_status(COMBINER_IP)
    print(f"API Server Running at: Port {api_server_status['discover_port']}")

if __name__ == "__main__":
    main()