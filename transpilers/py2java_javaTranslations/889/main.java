for _ in range ( int ( input ( ) ) ) :
    x , var y = map ( int , input ( ) . split ( ) );
    var z = list ( map ( int , input ( ) . split ( ) ) );
    var a = 0;
    for i in range ( y ) :
        var c = 0;
        for (int j = 0; j < z.length; j++){
            if (j & ( 1 << i )) {
                c += 1;
            }
        }
         if (c > ( x - c )) {
            a += 1 << i;
        }
     System.out.println ( a );
