# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the 
# strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.
# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/powershell

function in-array
{
    [OutputType([string[]])]
    Param ([string[]]$a1, [string[]]$a2)
    $new = $a1 | Sort-Object
    $r = @()
    foreach ($item in $new) {
        foreach ($a2item in $a2) {
            if ($a2item.contains($item)) {
                if (-not $r.Contains($item)){
                    $r += $item
                }
                break
            }
        }
    }
    return $r
}

$a1 = @("live", "arp", "strong") 
$a2 = @("lively", "alive", "harp", "sharp", "armstrong")
in-array $a1 $a2

$a1 = @("arp", "mice", "bull") 
$a2 = @("lively", "alive", "harp", "sharp", "armstrong")
in-array $a1 $a2  