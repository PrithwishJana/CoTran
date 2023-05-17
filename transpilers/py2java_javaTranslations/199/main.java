var i = input ; l = 3;
for _ in { 0 } * int ( i ( ) ) :
    var x = int ( i ( ) );
    if x == l : System.out.println ( 'NO' ) ; exit ( );
    l ^= x;
System.out.println ( 'YES' );
