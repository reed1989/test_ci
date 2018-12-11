#!/usr/bin/env python

import sys
import os
import subprocess


def main():
    make_file_path = sys.argv[1]
    dir_path = os.path.dirname(os.path.realpath(make_file_path))

    print("Start to make clean")
    p_clean = subprocess.Popen(["make clean", "-f", make_file_path],
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               cwd=dir_path)
    p_clean.wait()
    # for line in p_clean.stdout.readline():
    #     print(line)
#    print(p_clean.stdout.read().decode('utf-8'))
    result = p_clean.returncode
    if result == 0:
      print(p_clean.stdout.read().decode('utf-8'))
    else:
      print(p_clean.stderr.read().decode('utf-8'))

    print("Start to make make")
    p_make = subprocess.Popen(["make"],
                              shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              cwd=dir_path)
    p_make.wait()
    # for line in p_clean.stdout.readline():
    #     print(line)
    result = p_make.returncode
    if result == 0:
      print(p_make.stdout.read().decode('utf-8'))
    else:
      print(p_make.stderr.read().decode('utf-8'))
    


    print("Start to make execute the test case")
    run_test_file = os.path.join(dir_path, "./run_test")
    p_run = subprocess.Popen([run_test_file],
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             cwd=dir_path)
    p_run.wait()
    # for line in p_clean.stdout.readline():
    #     print(line)
    result = p_run.returncode
    if result == 0:
      print(p_run.stdout.read().decode('utf-8'))
    else:
      print(p_run.stderr.read().decode('utf-8'))



if __name__ == '__main__':
    main()