public void compute_lps ( s ) {
    var n = len ( s );
    lps = { 0 for i in range ( n ) };
    Len = 0;
    lps { 0 } = 0;
    i = 1;
    while (( i < n )) {
        if (( s { i } == s { Len } )) {
            Len += 1;
            lps { i } = Len;
            i += 1;
        }
         else{
            if (( Len != 0 )) {
                Len = lps { Len - 1 };
            }
             else{
                lps { i } = 0;
                i += 1;
            }
        }
    }
     return lps;
}
public void Longestsubstring ( s ) {
    lps = compute_lps ( s );
    n = len ( s );
    if (( lps { n - 1 } == 0 )) {
        System.out.println ( - 1 );
        exit ( );
    }
     for i in range ( 0 , n - 1 ) :
        if (( lps { i } == lps { n - 1 } )) {
            System.out.println ( s { 0 : lps [ i } ] );
            exit ( );
        }
     if (( lps { lps [ n - 1 } - 1 ] == 0 )) {
        System.out.println ( - 1 );
    }
     else{
        System.out.println ( s { 0 : lps [ lps [ n - 1 } - 1 ] ] );
    }
}
var s = "fixprefixsuffix";
Longestsubstring ( s );
