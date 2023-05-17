n , var m = map ( int , input ( ) . strip ( ) . split ( ) );
var out = { 0 for _ in range ( n ) };
var comp = { i + 2 for i in range ( n ) };
for _ in range ( m ) :
    l , r , var x = map ( int , input ( ) . strip ( ) . split ( ) );
    var t = l;
    while (t <= r) {
        next_val = comp { t - 1 };
        if (out { t - 1 } == 0 and t != x) {
            out { t - 1 } = x;
        }
         comp { t - 1 } = r + 1 if t >= x else x;
        t = next_val;
    }
 System.out.println ( * out );
