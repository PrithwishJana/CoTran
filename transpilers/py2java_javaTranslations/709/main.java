while (true) {
    n , var m = map ( int , input ( ) . split ( ) );
    if (n == m == 0) {
        break;
    }
     var students = { 0 for _ in range ( n ) };
    for _ in range ( m ) :
        var scores = list ( map ( int , input ( ) . split ( ) ) );
        for i in range ( n ) :
            students { i } += scores { i };
    System.out.println ( max ( students ) );
}
 