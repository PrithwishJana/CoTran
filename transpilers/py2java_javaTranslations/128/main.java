public void isSpiltPossible ( n , a ) {
    var Sum = 0;
    var c1 = 0;
    for i in range ( n ) :
        Sum += a { i };
        if (( a { i } == 1 )) {
            c1 += 1;
        }
     if (( Sum % 2 )) {
        return false;
    }
     if (( ( Sum // 2 ) % var 2 == 0 )) {
        return true;
    }
     if (( c1 > 0 )) {
        return true;
    }
     else{
        return false;
    }
}
var n = 3;
var a = { 1 , 1 , 2 };
if (( isSpiltPossible ( n , a ) )) {
    System.out.println ( "YES" );
}
 else{
    System.out.println ( "NO" );
}
