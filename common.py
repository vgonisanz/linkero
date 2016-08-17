# -*- coding: utf-8 -*-

import logging
import json
from submodules.common import bcolors

version = "0.3.1"

def printWellcome():
    print(bcolors.HEADER+"")
    print("-----------------------------------------------------")
    print(bcolors.OKBLUE+"")
    print("  _____                                "+bcolors.WARNING+"|`-._/\_.-`|"+bcolors.OKBLUE)
    print(" |_   _|                               "+bcolors.WARNING+"|    ||    |"+bcolors.OKBLUE)
    print("   | |  _ __   __ _ _ __ __ _ _ __     "+bcolors.WARNING+"|___o()o___|"+bcolors.OKBLUE)
    print("   | | | '_ \ / _` | '__/ _` | '_ \    "+bcolors.WARNING+"|__((<>))__|"+bcolors.OKBLUE)
    print("  _| |_| | | | (_| | | | (_| | | | |   "+bcolors.WARNING+"\   o\/o   /"+bcolors.OKBLUE)
    print(" |_____|_| |_|\__, |_|  \__,_|_| |_|   "+bcolors.WARNING+" \   ||   / "+bcolors.OKBLUE)
    print("               __/ |                   "+bcolors.WARNING+"  \  ||  /  "+bcolors.OKBLUE)
    print("              |___/                    "+bcolors.WARNING+"   '.||.'   "+bcolors.OKBLUE)
    print(""+bcolors.ENDC)
    print("                                        Engineering  ")
    print(" v"+version+bcolors.HEADER+"")
    print("-----------------------------------------------------")
    print(""+bcolors.ENDC)


def loadConfig(logger):
    print(bcolors.WARNING)

    if logger.getEffectiveLevel() != logging.DEBUG:
        logger.info("Running in Release Mode")

        with open('config/config.json') as config_file:
            config = json.load(config_file)
            logger.info("Loaded: config/config.json")
    else:
        logger.info("Running in Debug Mode")

        with open('config/test/config.json') as config_file:
            config = json.load(config_file)
            logger.info("Loaded: config/test/config.json")

    print(bcolors.ENDC)
    return (config)
