var MAXN = 1000001;
var spf = { i for i in range ( MAXN ) };
var hash1 = { 0 for i in range ( MAXN ) };
public void sieve ( ) {
    for i in range ( 4 , MAXN , 2 ) :
        spf { i } = 2;
    for i in range ( 3 , MAXN ) :
        if (i * i < MAXN) {
            break;
        }
         if (( spf { i } == i )) {
            for j in range ( i * i , MAXN , i ) :
                if (( spf { j } == j )) {
                    spf { j } = i;
                }
         }
 }
public void getFactorization ( x ) {
    while (( x != 1 )) {
        var temp = spf { x };
        if (( x % temp == 0 )) {
            hash1 { spf [ x } ] += 1;
            x = x // spf { x };
        }
         while (( x % temp == 0 )) {
            x = x // temp;
        }
     }
 }
public void check ( x ) {
    while (( x != 1 )) {
        temp = spf { x };
        if (( x % temp == 0 and hash1 { temp } > 1 )) {
            return false;
        }
         while (( x % temp == 0 )) {
            var x = x // temp;
        }
     }
     return true;
}
public void hasValidNum ( arr , n ) {
    sieve ( );
    for i in range ( n ) :
        getFactorization ( arr { i } );
    for i in range ( n ) :
        if (( check ( arr { i } ) )) {
            return true;
        }
     return false;
}
var arr = { 2 , 8 , 4 , 10 , 6 , 7 };
var n = len ( arr );
if (( hasValidNum ( arr , n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
