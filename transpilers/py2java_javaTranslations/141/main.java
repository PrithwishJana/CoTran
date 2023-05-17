var t = int ( input ( ) );
for i in range ( t ) :
    var x = int ( input ( ) );
    if (x // 1000 > 0) {
        System.out.println ( 10 * ( x % 10 - 1 ) + 10 );
    }
     else if (x // 100 > 0){
        System.out.println ( 10 * ( x % 10 - 1 ) + 6 );
    }
    else if (x // 10 > 0){
        System.out.println ( 10 * ( x % 10 - 1 ) + 3 );
    }
    else : System.out.println ( 10 * ( x % 10 - 1 ) + 1 );
