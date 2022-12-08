# https://www.codewars.com/kata/55b3425df71c1201a800009c/train/shell

stat () {
    if [[ $1 == "" ]]; then echo ""; return; fi;
    IFS="," read -ra STATS <<< $1
    ARRAY=()
    entries=${#STATS[@]}
    for i in ${STATS[@]}; do
        IFS="|" read -ra TIME <<< "$i"
        ARRAY+=($(( ${TIME[0]}*60*60+${TIME[1]}*60+${TIME[2]} )))
    done
    readarray -t ARRAY < <(printf '%s\n' "${ARRAY[@]}" | sort -n)
    echo ${ARRAY[@]}
    max=${ARRAY[$entries-1]}
    min=${ARRAY[0]}
    total=0
    for i in "${ARRAY[@]}"; do
        total=$(( total + i ))
    done
    RANGE=$(( max - min ))
    MEAN=$(( total / entries ))
    if (( $entries%2 )); then
        MEDIAN=${ARRAY[entries/2]}
    else
        MEDIAN=($(((${ARRAY[entries/2]}+${ARRAY[entries/2-1]})/2)))
    fi
    echo $entries
    
    range=`printf "%02d" $(( RANGE/3600 ))`
    range+="|"
    range+=`printf "%02d" $(( RANGE%3600/60 ))`
    range+="|"
    range+=`printf "%02d" $(( RANGE%3600%60 ))`
    mean=`printf "%02d" $(( MEAN/3600 ))`
    mean+="|"
    mean+=`printf "%02d" $(( MEAN%3600/60 ))`
    mean+="|"
    mean+=`printf "%02d" $(( MEAN%3600%60 ))`
    median=`printf "%02d" $(( MEDIAN/3600 ))`
    median+="|"
    median+=`printf "%02d" $(( MEDIAN%3600/60 ))`
    median+="|"
    median+=`printf "%02d" $(( MEDIAN%3600%60 ))`
    
    echo "Range: $range Average: $mean Median: $median"

}
stat "$1"