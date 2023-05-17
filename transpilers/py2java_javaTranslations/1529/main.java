for i in range ( int ( input ( ) ) ) :
    n , x , a , var b = map ( int , input ( ) . split ( ) );
    var p = abs ( a - b );
    var q = p + x;
    if (q >= n - 1) {
        System.out.println ( n - 1 );
    }
     else{
        System.out.println ( q );
    }
