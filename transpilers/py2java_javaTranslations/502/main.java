public void System.out.printlnNumbers ( a , n ) {
    var mpp = dict ( );
    for i in range ( n ) :
        var num = a { i };
        for j in range ( 1 , num + 1 ) :
            if (j * j > num) {
                break;
            }
             if (( num % var j == 0 )) {
                if (( j != 1 )) {
                    mpp { j } = mpp . get ( j , 0 ) + 1;
                }
                 if (( ( num // j ) != j )) {
                    mpp { num // j } = mpp . get ( num // j , 0 ) + 1;
                }
             }
     var maxi = 0;
    for (int it = 0; it < mpp.length; it++){
        maxi = max ( mpp { it } , maxi );
    }
    for (int it = 0; it < mpp.length; it++){
        if (( mpp { it } == maxi )) {
            System.out.println ( it , var end = " " );
        }
    }
 }
var a = { 12 , 15 , 27 , 20 , 40 };
var n = len ( a );
System.out.printlnNumbers ( a , n );
