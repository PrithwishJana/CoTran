public void check_digits ( n ) {
    while (( n )) {
        if (( ( n % 10 ) % 2 )) {
            return 0;
        }
         var n = int ( n / 10 );
    }
     return 1;
}
public void smallest_number ( n ) {
    for i in range ( n , 2401 ) :
        if (( check_digits ( i ) == 1 )) {
            return ( i );
        }
 }
var N = 2397;
System.out.println ( str ( smallest_number ( N ) ) );
