public void searchnode ( i , u , path ) {
    var r = 1;
    u { i } = 1;
    for j in range ( 26 ) :
        if (path { i } { j } and ( not u { j } )) {
            r += searchnode ( j , u , path );
        }
     return r;
}
while (( true )) {
    var n = int ( input ( ) );
    if not n : break;
    var strs = list ( map ( lambda x : { x [ 0 } , x { - 1 } ] , { input ( ) for i in range ( n ) } ) );
    ss , var ee = { 0 } * 26 , { 0 } * 26;
    var path = { [ 0 } * 26 for _ in range ( 27 ) ];
    var u = { 0 } * 26;
    for s , e in strs :
        ss { ord ( s ) - ord ( 'a' ) } += 1;
        ee { ord ( e ) - ord ( 'a' ) } += 1;
        path { ord ( s ) - ord ( 'a' ) } { ord ( e ) - ord ( 'a' ) } += 1;
    if ({ 1 for s1 , e1 in zip ( ss , ee ) if s1 - e1 }) {
        System.out.println ( "NG" );
        continue;
    }
     System.out.println ( "OK" if len ( { 1 for s in ss if s } ) == searchnode ( ord ( s ) - ord ( 'a' ) , u , path ) else "NG" );
}
 