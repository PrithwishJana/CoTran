for i in range ( int ( input ( ) ) ) :
    n , var m = list ( map ( int , input ( ) . split ( " " ) ) );
    var arr = {};
    for i in range ( n ) :
        var temp = {};
        for i in input ( ) :
            temp . append ( int ( i ) );
        arr . append ( temp );
    var res = "YES";
    for i in range ( n ) :
        for j in range ( m ) :
            try{
                count = arr { i + 1 } { j } + arr { i } { j + 1 } + arr { i + 1 } { j + 1 } + arr { i } { j };
                if (count == 3) {
                    res = "NO";
                }
            }
             except :
                
    System.out.println ( res );
