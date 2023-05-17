public void highestPowerOf2 ( n ) {
    return ( n & ( ~ ( n - 1 ) ) );
}
if (var __name__ == '__main__') {
    var n = 48;
    System.out.println ( highestPowerOf2 ( n ) );
}
 