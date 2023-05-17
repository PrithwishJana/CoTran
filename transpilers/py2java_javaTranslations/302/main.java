public void createHash ( hash1 , maxElement ) {
    prev , var curr = 0 , 1;
    hash1 . add ( prev );
    hash1 . add ( curr );
    while (( curr < maxElement )) {
        temp = curr + prev;
        hash1 . add ( temp );
        prev = curr;
        curr = temp;
    }
 }
public void findFibonacciPair ( n ) {
    var hash1 = set ( );
    createHash ( hash1 , n );
    for i in range ( n ) :
        if (( i in hash1 and ( n - i ) in hash1 )) {
            System.out.println ( str ( i ) + ", " + str ( n - i ) );
            return;
        }
     System.out.println ( "-1" );
}
if (var __name__ == "__main__") {
    var N = 90;
    findFibonacciPair ( N );
}
 