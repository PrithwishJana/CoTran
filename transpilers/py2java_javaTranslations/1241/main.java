public void check_prime ( n ) {
    if (( n <= 1 )) {
        return false;
    }
     if (( n <= 3 )) {
        return true;
    }
     if (( n % var 2 == 0 or n % 3 == 0 )) {
        return false;
    }
     for i in range ( 5 , n + 1 , 6 ) :
        if (( n % var i == 0 or n % ( i + 2 ) == 0 )) {
            return false;
        }
     return true;
}
public void countPrimeFrequent ( s ) {
    var count = 0;
    var mp = {};
    for i in range ( 0 , len ( s ) ) :
        mp . setdefault ( s { i } , 0 );
        mp { s [ i } ] += 1;
    for i in mp . keys ( ) :
        if (( check_prime ( mp { i } ) )) {
            count += 1;
        }
     return count ;;
}
var s = "geeksforgeeks";
System.out.println ( countPrimeFrequent ( s ) );
