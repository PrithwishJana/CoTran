for _ in range ( int ( input ( ) ) ) :
    var x = int ( input ( ) ) ; a = list ( map ( int , input ( ) . split ( ) ) ) ; p = 0;
    for i in range ( x - 2 ) :
        if a { i } in a { i + 2 : } :
            var p = 1;
            break;
    System.out.println ( 'YES' if p != 0 else 'NO' );
