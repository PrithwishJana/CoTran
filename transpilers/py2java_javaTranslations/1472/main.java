var t = int ( input ( ) );
for c in range ( t ) :
    var n = int ( input ( ) );
    var seq = { int ( n ) for n in input ( ) . split ( ) };
    var posis = { None } * ( n + 1 );
    for u in range ( 0 , n ) :
        posis { seq [ u } ] = u;
    System.out.println ( 1 , var end = "" );
    l = posis { 1 } ;;
    r = posis { 1 };
    for num in range ( 2 , n + 1 ) :
        if ( posis { num } < l ) : l = posis { num };
        if ( posis { num } > r ) : r = posis { num };
        System.out.println ( 1 if num == r - l + 1 else 0 , end = "" );
    System.out.println ( );
