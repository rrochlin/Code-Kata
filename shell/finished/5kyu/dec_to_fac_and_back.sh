#!/bin/bash
fact_array=(1 1 2 6 24 120 720 5040 40320 362880 3628800 39916800 479001600 6227020800 87178291200 1307674368000 20922789888000 355687428096000 6402373705728000 121645100408832000 2432902008176640000 51090942171709440000 1124000727777607680000 25852016738884976640000 620448401733239439360000 15511210043330985984000000 403291461126605635584000000 10888869450418352160768000000 304888344611713860501504000000 8841761993739701954543616000000 265252859812191058636308480000000 8222838654177922817725562880000000 263130836933693530167218012160000000 8683317618811886495518194401280000000 295232799039604140847618609643520000000 10333147966386144929666651337523200000000 371993326789901217467999448150835200000000)
dec2FactString () {
    local dec=$1
    local result=""
    local i=1
    while (( $(echo "$dec > 0" | bc) )); do
        res=$(echo "$dec % $i" | bc)
        if (( res > 9 )); then
            result+=$( printf "\\$(printf '%03o' "$res+55")" )
        else
            result+=$res
        fi
        dec=$(echo "$dec / $i" | bc)
        i=$(( i + 1 ))
    done
    echo $result | rev
}
factString2Dec () {
    local length=${#1}
    local string=$1
    local result=0
    for (( i=length; i>=2; i-- )); do
        coefficient=${string:$length-$i:1}
        if [[ $coefficient == [A-Z] ]]; then
            coefficient=$(( $( ord $coefficient ) - 55 ))
        fi
        fact_result=${fact_array[$i]}
        result=$(echo "$result + $coefficient * $fact_result" | bc)
    done
    echo $result
}

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}

if [ "$1" = "dec2FactString" ]; then
    dec2FactString $2
else
    factString2Dec $2
fi
times