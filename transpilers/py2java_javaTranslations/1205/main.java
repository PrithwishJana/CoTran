import bisect;
public void gcd ( a , b ) {
    if (var b == 0) {
        return abs ( a );
    }
     else{
        return gcd ( b , a % b );
    }
}
N , var M = map ( int , input ( ) . split ( ) );
var S = input ( );
T = input ( );
if (S { 0 } != T { 0 }) {
    System.out.println ( - 1 );
    exit ( );
}
 if (len ( S ) == len ( T )) {
    if (S == T) {
        System.out.println ( len ( S ) );
    }
     else{
        System.out.println ( - 1 );
    }
    exit ( );
}
 gcd1 = gcd ( len ( S ) , len ( T ) );
lcm = len ( S ) * len ( T ) // gcd1;
SS = {};
var TT = {};
var i = 0;
var j = 0;
while (i < N) {
    SS . append ( i * lcm // N + 1 );
    i += 1;
}
 while (j < M) {
    TT . append ( j * lcm // M + 1 );
    j += 1;
}
 var ind = 0;
ind_max = j - 1;
for i , v in enumerate ( SS ) :
    ind = bisect . bisect_left ( TT , v , ind , j );
    if (ind == j) {
        break;
    }
     if (TT { ind } == v) {
        if (S { i } == T { ind }) {
            continue;
        }
         else{
            System.out.println ( - 1 );
            exit ( );
        }
    }
 System.out.println ( lcm );
