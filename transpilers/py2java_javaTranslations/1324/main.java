public void isSubstring ( s1 , s2 ) {
    var M = len ( s1 );
    var N = len ( s2 );
    for i in range ( N - M + 1 ) :
        for j in range ( M ) :
            if (( s2 { i + j } != s1 { j } )) {
                break;
            }
         if (j + var 1 == M) {
            return i;
        }
     return - 1;
}
if (__name__ == "__main__") {
    s1 = "for";
    var s2 = "geeksforgeeks";
    var res = isSubstring ( s1 , s2 );
    if (res == - 1) {
        System.out.println ( "Not present" );
    }
     else{
        System.out.println ( "Present at index " + str ( res ) );
    }
}
 