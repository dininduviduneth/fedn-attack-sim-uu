from fedn import APIClient
import time
# import uuid
# import json
# import numpy as np
# import collections
# import sys
# sys.path.append('/home/ubuntu/fedn-attack-sim-uu/examples/mnist-pytorch')

from combiner_config import COMBINER_IP

print(f"Combiner IP: {COMBINER_IP} is set")

DISCOVER_HOST = COMBINER_IP
DISCOVER_PORT = 8092
client = APIClient(DISCOVER_HOST, DISCOVER_PORT)

print(f"API Client connected to combiner at: {DISCOVER_HOST}:{DISCOVER_PORT}")

sessions_list = client.list_sessions()['result']
if len(sessions_list) != 0:
    print(f"Number of sessions: {len(sessions_list)}")
    for id, session in enumerate(sessions_list):
        print(f"{id} - {session['session_id']}")
else:
    print("No sessions yet")

client._get_url('set_package')

client.set_package('package.tgz', 'numpyhelper')
client.set_initial_model('seed.npz')
seed_model = client.get_initial_model()

session_id = input("Set session_id: ")
rounds = input("Set the number of rounds: ")

session_config_fedavg = {
    "helper": "numpyhelper",
    "session_id": session_id,
    "aggregator": "fedavg",
    "model_id": seed_model['model_id'],
    "rounds": int(rounds)
}

result_fedavg = client.start_session(**session_config_fedavg)
time.sleep(10)

def run_until_finished(session_id):
    while not client.session_is_finished(session_id):
        models = client.list_models(session_id)
        print(f"Rounds: {models['count']} out of {session_config_fedavg['rounds']} completed!", end="\r")
        time.sleep(15)

# Call the function
run_until_finished(session_id) 

if client.session_is_finished(session_id):
    print(f"The session: {session_id} is over!")