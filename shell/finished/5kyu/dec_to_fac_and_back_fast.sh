#!/bin/bash
# super fast method i stole from some guy on codewars, I think the main difference is minimizing
# calls to bc by writing a large logical flow to execute with bc
# * factorial numbers
# arbitrary precision via bc

# ** define digit/place values. e.g 'K'=#20

declare    fdigits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ** build an associative array for digit values

declare -A fdigitvalue=()
declare -i n="${#fdigits}"
for ((i=0;i<n;i++))
    do fdigitvalue["${fdigits:$i:1}"]="$i"
done


# *** f2d() - factorial to decimal
# break the factonum into an array of values by place
# then have bc roll a factorial while mulsumming a decimal value

bc-f2d(){
    declare num="$1"
 
    # preparation of the array to eval
    declare -i len="${#num}" pos 
	  declare -a lin=("cnt=$len; ")
    declare chr=""
    pos=$((len-1))
    #declare -p num len pos lin
    for ((i=0;i<len;i++)); do
		  chr="${num:$pos:1}"
  		lin+=("num[$i]=0${fdigitvalue["$chr"]}; ")
      #declare -p chr 
  		pos=$((pos-1))
  	done
    
    # create a script, run and compute. 
    declare out="
    ${lin[@]}
    sum=num[0]
    ind=1
    prv=1
    while(ind<cnt){
	     fac=ind*prv
	     prv=fac
	     sum=sum+(num[ind]*fac)
	     ind=ind+1
    }

    print sum
    quit
    "
	  #echo -e "$out"

    read out < <(bc < <(echo -e "$out"))    
    
    # that's it, echo the decimal value
    # built by bc from the array.
    echo "$out"
}


# *** d2f() - decimal to factorial
# pass the decimal and have bc compute the remainders into an array
# then map the values from that array into digits and build a string.

bc-d2f(){
 	declare -a digitvalues=()
  read -a digitvalues < <(bc <<HERE

  scale=0
  define d2f(n){
    # builds an reverse list of values for places in a factorial number
    # each division makes a significant digit. read as array, translate to chars.
    auto i,v,r,x;
    print "0 ";
    i=2;
    x=n;
    v=0;
    r=0;
    while(i<99){
    	v=x/i;
    	r=x-(i*v);
    	print r," "
    	if (v==0) return;
    	x=v;
    	i=i+1;
    }
  }

  .=d2f($1)
quit
HERE
  )

  declare out=""
	declare -i val=0  
  
  # prepend incoming digits cause the division ran in reverse.
	for val in "${digitvalues[@]}"; do
		out="${fdigits:${val}:1}$out"
	done
  
  # that's it, echo the factonum
  # built from bc's output.
	echo "$out"
}


# ** main 

testing(){
  case "$1" in
	"dec2FactString") res=$(bc-d2f $2);;
	"factString2Dec") res=$(bc-f2d $2);;
	*) echo "error"; return 1;;
  esac
  if [ -z "$3" ]; then 
    echo $res
    return 0
  elif [ "$res" = "$3" ]; then ok="== OK!"; else ok="== KO: $3"; fi
  echo "$2 -> $res $ok"
}

if [ -n "$1" ]; then 
  testing "$1" "$2"
  times
fi
