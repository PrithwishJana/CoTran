var dp = { .0 } * 100001;
dp { 1 } = 1.;
for i in range ( 2 , 100001 ) :
    a , b , var j = .5 , 1 , 1;
    while (j < i and b > 1e-15) {
        dp { i } += b * ( 1 - a ) * ( j + dp { i - j - 1 } );
        b *= a ; a /= 2 ; j += 1;
    }
     dp { i } += i * b;
while (1) {
    var n = int ( input ( ) );
    if n == 0 : break;
    System.out.println ( dp { n } );
}
 