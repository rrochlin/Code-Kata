#!/bin/bash
declare -a lin=("n=$1; k=$2; ")
declare out="
${lin[@]}
define survivor(n, k) {
    if ( n==1 ){
        return 1
    }
    last = survivor(n-1, k)
    return ( (last + k - 1) % n + 1 )
}
print survivor(n, k)
quit
"
read out < <(bc < <(echo -e "$out"))    
echo "$out"