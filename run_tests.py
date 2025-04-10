import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.g_lists_and_tuples import test_dictionaries_and_sets 

suite = unittest.TestLoader().loadTestsFromModule(test_dictionaries_and_sets) 
unittest.TextTestRunner().run(suite) 