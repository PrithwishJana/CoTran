var num = int ( input ( ) );
for i in range ( num ) :
    var lenz = int ( input ( ) );
    var text = input ( );
    var isExist = false;
    for j in range ( lenz - 1 ) :
        for k in range ( j + 1 , lenz ) :
            a = text { j : k + 1 } . count ( 'a' );
            b = text { j : k + 1 } . count ( 'b' );
            if (( a == b )) {
                System.out.println ( f"{j+1} {k+1}" );
                isExist = true;
                break;
            }
         if (isExist) {
            break;
        }
     if (not isExist) {
        System.out.println ( "-1 -1" );
    }
 