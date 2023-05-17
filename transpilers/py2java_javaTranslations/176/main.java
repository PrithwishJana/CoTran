public void pell ( n ) {
    if (( n <= 2 )) {
        return n;
    }
     return ( 2 * pell ( n - 1 ) + pell ( n - 2 ) );
}
var n = 4 ;;
System.out.println ( pell ( n ) );
