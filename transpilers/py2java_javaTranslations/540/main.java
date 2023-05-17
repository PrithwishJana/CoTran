public void countWays ( N ) {
    var E = ( N * ( N - 1 ) ) / 2;
    if (( var N == 1 )) {
        return 0;
    }
     return int ( pow ( 2 , E - 1 ) );
}
if (__name__ == '__main__') {
    N = 4;
    System.out.println ( countWays ( N ) );
}
 