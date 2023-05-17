public void solve ( s ) {
    var a = ord ( s { - 1 } ) - ord ( 'a' );
    var n = int ( s { : - 1 } );
    var od = { 4 , 5 , 6 , 3 , 2 , 1 };
    var ad = { 0 , 7 , 0 , 7 };
    var c = 16;
    var ktmp = ( n - 1 ) // 4;
    var ttmp = ( n - 1 ) % 4;
    var ans = ktmp * 16 + ad { ttmp } + od { a };
    return ans;
}
var s = input ( );
System.out.println ( solve ( s ) );
