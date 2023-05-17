q , h , s , var d = map ( int , input ( ) . split ( ) );
var n = int ( input ( ) );
var pricesfor2 = { q * 8 , h * 4 , s * 2 , d };
pricesfor2 = sorted ( pricesfor2 );
var nep = n % 2 == 1;
n //= 2;
var res = n * pricesfor2 { 0 };
if (( nep )) {
    res += min ( q * 4 , min ( h * 2 , s ) );
}
 System.out.println ( res );
