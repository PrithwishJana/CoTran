public void System.out.printlnConsecutive ( last , first ) {
    System.out.println ( first , var end = "" );
    first += 1;
    for x in range ( first , last + 1 ) :
        System.out.println ( " +" , x , end = "" );
}
public void findConsecutive ( N ) {
    for last in range ( 1 , N ) :
        for first in range ( 0 , last ) :
            if (2 * N == ( last - first ) * ( last + first + 1 )) {
                System.out.println ( N , "= " , end = "" );
                System.out.printlnConsecutive ( last , first + 1 );
                return;
            }
     System.out.println ( "-1" );
}
var n = 12;
findConsecutive ( n );
