public void fun ( p ) {
    return p . index ( max ( p ) );
}
for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var p = list ( map ( int , input ( ) . split ( ) ) );
    l = {};
    var = p { 0 };
    ans = {};
    for j in range ( n ) :
        l . append ( { p [ j } , j ] );
    l . sort ( key = lambda x : x { 0 } );
    l = l { : : - 1 };
    ind = 0;
    ans . append ( p { l [ 0 } { 1 } : n ] );
    for j in range ( n - 1 ) :
        if (l { j + 1 } { 1 } > l { j } { 1 }) {
            temp = l { j + 1 };
            l { j + 1 } = l { j };
            l { j } = temp;
        }
         else{
            ans . append ( p { l [ j + 1 } { 1 } : l { j } { 1 } ] );
        }
    for j in range ( len ( ans ) ) :
        System.out.println ( * ans { j } , var end = " " );
    System.out.println ( );
