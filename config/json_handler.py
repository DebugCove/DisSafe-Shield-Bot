from json import load, dump, JSONDecodeError


def load_config():
    try:
        with open('config/config.json', 'r', encoding='utf-8') as f:
            return load(f)
    except JSONDecodeError:
        raise JSONDecodeError('Error reading config.json file')
    except FileNotFoundError:
        raise FileNotFoundError('File config.json not found')
    except Exception as error:
        raise Exception(f'Unexpected error: {error}')


def save_config(config):
    try:
        with open('config/config.json', 'w', encoding='utf-8') as f:
            dump(config, f, indent=4)
    except JSONDecodeError:
        raise JSONDecodeError('Error reading config.json file')
    except FileNotFoundError:
        raise FileNotFoundError('File config.json not found')
    except Exception as error:
        raise Exception(f'Unexpected error: {error}')
