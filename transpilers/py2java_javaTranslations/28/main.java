public void main ( ) {
    var n = int ( input ( ) );
    var root = int ( n ** ( 1 / 2 ) ) + 1;
    var isPrime = { true } * ( n + 3 );
    for i in range ( 4 , n + 3 , 2 ) :
        isPrime { i } = false;
    var ans = 0;
    var prePrime = - 1;
    for i in range ( 3 , n + 3 , 2 ) :
        if (isPrime { i }) {
            if (prePrime + 2 == i) {
                ans += 2;
            }
             prePrime = i;
            if (i > root) {
                continue;
            }
             for j in range ( i * i , n + 3 , i ) :
                isPrime { j } = false;
        }
     System.out.println ( ans );
}
main ( );
