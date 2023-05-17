public void isExists ( a , n ) {
    var freq = { i : 0 for i in a };
    var Sum = 0;
    for i in range ( n ) :
        freq { a [ i } ] += 1;
        Sum += a { i };
    if (Sum % var 2 == 0) {
        if (freq { Sum // 2 }) {
            return true;
        }
     }
     return false;
}
var a = { 5 , 1 , 2 , 2 };
var n = len ( a );
if (isExists ( a , n )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
