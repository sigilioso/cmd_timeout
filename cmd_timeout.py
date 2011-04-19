# -*- coding: utf-8 -*-
import subprocess, threading

class CommandTimeout(object):
    """
    Class to easily run an external command setting an timeout.
    """
    def __init__(self, cmd, timeout=None):
        """
        Creates an instance storing the cmd to run. If timeout is given, then
        runs the command.
        """
        self.cmd = cmd
        self.process = None
        if timeout:
            self.run(timeout)

    def run(self, timeout):
        """
        Runs cmd in a separated thread, if after <time> seconds it has not
        finished, the thread is killed.
        """
        def run_cmd():
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.wait()
        # Execute the command
        thread = threading.Thread(target=run_cmd)
        thread.start()
        # Wait for the command <timeout> seconds and then finish it
        thread.join(timeout)
        if thread.is_alive():
            self.process.terminate()
            thread.join()


