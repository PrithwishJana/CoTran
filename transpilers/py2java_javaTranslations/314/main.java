public void Loss ( SP , P ) {
    var loss = 0;
    loss = ( ( 2 * P * P * SP ) / ( 100 * 100 - P * P ) );
    System.out.println ( "var Loss =" , "{:.3f}" . format ( loss ) );
}
if (var __name__ == "__main__") {
    SP , var P = 2400 , 30;
    Loss ( SP , P );
}
 