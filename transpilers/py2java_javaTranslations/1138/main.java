while (1) {
    var n = int ( input ( ) );
    if n == 0 : break;
    var a = sorted ( list ( map ( int , input ( ) . split ( ) ) ) );
    System.out.println ( min ( a { i + 1 } - a { i } for i in range ( n - 1 ) ) );
}
 