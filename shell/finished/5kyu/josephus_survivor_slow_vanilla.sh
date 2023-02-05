#!/bin/bash
n=$1
k=$2

function survivor () {
    if (( $1 == 1 )); then
        echo 1
    else
        n_minus_one=$( survivor $(( $1 - 1 )) $2 )
        last=$(( $n_minus_one + $2 - 1 ))
        echo $(( last % $1 + 1 ))
    fi
}

survivor $n $k