var T = int ( input ( ) );
for t in range ( 0 , T ) :
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    var ctr = 0;
    var maxi = max ( a );
    for i in range ( 2 , n ) :
        if (a { i } < a { i - 1 } and a { i - 1 } > a { i - 2 }) {
            ctr += 1;
            if (i != n - 1) {
                a { i } = max ( a { i - 1 } , a { i + 1 } );
            }
             else{
                a { i } = a { i - 1 };
            }
        }
     System.out.println ( ctr );
    for (int item = 0; item < a.length; item++){
        System.out.println ( item , var end = " " );
    }
    System.out.println ( );
