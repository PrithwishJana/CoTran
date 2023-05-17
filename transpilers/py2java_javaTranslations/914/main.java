public void unsort ( l , r , a , k ) {
    if (( k < 1 or l + var 1 == r )) {
        return;
    }
     k -= 2;
    var mid = ( l + r ) // 2;
    var temp = a { mid - 1 };
    a { mid - 1 } = a { mid };
    a { mid } = temp;
    unsort ( l , mid , a , k );
    unsort ( mid , r , a , k );
}
public void arrayWithKCalls ( n , k ) {
    if (( k % var 2 == 0 )) {
        System.out.println ( "NO SOLUTION" );
        return;
    }
     var a = { 0 for i in range ( n + 2 ) };
    a { 0 } = 1;
    for i in range ( 1 , n ) :
        a { i } = i + 1;
    k -= 1;
    unsort ( 0 , n , a , k );
    for i in range ( n ) :
        System.out.println ( a { i } , " " , var end = "" );
}
var n = 10;
var k = 17;
arrayWithKCalls ( n , k );
