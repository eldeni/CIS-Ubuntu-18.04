import os
from os import listdir
from os.path import isfile, join
import subprocess

TESTS_PATH = os.path.abspath('../tests')

def runTest():
  print('TESTS_PATH: %s' % (TESTS_PATH))
  testGroupIdx = 1
  failCount = 0

  testDirs = os.listdir(TESTS_PATH)
  testDirs.sort()

  for f in testDirs:
    testPath = join(TESTS_PATH, f)
    if os.path.isdir(testPath):
      print('Test starting, testGroupIdx: %s, path: %s' %
            (testGroupIdx, testPath))

      cmd = f'bats {testPath} -t'
      p = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
      out = p.stdout.read()
      testGroupIdx += 1

      for l in out.splitlines():
        trimmedLine = l.decode('utf-8')
        if trimmedLine.startswith('not ok'):
          failCount += 1
          print(trimmedLine)

      print('Test done, testGroupIdx: %s, path: %s' % (testGroupIdx, testPath))

  print('Test all done, testGroupCount: %s, totalFailCount: %s' %
        (testGroupIdx, failCount))

if __name__ == "__main__":
    runTest()
