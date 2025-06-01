from os import getcwd, path
import yaml
import logging
import logging.config
import sys


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('logs_bot')

def load_config():
    project_path = getcwd()
    config_path = path.join(project_path, 'config', 'config.yaml')

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            if not isinstance(data, dict):
                logger.error('config.yaml file is not formatted correctly')
                raise ValueError('config.yaml file is not formatted correctly')
            logger.info('config.yaml file loaded successfully')
            return data

    except FileNotFoundError:
        logger.error('config.yaml file does not exist, project may be corrupted')
        raise FileNotFoundError('config.yaml file does not exist, project may be corrupted')

    except yaml.YAMLError as yaml_error:
        logger.error(f'Error formatting the config.yaml file: {yaml_error}')
        raise RuntimeError(f'Error formatting the config.yaml file: {yaml_error}')

    except Exception as error:
        logger.error(f'Unexpected error when trying to load configuration file: {error}')
        raise RuntimeError(f'Unexpected error when trying to load configuration file: {error}')
