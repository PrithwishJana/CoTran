for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) ) ; l = list ( map ( int , input ( ) . split ( ) ) );
    var a = set ( l );
    var l1 = {};
    for i in range ( 1 , n + 1 ) : l1 . append ( max ( i , len ( a ) ) );
    System.out.println ( * l1 );
