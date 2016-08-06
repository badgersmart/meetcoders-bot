#!/usr/bin/env python

import logging
import os
import sys
import time

from modules import GitBot
from modules import ConfigLoader

if __name__ == '__main__':

    action = sys.argv[1]
    config = ConfigLoader(os.path.join(os.getcwd(), "config.cfg"))
    logging.basicConfig(filename=config.get_log_path_file(), level=logging.DEBUG)

    d = GitBot(pidfile=config.get_pid_path_file())
    d.setConfig(config)

    if action == "start":

        d.start()

    elif action == "stop":

        d.stop()

    elif action == "restart":

        d.restart()
