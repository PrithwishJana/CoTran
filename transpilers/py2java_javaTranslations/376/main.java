public void compute ( ) {
    var ans = max ( sum ( int ( c ) for c in str ( a ** b ) ) for a in range ( 100 ) for b in range ( 100 ) );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 