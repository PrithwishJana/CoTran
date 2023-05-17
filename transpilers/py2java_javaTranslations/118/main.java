public void isAnyNotPalindrome ( s ) {
    var unique = set ( );
    for i in range ( 0 , len ( s ) ) :
        unique . add ( s { i } );
    if (( len ( unique ) > 1 )) {
        return true;
    }
     else{
        return false;
    }
}
if (var __name__ == '__main__') {
    var s = "aaaaab";
    if (( isAnyNotPalindrome ( s ) )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 