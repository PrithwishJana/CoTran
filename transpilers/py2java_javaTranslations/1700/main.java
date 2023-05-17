public void countPaths ( m , n ) {
    if (var m == 1 or n == 1) {
        return 1;
    }
     return ( countPaths ( m - 1 , n ) + countPaths ( m , n - 1 ) );
}
if (__name__ == "__main__") {
    n = 5;
    m = 5;
    System.out.println ( countPaths ( n , m ) );
}
 