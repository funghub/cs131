#!/bin/bash

# shell function
christmasyet () {
	if date +%F | grep -e "-12-25"; then
		echo "It is Christmas!"
	else
		echo "Not Christmas yet :'("
	fi
}

# a function that will cd into the file you want
# then show list of paths after . (including hidden) with the depth specified by user
# if no argument, it will list paths 1 level deep
gofile () {
	if [[ -n "$1" && -e "$1" ]]; then  # user enters a path as 1st argument and it exists as file
		cd "$1"
		if [ -n "$2" ]; then  # user enters 1st argument then 2nd argument as a depth level file tree
			find . -maxdepth "$2"
		fi	
	else  # user does not enter any arguments
		find . -maxdepth 1

	fi
}

# aliases
alias hello="echo hello"
alias ls_nice="ls -alh" # quickly give human readable ls and hidden files nicely in a list
alias cs131-ssh="ssh ishigaki-cs7@100.107.21.115"
