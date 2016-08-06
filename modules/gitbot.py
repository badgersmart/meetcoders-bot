#!/usr/bin/python
import time

from daemons.prefab import run
from communicate import Communicate
from tasks import GitTasks

class GitBot(run.RunDaemon):
    def setConfig(self,config):
        self.config = config

    def run(self):
        while True:
            git = GitTasks(self.config)
#            req = Communicate(self.config)
#            req.work_labels()
            time.sleep(60)