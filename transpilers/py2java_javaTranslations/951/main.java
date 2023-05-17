n , var wmax = map ( int , input ( ) . split ( ) );
var U = {};
for _ in range ( n ) :
    v , var w = map ( int , input ( ) . split ( ) );
    var u = v / w;
    U . append ( { - u , v , w } );
U . sort ( );
var remains = wmax;
var i = 0;
var ans = 0;
while (true) {
    try{
        if (remains > U { i } { 2 }) {
            remains -= U { i } { 2 };
            ans += U { i } { 1 };
            i += 1;
        }
         else{
            ans += U { i } { 1 } * remains / U { i } { 2 };
            break;
        }
    }
    except :
        break;
}
 System.out.println ( ans );
