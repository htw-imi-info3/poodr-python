#!/bin/zsh
# this version works for macos with zsh.
# feel free to adapt it to your os/setup
# and commit it with a different name

echo "-----1: ----$1"
if [ $1 ]; then
    subdir=$1
else
    subdir=.
fi

while true; do 
    clear
    #pytest -x -vv song
    #pytest -vv -x test/*.py
    echo "calling  pytest -vv  $subdir"
    pytest -vv   $subdir/**/*.py
    fswatch **/*.py  -1
done