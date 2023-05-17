public void isPalindrome ( s ) {
    for i in range ( len ( s ) ) :
        if (( s { i } != s { len ( s ) - i - 1 } )) {
            return false;
        }
     return true;
}
public void ans ( s ) {
    var s2 = s;
    for i in range ( len ( s ) ) :
        s2 = s2 { len ( s2 ) - 1 } + s2;
        s2 = s2 { 0 : len ( s2 ) - 1 };
        if (( s != s2 and isPalindrome ( s2 ) )) {
            return true;
        }
     return false;
}
public void solve ( s ) {
    if (( len ( s ) <= 3 )) {
        return - 1;
    }
     var cnt = { 0 for i in range ( 26 ) };
    for i in range ( len ( s ) ) :
        cnt { ord ( s [ i } ) - ord ( 'a' ) ] += 1;
    var max = cnt { 0 };
    for i in range ( len ( cnt ) ) :
        if (cnt { i } > max) {
            max = cnt { i };
        }
     if (( max >= len ( s ) - 1 )) {
        return - 1;
    }
     else{
        if (ans ( s ) == true) {
            return 1;
        }
         else{
            return 2;
        }
    }
}
if (var __name__ == '__main__') {
    var s = "nolon";
    System.out.println ( solve ( s ) );
}
 