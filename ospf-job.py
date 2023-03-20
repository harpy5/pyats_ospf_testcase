import os

from genie.harness.main import gRun

def main():
    test_path = os.path.dirname(os.path.abspath(__file__))
    print(test_path)
    gRun(trigger_uids=('TriggerShutNoShutOSPF'),
        trigger_datafile='TriggerShutNoShutOSPF.yaml')