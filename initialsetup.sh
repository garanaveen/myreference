#!/bin/bash

#-h is test if file exists and is a link.
#Make a link in home directory.
if [ ! -h "$HOME/myreference" ]; then
    ln -sv $PWD $HOME/myreference
fi

export MYREFERENCE_ROOT=$PWD/

#Git config
git config --local user.email "garanaveen@gmail.com"
git config --local user.name "garanaveen"


