# -*- coding: utf-8 -*-
import os
import logging

__author__ = 'Guillaume Vincent'
__email__ = 'guillaume@oslab.fr'
__version__ = '0.1.0'

logger = logging.getLogger(__name__)


def _help_user_to_use_nice_api(key, default):
    type_default = str(type(default)).split("'")[1]
    if type_default not in ['bool', 'int', 'float', 'list']:
        return
    warning_message = 'type of {key} is not the same as the type of default value ({default} is type of {type_default})'
    logger.warning(warning_message.format(key=key, default=default, type_default=type_default))
    help_message = "use smartgetenv.get_{type_default}('{key}',{default}) method to cast env variable to {type_default}"
    logger.info(help_message.format(type_default=type_default, key=key, default=default))


def get_env(key, default=None):
    env_variable = os.getenv(key, default)

    if default and type(default) != type(env_variable):
        _help_user_to_use_nice_api(key, default)
    return env_variable


def _string_is_true(string):
    return string.lower() in ['true', '1', 't', 'y', 'yes']


def get_bool(key, default=None):
    env_variable = os.getenv(key, default)
    if isinstance(env_variable, bool):
        return env_variable
    return _string_is_true(env_variable)


def get_list(key, default=None, separator=';'):
    env_variable = os.getenv(key, default)
    if isinstance(env_variable, list):
        return env_variable
    return env_variable.split(separator)


def get_int(key, default=None):
    env_variable = os.getenv(key, default)
    if isinstance(env_variable, int):
        return env_variable
    return int(env_variable)


def get_float(key, default=None):
    env_variable = os.getenv(key, default)
    if isinstance(env_variable, float):
        return env_variable
    return float(env_variable)
