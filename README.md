# Complementary Pairs

Two strings form a complementary pair if there exists some permutation of their concatenation that forms a palindrome. 
For example, the strings "abac" and "cab" form a complementary pair since their concatenation "abaccab" can be rearranged to form the palindrome "bcaaacb".

Given an array of strings, find the number of complementary pairs that can be formed. 
Note that pairs (i, j) and (j, i) are considered the same.

## Example
`stringData = ["abc", "abcd", "bc", "adc"]`

The complementary pairs are:
* ("abc", "abcd") - concatenated to "abcabcd", which can be arranged as "abcdcba"
* ("abc", "bc") - concatenated to "abcbc", which can be arranged as "bcacb"
* ("abcd", "adc") - concatenated to "abcdadc", which can be arranged as "acdbdca"

The answer is 3.

## Function Description
Complete the function `countComplementaryPairs` in the editor with the following parameters:
`string stringData[n]`: the strings to pair

**Returns**
`long_int`: the number of complementary pairs that can be formed

## Constraints
* `1 ≤ n ≤ 10^5`
* `1 ≤ length(stringData[i]) ≤ 3 * 10^5`
* `1 ≤ sum of the length of strings in stringData ≤ 3 * 10^5`
* All strings consist of lowercase English letters only.

## Input Format for Custom Testing
The first line contains an integer `n`, denoting the size of the array `stringData`.
Each line `i` of the `n` subsequent lines (where `0 ≤ i < n`) represents `stringData[i]`.

## Sample Case 0
### Sample Input 0
```
4
ball
all
call
bal
```

### Sample Output 0
`3`

### Explanation
The following complementary pairs can be formed:
* ("ball", "all"), concatenated string = "ballall" -> "allblla".
* ("ball", "bal"), concatenated string = "ballbal" -> "balllab".
* ("all", "call"), concatenated string = "allcall" -> "allclla".

## Sample Case 1
### Sample Input 1
```
3
eye
aa
c
```

### Sample Output 1
`2`

### Explanation
The following complementary pairs can be formed:
* ("eye", "aa"), concatenated string = "eyeaa" -> "eayae".
* ("aa", "c"), concatenated string = "aac" -> "aca".
