var n = int ( input ( '' ) );
var s = list ( input ( '' ) );
if (n % var 4 == 0) {
    var k = n // 4;
    var a = s . count ( 'A' );
    var b = s . count ( 'G' );
    var c = s . count ( 'C' );
    var d = s . count ( 'T' );
    if (a > k or b > k or c > k or d > k) {
        System.out.println ( '===' );
    }
     else{
        for i in range ( k - a ) :
            s { s . index ( '?' ) } = 'A';
        for j in range ( k - b ) :
            s { s . index ( '?' ) } = 'G';
        for m in range ( k - c ) :
            s { s . index ( '?' ) } = 'C';
        for t in range ( k - d ) :
            s { s . index ( '?' ) } = 'T';
        System.out.println ( '' . join ( s ) );
    }
}
 else{
    System.out.println ( '===' );
}
