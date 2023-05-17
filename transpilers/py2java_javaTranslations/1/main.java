var MAX_CHAR = 26 ;;
public void countFreq ( str1 , freq , len1 ) {
    for i in range ( len1 ) :
        freq { ord ( str1 [ i } ) - ord ( 'a' ) ] += 1 ;;
}
public void canMakePalindrome ( freq , len1 ) {
    var count_odd = 0 ;;
    for i in range ( MAX_CHAR ) :
        if (( freq { i } % 2 != 0 )) {
            count_odd += 1 ;;
        }
     if (( len1 % var 2 == 0 )) {
        if (( count_odd > 0 )) {
            return false ;;
        }
         else{
            return true ;;
        }
    }
     if (( count_odd != 1 )) {
        return false ;;
    }
     return true ;;
}
public void findOddAndRemoveItsFreq ( freq ) {
    var odd_str = "" ;;
    for i in range ( MAX_CHAR ) :
        if (( freq { i } % 2 != 0 )) {
            freq { i } -= 1 ;;
            odd_str += chr ( i + ord ( 'a' ) ) ;;
            return odd_str ;;
        }
     return odd_str ;;
}
public void findPalindromicString ( str1 ) {
    len1 = len ( str1 ) ;;
    freq = { 0 } * MAX_CHAR ;;
    countFreq ( str1 , freq , len1 ) ;;
    if (( canMakePalindrome ( freq , len1 ) == false )) {
        return "No Palindromic String" ;;
    }
     odd_str = findOddAndRemoveItsFreq ( freq ) ;;
    var front_str = "" ;;
    var rear_str = " " ;;
    for i in range ( MAX_CHAR ) :
        temp = "" ;;
        if (( freq { i } != 0 )) {
            ch = chr ( i + ord ( 'a' ) ) ;;
            for j in range ( 1 , int ( freq { i } / 2 ) + 1 ) :
                temp += ch ;;
            front_str += temp ;;
            rear_str = temp + rear_str ;;
        }
     return ( front_str + odd_str + rear_str ) ;;
}
var str1 = "malayalam" ;;
System.out.println ( findPalindromicString ( str1 ) ) ;;
