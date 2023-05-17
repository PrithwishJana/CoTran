var char_list = list ( map ( chr , range ( ord ( 'a' ) , ord ( 'z' ) + 1 ) ) );
char_list += list ( map ( chr , range ( ord ( 'A' ) , ord ( 'Z' ) + 1 ) ) );
while (true) {
    var n = int ( input ( ) );
    if (n == 0) {
        break;
    }
     var keys = list ( map ( int , input ( ) . split ( " " ) ) );
    var sentence = input ( );
    for i in range ( len ( sentence ) ) :
        if (sentence { i } . isupper ( )) {
            var j = ord ( sentence { i } ) - ord ( 'A' ) + 26;
        }
         else{
            j = ord ( sentence { i } ) - ord ( 'a' );
        }
        System.out.println ( char_list { j - keys [ i % len ( keys ) } ] , var end = "" );
    System.out.println ( );
}
 