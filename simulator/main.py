from fedn import APIClient
import docker
import os
import shutil
import sys
import json
import requests

def get_combiner_ip():
    with open("/home/ubuntu/fedn-attack-sim-uu/simulator/config/api_server_config.json", "r") as file:
        config = json.load(file)
    
    if config['initialized']:
        return config['api_server_ip']
    else:
        print(f"API configuration has not been set!")
        return True

def display_p1_options():
    with open("simulator/config/program_structure.json", 'r') as program_structure_json:
        program_structure = json.load(program_structure_json)

        print(f"Choose an option from below:", '\n')
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

def show_models():
    with open("simulator/config/models.json", "r") as json_file:
        models = json.load(json_file)

    print(f"Model\t\t\t| Model Initialized\t| Model Uploaded")
    for model in models:
        print(f"{model['id']} - {model['model_id']}\t| {model['env_initialized']}\t\t\t| {model['data_uploaded']}")

    print()
    return True

def copy_sim_template(model_id, path):
    shutil.copytree(f"simulator/sim-template", f"{path}/sim-template")

    if os.path.exists(f"{path}/sim-template"):
        os.rename(f"{path}/sim-template", f"{path}/{model_id}")
        print("Model template copied successfully!", '\n')
    
    if os.path.exists(f"{path}/sim-template"):
        os.rmdir(f"{path}/sim-template")
        os.rmdir(f"{path}")

    return True

def insert_parameterized_files(model_id):
    try:
        # Read the content from the template file
        with open("simulator/sim-param-files/gitignore.txt", 'r') as file:
            content = file.read()

        # Replace the placeholder with the actual model_id
        content = content.replace('{model_id}', model_id)

        # Write the modified content to the output file
        with open(f"examples/{model_id}/.gitignore", 'w') as file:
            file.write(content)

        print(f"Successfully created examples/{model_id}/.gitignore with model_id {model_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # Read the content from the template file
        with open("simulator/sim-param-files/init_venv.txt", 'r') as file:
            content = file.read()

        # Replace the placeholder with the actual model_id
        content = content.replace('{model_id}', model_id)

        # Write the modified content to the output file
        with open(f"examples/{model_id}/bin/init_venv.sh", 'w') as file:
            file.write(content)

        print(f"Successfully created examples/{model_id}/bin/init_venv.sh with model_id {model_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # Read the content from the template file
        with open("simulator/sim-param-files/start_clients.txt", 'r') as file:
            content = file.read()

        # Replace the placeholder with the actual model_id
        content = content.replace('{model_id}', model_id)

        # Write the modified content to the output file
        with open(f"examples/{model_id}/bin/start_clients.sh", 'w') as file:
            file.write(content)

        print(f"Successfully created examples/{model_id}/bin/start_clients.sh with model_id {model_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # Read the content from the template file
        with open("simulator/sim-param-files/test_simulation.txt", 'r') as file:
            content = file.read()

        # Replace the placeholder with the actual model_id
        content = content.replace('{model_id}', model_id)

        # Write the modified content to the output file
        with open(f"examples/{model_id}/test_simulation.py", 'w') as file:
            file.write(content)

        print(f"Successfully created examples/{model_id}/test_simulation.py with model_id {model_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        COMBINER_IP = get_combiner_ip()
        # Read the content from the template file
        with open("simulator/sim-param-files/client.txt", 'r') as file:
            content = file.read()

        # Replace the placeholder with the actual model_id
        content = content.replace('{combiner_ip}', COMBINER_IP)

        # Write the modified content to the output file
        with open(f"examples/{model_id}/client.yaml", 'w') as file:
            file.write(content)

        print(f"Successfully created examples/{model_id}/client.yaml with model_id {model_id}", '\n')

    except Exception as e:
        print(f"An error occurred: {e}")

def copy_uploads(model_id):
    # Copy data
    shutil.copytree(f"simulator/sim-upload/data", f"examples/{model_id}/data")
    # Copy entrypoint
    shutil.copy(f"simulator/sim-upload/entrypoint", f"examples/{model_id}/client/entrypoint")
    # Copy split_data
    shutil.copy(f"simulator/sim-upload/split_data", f"examples/{model_id}/bin/split_data")
    # Copy requirements.txt
    shutil.copy(f"simulator/sim-upload/requirements.txt", f"examples/{model_id}/requirements.txt")

    print("All uploads have been copied!", '\n')

    return True

def set_all_executable_permissions(directory):
    try:
        # Walk through all files and directories in the specified directory
        for root, dirs, files in os.walk(directory):
            for name in files:
                file_path = os.path.join(root, name)
                os.chmod(file_path, 0o777)
                print(f"Set executable permissions for file: {file_path}")
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.chmod(dir_path, 0o777)
                print(f"Set executable permissions for directory: {dir_path}")
                
        # Also set permissions for the main directory
        os.chmod(directory, 0o777)
        print(f"Set executable permissions for directory: {directory}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def add_model():
    model_id = "sim-" + input("Enter model_id: ")
    model_name = input("Enter a model name: ")
    path = f"examples/{model_id}" 
    print(f"The new model is: {model_id}", '\n')

    with open("simulator/config/models.json", "r") as models_json:
        models = json.load(models_json)
        model_count = len(models)

    new_model_dict = {
        "id": model_count + 1,
        "model_id": model_id,
        "model_name": model_name,
        "path": path,
        "fixed": False,
        "env_initialized": False,
        "data_uploaded": False
    }

    # ADD THE NEW MODEL TO JSON
    models.append(new_model_dict)

    with open("simulator/config/models.json", "w") as models_json:
        json.dump(models, models_json, indent=4)

    copy_sim_template(model_id, "examples")

    insert_parameterized_files(model_id)

    set_all_executable_permissions(f"examples/{model_id}")

    return copy_uploads(model_id)

def delete_model():
    with open("simulator/config/models.json", "r") as models_json:
        models_list = json.load(models_json)

    print(f"Model\t\t\t| Model Initialized\t| Model Uploaded")
    for model in models_list:
        print(f"{model['id']} - {model['model_id']}\t| {model['env_initialized']}\t\t\t| {model['data_uploaded']}")
    
    print()
    remove_id = int(input(f"Select a model to delete: "))
    
    for model in models_list:
        if model['id'] == remove_id:
            if model['fixed']:
                print(f"{model['model_id']} is a fixed model and cannot be deleted!")
                return True
            else:
                # Check if the folder exists
                folder_path = f"{model['path']}"
                if not os.path.exists(folder_path):
                    print(f"Folder {folder_path} does not exist.")
                    return True
                
                # Remove the folder and its contents
                shutil.rmtree(folder_path)
                print(f"Successfully removed folder: {folder_path}")

                models_list.pop(remove_id - 1)

    for id, model in enumerate(models_list):
        model['id'] = id + 1

    with open("simulator/config/models.json", "w") as models_json:
        json.dump(models_list, models_json, indent=4)
    
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
            case 4:
                landing = show_models()
            case 5:
                landing = add_model()
            case 6:
                landing = delete_model()
            case 10:
                exit()
            case _:
                print('Other entry!', '\n')