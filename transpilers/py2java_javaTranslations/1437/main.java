public void factorial ( n ) {
    if (( n <= 1 )) {
        return 1 ;;
    }
     return n * factorial ( n - 1 ) ;;
}
public void nCr ( n , r ) {
    return ( factorial ( n ) / ( factorial ( n - r ) * factorial ( r ) ) ) ;;
}
public void NumberOfWays ( n , x , y ) {
    return ( nCr ( 2 * n - x - y , n - x ) * factorial ( n ) * factorial ( n ) ) ;;
}
n , x , var y = 5 , 4 , 2 ;;
System.out.println ( int ( NumberOfWays ( n , x , y ) ) ) ;;
