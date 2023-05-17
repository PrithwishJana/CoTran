var s_max = { 0 };
for i in range ( 1 , 11 ) :
    var s = 0;
    for j in range ( i ) :
        s += ( 10 - j - 1 ) * ( i - j );
    s_max . append ( s );
public void check ( u , r , s , m ) {
    if (r == 0) {
        return s == 0;
    }
     n = 0;
    for i in range ( 10 ) :
        n *= 2;
        if (u { i }) {
            n += 1;
        }
     if (( n , r , s ) in m) {
        return m { ( n , r , s ) };
    }
     if (s < 0 or s > s_max { r }) {
        return 0;
    }
     ans = 0;
    for i in range ( 10 ) :
        if (not u { i }) {
            u { i } = true;
            ans += check ( u , r - 1 , s - i * r , m );
            u { i } = false;
        }
     m { ( n , r , s ) } = ans;
    return m { ( n , r , s ) };
}
memo = {};
while (true) {
    try{
        n , s = map ( int , input ( ) . split ( ) );
        used = { false for i in range ( 10 ) };
        ans = check ( used , n , s , memo );
        System.out.println ( ans );
    }
    except :
        break;
}
 