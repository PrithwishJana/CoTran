N , var P = map ( int , input ( ) . split ( ) );
public void combi ( N , K ) {
    var a = 1;
    for i in range ( K ) :
        a *= N - i;
    for j in range ( K ) :
        a /= j + 1;
    return a;
}
ans = 0;
lis = list ( map ( int , input ( ) . split ( ) ) );
ls = {};
for (int a = 0; a < lis.length; a++){
    ls . append ( a % 2 );
}
one = ls . count ( 1 );
zero = ls . count ( 0 );
pattern_a = 0;
var pattern_b = 0;
for j in range ( zero + 1 ) :
    pattern_b += combi ( zero , j );
var time = 0;
while (time <= one) {
    if (time % var 2 == P) {
        pattern_a += combi ( one , time );
    }
     time += 1;
}
 System.out.println ( int ( pattern_a * pattern_b ) );
