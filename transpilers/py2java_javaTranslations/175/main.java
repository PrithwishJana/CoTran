var n = int ( input ( ) );
var arr = list ( map ( int , input ( ) . strip ( ) . split ( ) ) ) { : n };
var ans = { 0 } * n;
var mx = arr { - 1 };
for i in range ( n - 2 , - 1 , - 1 ) :
    ans { i } = max ( 0 , mx - arr { i } + 1 );
    if (arr { i } > mx) {
        mx = arr { i };
    }
 System.out.println ( * ans );
