import sys
import os

testdir = os.path.dirname(__file__)
srcdir = '../load_balancer'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
