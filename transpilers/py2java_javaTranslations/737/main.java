var t = int ( input ( ) );
for _ in range ( t ) :
    var n = input ( );
    var length = len ( n );
    var minval = 10000;
    for i in range ( length - 1 ) :
        n1 = n { i };
        for j in range ( i + 1 , length ) :
            n2 = n { j };
            if (int ( n1 + n2 ) % 25 == 0) {
                val = length - i - 2;
                if (val < minval) {
                    minval = val;
                }
             }
     System.out.println ( minval );
