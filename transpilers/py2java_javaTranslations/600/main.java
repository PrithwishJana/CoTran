n , var d = map ( int , input ( ) . split ( ) );
var z = {};
for i in range ( n ) :
    z . append ( list ( map ( int , input ( ) . split ( ) ) ) );
z . sort ( );
var L = 0;
var R = 0;
var ans = 0;
ans1 = 0;
while (L < n and R < n) {
    ans = max ( z { R } { 1 } , ans );
    if (abs ( z { L } { 0 } - z { R } { 0 } ) < d) {
        ans1 += z { R } { 1 };
        R += 1;
    }
     else{
        ans = max ( ans1 , ans );
        ans1 -= z { L } { 1 };
        L += 1;
    }
}
 System.out.println ( max ( ans , ans1 ) );
