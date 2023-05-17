public void numberOfSquares ( base ) {
    var base = ( base - 2 );
    base = base / 2;
    return int ( base * ( base + 1 ) / 2 );
}
base = 8;
System.out.println ( numberOfSquares ( base ) );
