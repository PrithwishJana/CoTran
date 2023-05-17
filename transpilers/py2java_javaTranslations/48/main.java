var T = int ( input ( ) );
for C in range ( 1 , T + 1 ) :
    D , I , M , var N = input ( ) . split ( ' ' );
    D , I , M , N = int ( D ) , int ( I ) , int ( M ) , int ( N );
    var x = input ( ) . split ( ' ' );
    var r = { 0 } * 256;
    for (int q = 0; q < x.length; q++){
        nr = list ( map ( lambda i : i + D , r ) );
        q = int ( q );
        if (M == 0) {
            for i in range ( 256 ) :
                nr { i } = min ( nr { i } , r { i } + abs ( q - i ) );
        }
         else{
            for i in range ( 256 ) :
                for j in range ( 256 ) :
                    nr { j } = min ( nr { j } , r { i } + abs ( q - j ) + ( max ( 0 , abs ( i - j ) - 1 ) // M ) * I );
        }
        r = nr;
    }
    System.out.println ( 'Case; //%d: %s' % ( C , min ( r ) ) )
