var D = 360;
var x = { 0 for i in range ( D ) };
var n = int ( input ( ) );
for i in range ( n ) :
    m , d , v , var s = map ( int , input ( ) . split ( ) );
    m -= 1;
    d -= 1;
    var start = 30 * m + d;
    var end = ( start + v - 1 ) % D;
    var h = { false for _ in range ( D ) };
    for j in range ( v ) :
        var y = ( start + j ) % D;
        h { y } = true;
    for j in range ( D ) :
        if (h { j }) {
            x { j } = max ( x { j } , s );
        }
         else{
            var A = abs ( start - j );
            if (A > D // 2) {
                A = D - A;
            }
             var B = abs ( end - j );
            if (B > D // 2) {
                B = D - B;
            }
             x { j } = max ( x { j } , s - min ( A , B ) );
        }
System.out.println ( min ( x ) );
