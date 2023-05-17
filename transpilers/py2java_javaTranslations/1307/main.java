public void squaresum ( n ) {
    var sm = 0;
    for i in range ( 1 , n + 1 ) :
        sm = sm + ( i * i );
    return sm;
}
var n = 4;
System.out.println ( squaresum ( n ) );
