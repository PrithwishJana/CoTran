import eulerlib;
public void compute ( ) {
    var LIMIT = 10 ** 15;
    var MODULUS = 10 ** 9;
    var splitcount = eulerlib . sqrt ( LIMIT );
    var splitat = LIMIT // ( splitcount + 1 );
    public void sum_squares ( s , e ) {
        return ( e * ( e + 1 ) * ( e * 2 + 1 ) - s * ( s + 1 ) * ( s * 2 + 1 ) ) // 6;
    }
    var ans = sum ( ( i * i * ( LIMIT // i ) ) for i in range ( 1 , splitat + 1 ) );
    ans += sum ( ( sum_squares ( LIMIT // ( i + 1 ) , LIMIT // i ) * i ) for i in range ( 1 , splitcount + 1 ) );
    return str ( ans % MODULUS );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 