for p in range ( int ( input ( ) ) ) :
    n , var k = list ( map ( int , input ( ) . split ( ) ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    if (n % 2) {
        x , var y = n // 2 , n // 2 + 1;
    }
     else{
        x , y = n // 2 - 1 , n // 2 + 1;
    }
    if (var n == 2) {
        var s = 0;
        for i in range ( 0 , n * k , 2 ) :
            s += a { i };
        System.out.println ( s );
    }
     else{
        d , s = x * k , 0;
        while (d < ( n * k )) {
            s += a { d };
            d += y;
        }
         System.out.println ( s );
    }
