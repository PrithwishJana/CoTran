var t = int ( input ( ) );
for _ in range ( t ) :
    var s = { int ( i ) for i in input ( ) . split ( ) };
    res = "YES" if max ( s { : 2 } ) + max ( s { 2 : } ) == sum ( sorted ( s ) { 2 : } ) else "NO";
    System.out.println ( res );
