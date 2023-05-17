import sys;
var input = sys . stdin . readline;
var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var d = { 0 for _ in range ( 100007 ) };
var ans = 0;
for (int i = 0; i < a.length; i++){
    for j in range ( 2 , i + 1 ) :
        if (j * j > i) {
            break;
        }
         if (i % j == 0) {
            d { i } = max ( d { i } , d { i // j } + 1 , d { j } + 1 );
        }
     d { i } = max ( d { i } , 1 );
    for j in range ( 2 , i + 1 ) :
        if (j * j > i) {
            break;
        }
         if (i % j == 0) {
            d { i // j } = d { i };
            d { j } = d { i };
        }
     ans = max ( ans , d { i } );
}
System.out.println ( ans );
