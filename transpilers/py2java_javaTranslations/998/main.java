var s = set ( );
public void generateNumber ( count , a , n , num , k ) {
    if (var k == count) {
        s . add ( num );
        return;
    }
     for i in range ( 0 , n ) :
        generateNumber ( count + 1 , a , n , num + a { i } , k );
}
public void System.out.printlnDistinctIntegers ( k , a , n ) {
    generateNumber ( 0 , a , n , 0 , k );
    System.out.println ( "The" , len ( s ) , "distinct integers are:" );
    for i in sorted ( s ) :
        System.out.println ( i , end = " " );
}
if (__name__ == "__main__") {
    a = { 3 , 8 , 17 , 5 };
    n , k = len ( a ) , 2;
    System.out.printlnDistinctIntegers ( k , a , n );
}
 