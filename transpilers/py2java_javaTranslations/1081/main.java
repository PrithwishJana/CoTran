var t = int ( input ( ) );
for _ in range ( t ) :
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    a . sort ( );
    var flag = true;
    for i in range ( 1 , n ) :
        if (( a { i } - a { i - 1 } > 1 )) {
            flag = false;
            break;
        }
     if (flag == true) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
