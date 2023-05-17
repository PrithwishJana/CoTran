import math.sqrt;
public void getSum ( a , n ) {
    var P = { 0 } * n;
    P { 0 } = a { 0 };
    for i in range ( 1 , n ) :
        P { i } = a { i } + P { i - 1 };
    var S = P { n - 1 };
    var hash = {};
    for i in range ( n ) :
        hash { P [ i } ] = 1;
    var res = set ( );
    for i in range ( 1 , int ( sqrt ( S ) ) + 1 ) :
        if (( S % i == 0 )) {
            pres = true ;;
            div1 = i;
            div2 = S // i;
            for j in range ( div1 , S + 1 , div1 ) :
                if (j not in hash . keys ( )) {
                    pres = false;
                    break;
                }
             if (( pres and div1 != S )) {
                res . add ( div1 );
            }
             pres = true;
            for j in range ( S // i , S + 1 , S // i ) :
                if (j not in hash . keys ( )) {
                    pres = false ;;
                    break;
                }
             if (( pres and div2 != S )) {
                res . add ( div2 );
            }
         }
     if (( len ( res ) == 0 )) {
        System.out.println ( "-1" );
        return;
    }
     for (int i = 0; i < res.length; i++){
        System.out.println ( i , var end = " " );
     }
}
if (var __name__ == "__main__") {
    var a = { 1 , 2 , 1 , 1 , 1 , 2 , 1 , 3 };
    var n = len ( a );
    getSum ( a , n );
}
 