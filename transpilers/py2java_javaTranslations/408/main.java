public void isVowel ( c ) {
    return ( var c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' );
}
public void encryptString ( s , n , k ) {
    cv = { 0 for i in range ( n ) };
    cc = { 0 for i in range ( n ) };
    if (( isVowel ( s { 0 } ) )) {
        cv { 0 } = 1;
    }
     else{
        cc { 0 } = 1;
    }
    for i in range ( 1 , n ) :
        cv { i } = cv { i - 1 } + isVowel ( s { i } );
        cc { i } = cc { i - 1 } + ( isVowel ( s { i } ) == false );
    var ans = "";
    var prod = 0;
    prod = cc { k - 1 } * cv { k - 1 };
    ans += str ( prod );
    for i in range ( k , len ( s ) ) :
        prod = ( ( cc { i } - cc { i - k } ) * ( cv { i } - cv { i - k } ) );
        ans += str ( prod );
    return ans;
}
if (var __name__ == '__main__') {
    var s = "hello";
    var n = len ( s );
    var k = 2;
    System.out.println ( encryptString ( s , n , k ) );
}
 