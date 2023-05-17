public void modularSum ( arr , n , m ) {
    if (( n > m )) {
        return true;
    }
     var DP = { false for i in range ( m ) };
    for i in range ( n ) :
        if (( DP { 0 } )) {
            return true;
        }
         var temp = { false for i in range ( m ) };
        for j in range ( m ) :
            if (( DP { j } == true )) {
                if (( DP { ( j + arr [ i } ) % m ] == false )) {
                    temp { ( j + arr [ i } ) % m ] = true;
                }
             }
         for j in range ( m ) :
            if (( temp { j } )) {
                DP { j } = true;
            }
         DP { arr [ i } % m ] = true;
    return DP { 0 };
}
var arr = { 1 , 7 };
var n = len ( arr );
var m = 5;
System.out.println ( "YES" ) if ( modularSum ( arr , n , m ) ) else System.out.println ( "NO" );
