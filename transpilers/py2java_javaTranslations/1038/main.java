public void minRemove ( a , b , n , m ) {
    var countA = dict ( );
    var countB = dict ( );
    for i in range ( n ) :
        countA { a [ i } ] = countA . get ( a { i } , 0 ) + 1;
    for i in range ( n ) :
        countB { b [ i } ] = countB . get ( b { i } , 0 ) + 1;
    var res = 0;
    for (int x = 0; x < countA.length; x++){
        if (x in countB . keys ( )) {
            res += min ( countA { x } , countB { x } );
        }
    }
     return res;
}
var a = { 1 , 2 , 3 , 4 };
var b = { 2 , 3 , 4 , 5 , 8 };
var n = len ( a );
var m = len ( b );
System.out.println ( minRemove ( a , b , n , m ) );
