public void isPalindrome ( s ) {
    var l = len ( s );
    for i in range ( l // 2 ) :
        if (( s { i } != s { l - 1 - i } )) {
            return false;
        }
     return true;
}
public void createStringAndCheckPalindrome ( N ) {
    var sub = "" + chr ( N );
    var res_str = "";
    sum = 0;
    while (( N > 0 )) {
        digit = N % 10;
        sum += digit;
        N = N // 10;
    }
     while (( len ( res_str ) < sum )) {
        res_str += sub;
    }
     if (( len ( res_str ) > sum )) {
        res_str = res_str { 0 : sum };
     }
     if (( isPalindrome ( res_str ) )) {
        return true;
    }
     return false;
}
if (var __name__ == "__main__") {
    var N = 10101;
    if (( createStringAndCheckPalindrome ( N ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 