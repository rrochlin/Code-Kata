#!/bin/bash
#https://www.codewars.com/kata/52e1476c8147a7547a000811/train/shell
pw=$1
# reqs - over 6 chars in length, one+ uppercase, one+ lowercase, one+ digit, only alphanumeric
over_6_and_alnum="^[[:alnum:]]{6}[[:alnum:]]*$"
one_up="^.*[A-Z].*$"
one_low="^.*[a-z].*$"
one_dig="^.*[0-9].*$"
if [[ $pw =~ $over_6_and_alnum ]];then #&& $pw =~ $one_up && $pw =~ $one_dig && $pw =~ $one_low  ]]; then
    echo "true"
else
    echo "false"
fi
