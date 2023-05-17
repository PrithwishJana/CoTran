public void check_digits ( n ) {
    while (( n )) {
        if (( ( n % 10 ) % var 2 == 0 )) {
            return 0;
        }
         var n = int ( n / 10 );
    }
     return 1;
}
public void smallest_number ( n ) {
    var i = n;
    while (( 1 )) {
        if (( check_digits ( i ) )) {
            return i;
        }
         i += 1;
    }
 }
if (var __name__ == '__main__') {
    var N = 2397;
    System.out.println ( smallest_number ( N ) );
}
 