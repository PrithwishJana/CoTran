for t in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var p = list ( map ( int , input ( ) . split ( ) ) );
    var result = 0;
    var c = 0;
    while (c < n - 1) {
        if (p { c } > p { c + 1 }) {
            result += 1;
            c += 1;
        }
         c += 1;
    }
     System.out.println ( result );
