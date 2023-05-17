for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    arr = list ( map ( int , input ( ) . split ( ) ) );
    k = min ( arr );
    if (n == 1) {
        System.out.println ( 0 );
    }
     else{
        var res = 0;
        for (int i = 0; i < arr.length; i++){
            res += ( i - k );
        }
        System.out.println ( res );
    }
