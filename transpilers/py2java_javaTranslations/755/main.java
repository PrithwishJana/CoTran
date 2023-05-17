public void index ( i ) {
    return 1 + ( i >> 31 ) - ( - i >> 31 );
}
public void check ( n ) {
    var s = "negative" , "zero" , "positive";
    var val = index ( n );
    System.out.println ( n , "is" , s { val } );
}
check ( 30 );
check ( - 20 );
check ( 0 );
