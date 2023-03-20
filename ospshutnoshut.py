import time
import logging
# pyATS import
from pyats import aetest
from genie.harness.base import Trigger

# Set up logging
log = logging.getLogger()

# Define the trigger class and steps
# This class inherits from the Trigger class
class ShutNoShutOSPF(Trigger):
    '''Shut and unshut OSPF'''
    @aetest.setup
    def prerequisites(self, uut):
        
        output = uut.parse('show ip ospf ')

        if output['vrf']['default']['address_family']['ipv4']['instance']['10']['enable'] != 'True':
            self.skipped("Ospf is configured")

    @aetest.test
    def shut(self, uut):
        uut.configure('''router ospf 10
                          shutdown''')

    @aetest.test
    def verify(self, uut):

          output = uut.parse('show ip ospf ')

          if output['vrf']['default']['address_family']['ipv4']['instance']['10']['enable'] =='True':
               self.failed("Shutdown ospf did not work")

    @aetest.test
    def unshut(self, uut):
        uut.configure('''router ospf 10
                          no shutdown''')

    @aetest.test
    def verify_recover(self, uut):

          output = uut.parse('show ip ospf ')

          if output['vrf']['default']['address_family']['ipv4']['instance']['10']['enable'] =='True':
               self.failed("OSPF recovered to previous state")

    