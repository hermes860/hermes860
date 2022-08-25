#!/bin/bash

figlet cover_your_tracks

echo "Program by Jakub"

sudo echo "" /var/log/auth.log

sudo echo "" ~/.zsh_history

# sudo history -c

sudo export HISTFILE=0

sudo export HISTSIZE=0

sudo unset HISTFILE

sudo ln /dev/null ~/.zsh_history -sf

sudo kill -9 $$

echo "Your tracks was cleared"

echo "Happy Hacking!!! :-D"
