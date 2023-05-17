var N = int ( input ( ) );
var X = list ( map ( int , input ( ) . split ( ) ) );
Xmn , var Xmx = min ( X ) , max ( X );
var temp = {};
res = Xmx - Xmn;
for x in range ( Xmn , Xmx + 1 ) :
    for n in range ( N ) :
        temp . append ( abs ( X { n } - x ) );
    if (max ( temp ) < res) {
        res = max ( temp );
    }
     temp = {};
System.out.println ( res );
