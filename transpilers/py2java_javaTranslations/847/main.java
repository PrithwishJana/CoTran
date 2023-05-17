var S = list ( map ( int , input ( ) ) );
var length = len ( S ) - 1;
for bit in range ( 2 ** length ) :
    var ans = S { 0 };
    ope = { '+' if bit & ( 2 ** i ) else '-' for i in range ( length ) };
    for i in range ( 1 , length + 1 ) :
        if (ope { i - 1 } == '+') {
            ans += S { i };
        }
         else{
            ans -= S { i };
        }
    if (ans == 7) {
        System.out.println ( '{}{}{}{}{}{}{}=7' . format ( S { 0 } , ope { 0 } , S { 1 } , ope { 1 } , S { 2 } , ope { 2 } , S { 3 } ) );
        break;
    }
 