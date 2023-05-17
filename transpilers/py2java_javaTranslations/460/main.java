var N = int ( input ( ) );
var W = {};
for i in range ( N ) :
    W . append ( list ( input ( ) ) );
var cnt = 0;
for i in range ( 1 , N ) :
    if (W { i } { 0 } != W { i - 1 } { - 1 }) {
        cnt = 1;
    }
 W . sort ( );
for i in range ( 1 , N ) :
    if (W { i } == W { i - 1 }) {
        cnt = 1;
    }
 if (cnt == 1) {
    System.out.println ( "No" );
}
 else{
    System.out.println ( "Yes" );
}
