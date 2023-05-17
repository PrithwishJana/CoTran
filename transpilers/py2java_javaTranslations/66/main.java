public void isAlphabaticOrder ( s ) {
    var n = len ( s );
    var c = { s [ i } for i in range ( len ( s ) ) ];
    c . sort ( var reverse = false );
    for i in range ( n ) :
        if (( c { i } != s { i } )) {
            return false;
        }
     return true;
}
if (var __name__ == '__main__') {
    var s = "aabbbcc";
    if (( isAlphabaticOrder ( s ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 