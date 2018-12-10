#!/usr/bin/env python

import sys
import os
import subprocess


def main():
    make_file_path = sys.argv[1]
    dir_path = os.path.dirname(os.path.realpath(make_file_path))
	print("dir_path is:" + dir_path)

    p_clean = subprocess.run(["make clean", "-f", make_file_path],
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    print(p_clean)
    print(p_clean.stdout.decode('utf-8'))

    p_make = subprocess.run(["make", "-f", make_file_path],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    # p_make.wait()
    print(p_make.stdout.decode('utf-8'))

    run_test_file = os.path.join(dir_path, "./run_test")
    p_run = subprocess.run([run_test_file],
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    print(p_run.stdout.decode('utf-8'))


if __name__ == '__main__':
    main()