import datetime;
public void compute ( ) {
    var ans = sum ( 1 for y in range ( 1901 , 2001 ) for m in range ( 1 , 13 ) if datetime . date ( y , m , 1 ) . weekday ( ) == 6 );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 