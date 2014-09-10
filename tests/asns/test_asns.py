#!/usr/bin/env python

from unittest import TestCase
from os.path import dirname, realpath, join
import pyasn
import os


# test - TODO:
#   0. decide on testing library (unit-test, nose, etc) -- see resources in TODO
      
#   1. tests: load normal, load binary, load w/o asnames
#   2. tests: check a bunch of random IPs, from different ASes; including in & out of smaller prefix levels
#   3. tests: exhaustive - check all of IPv4 against RIPESTAT/shadowserver
#   4. tests: check as-names

class LoadRadixPickle(TestCase):
    def setUp(self):
        print('ameye hadi')
        self.ipdb = pyasn.pyasn(os.path.join('resources", "ipasn_20140513.dat'))
        # self.data_dir = join(dirname(realpath(__file__)), 'data')

    
    def _check_8888(self):
        asn, prefix = self.ipdb.lookup('8.8.8.8')
        self.assertEqual(asn, 15169)
        self.assertEqual(prefix, '8.8.8.0/24')
        
    
    def _check_tud(self):
        pass # check a few from tud's ranges
        
    
    def _check_superset(self):
        pass # check the key cases where the IP maps to several prefixes, and most specific is important
        
    def _check_emtpy_and_bad(self):
       asn, prefix = self.ipdb.lookup('230.2.2.2')
       self.assertEqual(asn, None)
       self.assertEqual(prefix, None)
       self.ipdb.lookup_asn('300.3.4.4')  # todo: check that it raises expcetion
        

    def _check_ipv6(self):
        pass  # TODO: ? at minimum, manually add/remove from the data


    def _check_asn32(self):
        pass # check a few 
        
    def _check_binaryformat(self):
        pass  # TODO: open the binary file as ipdb2 ; then loop, running random lookups on it and self.ipdb and seeing if results are same
        
        

# todo: perhaps needed:        
# def main():
    # unittest.main()
# if __name__ == '__main__':
    # main()


      