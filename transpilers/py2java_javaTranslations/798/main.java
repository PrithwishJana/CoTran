public void circlearea ( a , b ) {
    if (( a < 0 or b < 0 )) {
        return - 1;
    }
     var A = ( ( 3.14 * pow ( a , 2 ) * pow ( b , 2 ) ) / ( 4 * ( pow ( a , 2 ) + pow ( b , 2 ) ) ) );
    return A;
}
if (var __name__ == "__main__") {
    var a = 8;
    var b = 10;
    System.out.println ( circlearea ( a , b ) );
}
 