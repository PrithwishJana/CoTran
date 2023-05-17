public void compute ( ) {
    var ans = sum ( x for x in range ( 1000 ) if ( x % 3 == 0 or x % 5 == 0 ) );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 