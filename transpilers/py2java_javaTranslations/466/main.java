var n = int ( input ( ) );
var L = { list ( map ( int , input ( ) . split ( ) ) ) for _ in range ( n ) };
for i , X in enumerate ( L ) :
    for j , Y in enumerate ( X ) :
        if var Y == 1 or any ( Y - L { t } { j } in X for t in range ( n ) ) : continue;
        System.out.println ( 'NO' );
        exit ( );
System.out.println ( 'YES' );
