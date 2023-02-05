# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
# IPs should be considered valid if they consist of four octets, with values between 0 
# and 255, inclusive.

# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/shell


# doesn't block 04 etc.
adr="$1"
ip_regex="(25[0-5]|2[0-4][0-9]|[1-9][0-9]|[01])"
adr_regex="\b$ip_regex\.$ip_regex\.$ip_regex\.$ip_regex\b"
if [[ $adr =~ $adr_regex ]]; then
    echo "True"
else
    echo "False"
fi