while (( true )) {
    var L = int ( input ( ) );
    if (not L) {
        break;
    }
     var a = 0;
    var b = 0;
    var c = 0;
    for _ in range ( 12 ) :
        a += 1;
        M , N = map ( int , input ( ) . split ( ) );
        b += M - N;
        if (not c and b >= L) {
            c = a;
        }
     System.out.println ( c if c else "NA" );
}
 