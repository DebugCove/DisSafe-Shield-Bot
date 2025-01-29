import json 
import os


def load_config():
    try:
        with open('config/config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('File not found')
        return None
    except json.JSONDecodeError:
        print('Error decoding JSON')
        return None
    except Exception as error:
        print(f'Error loading config: {error}')
        return None

def save_config(config):
    try:
        with open('config/config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('File not found')
        raise
    except json.JSONDecodeError:
        print('Error decoding JSON')
        raise
    except Exception as error:
        print(f'Error saving config: {error}')
        raise


def load_server_config(server_id):
    try:
        with open(f'config/servers/{server_id}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('File not found')
        return None
    except json.JSONDecodeError:
        print('Error decoding JSON')
        return None
    except Exception as error:
        print(f'Error loading server config: {error}')
        return None

def save_server_config(config, server_id):
    try:
        with open(f'config/servers/{server_id}.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('File not found')
        raise
    except json.JSONDecodeError:
        print('Error decoding JSON')
        raise
    except Exception as error:
        print(f'Error saving server config: {error}')
        raise


def create_config_file(server_id):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    config_folder = os.path.join(folder_path, 'servers')

    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    file_path = os.path.join(config_folder, f'{server_id}.json')

    data = {
        'server_id': server_id,
        'chat_voting_id': None,
        'chat_logs_id': None
    }

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f'An error occurred when creating the server file{server_id}: {error}')
