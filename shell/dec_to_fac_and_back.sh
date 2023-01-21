dec2FactString () {
    local dec=$1
    if (( dec<=1 )); then
        result=$(( dec ))0
        return
    fi
    result=""
    local i=0
    local current_fact=1
    local next_fact=1
    while (( $dec > $next_fact)); do
        i=$(( i + 1 ))
        current_fact=$next_fact
        next_fact=$(fact $i)
    done
    for (( i=$i-1; i>=0; i-- )); do
        current_fact=$( fact $i )
        res=$(( dec / current_fact ))
        result=$result$res
        dec=$(( dec - res * current_fact ))
    done
}
#TODO need to take this while loop above and make it recursive. the idea is to get the largest factorial
# then subtract it from the number, repeat until we hit 0 so we have the factorial representation.
factString2Dec () {
    local length=${#1}
    local string=$1
    result=""
    
}
chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}
fact () {
    f=1
    for (( i=1; i<=$1; i++)); do
        f=$(( i * f ))
    done
    echo $f
}

if [ "$1" = "dec2FactString" ]; then
    dec2FactString $2
else
    factString2Dec $2
fi

echo $result