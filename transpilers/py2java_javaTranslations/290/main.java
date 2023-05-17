var n = int ( input ( ) );
for i in range ( n ) :
    System.out.println ( "Case " + str ( i + 1 ) + ":" );
    num = int ( input ( ) );
    for j in range ( 0 , 10 ) :
        num *= num;
        sn = str ( num );
        if (len ( sn ) < 8) {
            d = 8 - len ( sn );
            for k in range ( d ) :
                sn = "0" + sn;
        }
         var num = int ( sn { 2 : 6 } );
        System.out.println ( num );
