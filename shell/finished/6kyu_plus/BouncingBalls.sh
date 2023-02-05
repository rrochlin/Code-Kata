# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/shell
#  $1 >= 0 && $2 > 0 && $2 < 1 && $3 < $1 

#!/bin/bash

bouncingBall() {
    check=`echo "$1 >= 0 && $2 > 0 && $2 < 1 && $3 < $1" | bc`
    h=$1
    bounce=$2
    window=$3
    bounces=0
    # (( )) tells bash to evaluate i.e. will take 0 or 1 and give it as exit code
    if (( $check )); then
        while true; do
            # -l tag on bc will return long data types
            h=`echo "$h*$bounce" | bc -l`
            stop=`echo "$h <= $window" | bc`
            bounces=$[$bounces+1]
            echo $h
            if (( $stop ));then
                echo $bounces
                break
            fi
            bounces=$[$bounces+1]
        done
    else
        echo -1
    fi
}
bouncingBall $1 $2 $3