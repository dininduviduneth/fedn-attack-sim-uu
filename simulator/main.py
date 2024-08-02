from fedn import APIClient
import docker
import os
import sys
import json
import requests

def display_p1_options():
    with open("simulator/config/program_structure.json", 'r') as program_structure_json:
        program_structure = json.load(program_structure_json)

        print(f"Choose and option from below:", '\n')
        for option in program_structure['p1_options']:
            print(f"{option['id']} - {option['text']}")

        print()
        selected_option = int(input(": "))
        print()
        # ADD CODE TO HANDLE NON-INTEGER ENTRIES!
        return selected_option

def display_page1():
    p1_option = display_p1_options()
    return p1_option

def check_server_ip_config():
    file_path = "simulator/config/api_server_config.json"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            if data['initialized']:
                print(f"Server IP is configured to {data['api_server_ip']}", '\n')
            else:
                print("Server IP is not configured. Please configure from the Main Menu.", '\n')
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return True

def set_server_ip_config():
    COMBINER_IP = input("Enter the server IP: ")
    new_api_server_config = {
        'initialized': True,
        "api_server_ip": COMBINER_IP
    }

    with open('simulator/config/api_server_config.json', 'w') as json_file:
        json.dump(new_api_server_config, json_file)
        print(f"Successfully saved server IP configuration!")

    print(f"New API server configurations set - API Server at: {COMBINER_IP}", '\n')
    return True

def get_api_server_status():
    file_path = "simulator/config/api_server_config.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

        if data['initialized']:
            combiner_ip = data['api_server_ip']
            url = f"http://{combiner_ip}:8092/get_client_config"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
                if response.status_code == 200:
                    print(f"Server is running at: {data['api_server_ip']}", '\n')
                    return True
                else:
                    print(f"Server is not running at: {data['api_server_ip']}", '\n')
                    return True
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
                return True  
            except requests.exceptions.RequestException as err:
                print(f"Error occurred: {err}")
                return True  
            except json.JSONDecodeError:
                print("Error: The response is not a valid JSON.")
                return True  
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return True  
        else:
            print("Server IP is not configured. Please configure from the Main Menu.", '\n')  
            return True  

if __name__ == "__main__":
    landing = True

    print()
    print(f"WELCOME TO ATTACK SIMULATOR!")
    print(f"----------------------------", '\n')

    while landing:
        p1_option = display_page1()

        match p1_option:
            case 1:
                landing = check_server_ip_config()
            case 2:
                landing = set_server_ip_config()
            case 3:
                landing = get_api_server_status()
            case 10:
                exit()
            case _:
                print('Other entry!', '\n')