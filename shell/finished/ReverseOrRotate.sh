# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/shell

#!/bin/bash
revrot () {
    # -z checks if variable is empty, if you enter "" for the first arg bash will ignore
    # so you need to check if $2 exists to see if $1 does
    if [ -z $2 ] || (( $2 <= 0 )) || (( $2 > ${#1} )); then echo ""; return; fi
    str=$1
    sz=$2
    chunks=""
    for (( i=0; i<${#str}/$sz; i++ )); do
        let s=$i*$sz
        chunk=${str:s:sz}
        total=0
        while read -n1 nums; do
            total=$(( total + nums**3 ))
        done < <(echo -n "$chunk")
        if (( total%2 )); then
            chunks+=${chunk:1:sz-1}${chunk:0:1}
        else
            chunks+=`echo $chunk | rev`
        fi
    done
    echo $chunks

}
revrot $1 $2
