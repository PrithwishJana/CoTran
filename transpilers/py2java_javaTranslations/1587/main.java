var MAX = 100000;
public void System.out.printlns ( g1 , a , g2 , b ) {
    for i in range ( a ) :
        System.out.println ( g1 { i } , var end = " " );
    System.out.println ( "and " , end = "" );
    for i in range ( b ) :
        System.out.println ( g2 { i } , end = " " );
    System.out.println ( "\n" , end = "" );
}
public void checksum ( g1 , a , g2 , b ) {
    var x = 0;
    for i in range ( 0 , a , 1 ) :
        x += g1 { i };
    for i in range ( b ) :
        x -= g2 { i };
    return ( x == 0 );
}
public void formgroups ( arr , x , g1 , a , g2 , b , n ) {
    if (( x == n )) {
        if (( checksum ( g1 , a , g2 , b ) )) {
            System.out.printlns ( g1 , a , g2 , b );
        }
         return;
    }
     g1 { a } = arr { x };
    formgroups ( arr , x + 1 , g1 , a + 1 , g2 , b , n );
    g2 { b } = arr { x };
    formgroups ( arr , x + 1 , g1 , a , g2 , b + 1 , n );
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 3 , 9 , 4 , 5 };
    var n = len ( arr );
    var g1 = { 0 for i in range ( MAX ) };
    var g2 = { 0 for i in range ( MAX ) };
    formgroups ( arr , 0 , g1 , 0 , g2 , 0 , n );
}
 