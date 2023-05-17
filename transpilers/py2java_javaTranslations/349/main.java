var N = int ( input ( ) );
var K = int ( input ( ) );
var X = int ( input ( ) );
var Y = int ( input ( ) );
if (N <= K) {
    System.out.println ( int ( N * X ) );
}
 else{
    System.out.println ( int ( K * X + ( N - K ) * Y ) );
}
