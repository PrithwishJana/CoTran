public void initializeDiffArray ( A ) {
    var n = len ( A );
    var D = { 0 for i in range ( 0 , n + 1 ) };
    D { 0 } = A { 0 } ; D { n } = 0;
    for i in range ( 1 , n ) :
        D { i } = A { i } - A { i - 1 };
    return D;
}
public void update ( D , l , r , x ) {
    D { l } += x;
    D { r + 1 } -= x;
}
public void System.out.printlnArray ( A , D ) {
    for i in range ( 0 , len ( A ) ) :
        if (( i == 0 )) {
            A { i } = D { i };
        }
         else{
            A { i } = D { i } + A { i - 1 };
        }
        System.out.println ( A { i } , end = " " );
    System.out.println ( "" );
}
A = { 10 , 5 , 20 , 40 };
D = initializeDiffArray ( A );
update ( D , 0 , 1 , 10 );
System.out.printlnArray ( A , D );
update ( D , 1 , 3 , 20 );
update ( D , 2 , 2 , 30 );
System.out.printlnArray ( A , D );
