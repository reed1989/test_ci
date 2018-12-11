#!/bin/bash
shell_path=$(cd `dirname $0`; pwd)
make_file_path=$1
make_file_dir=`echo ${make_file_path%/*}`

cd ${make_file_dir}
pwd
echo "start to make clean"
make clean -f ${make_file_path}
echo "start to make"
make -f ${make_file_path}
echo "start to execute test case"
./run_test