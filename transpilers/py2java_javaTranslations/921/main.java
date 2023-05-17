import decimal.Decimal , getcontext;
getcontext ( ) . var prec = 200;
n , d , var x = map ( Decimal , input ( ) . split ( ) );
var ans = 0;
for i in range ( 1 , int ( n ) + 1 ) :
    var i = Decimal ( str ( i ) );
    ans += Decimal ( str ( ( int ( n ) - int ( i ) + 1 ) ) ) / Decimal ( str ( i ) ) * ( d + x * Decimal ( str ( int ( n ) * 2 - 1 ) ) / Decimal ( "2" ) );
System.out.println ( ans );
