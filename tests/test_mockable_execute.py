#!/usr/bin/python

import unittest
import sys
import os
from centos_package_cron import mockable_execute

class MockableExecuteTestCase(unittest.TestCase):
    def testExecute(self):
        # arrange
        executor = mockable_execute.MockableExecute()

        # act
        result = executor.run_command(['cat','/etc/centos-release'])

        # assert
        expected_string = 'CentOS Linux release 7.7.1908 (Core)\n'
        self.assertEquals(result, expected_string)

if __name__ == "__main__":
            unittest.main()
