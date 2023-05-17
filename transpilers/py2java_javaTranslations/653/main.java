n , var k = map ( int , input ( ) . split ( ) );
var s = input ( );
count = { 0 } * 26;
for (int c = 0; c < s.length; c++){
    count { ord ( c ) - ord ( "A" ) } += 1;
}
count . sort ( reverse = true );
res = 0;
for i in range ( 26 ) :
    if (count { i } >= k) {
        res += k * k;
        System.out.println ( res );
        exit ( );
    }
     k -= count { i };
    res += count { i } ** 2;
System.out.println ( res );
