#!/bin/bash

#hexo clean
#hexo generate
# git stash and pull First.
git add .
git commit -m "$1"
git push rpi master

#git reflog
