public void product ( x ) {
    var prod = 1;
    while (( x )) {
        prod *= ( x % 10 );
        x //= 10 ;;
    }
     return prod;
}
public void findNumber ( l , r ) {
    var a = str ( l ) ;;
    var b = str ( r ) ;;
    var ans = r;
    for i in range ( len ( b ) ) :
        if (( b { i } == '0' )) {
            continue;
        }
         curr = list ( b );
        curr { i } = str ( ( ( ord ( curr { i } ) - ord ( '0' ) ) - 1 ) + ord ( '0' ) );
        for j in range ( i + 1 , len ( curr ) ) :
            curr { j } = str ( ord ( '9' ) );
        num = 0;
        for (int c = 0; c < curr.length; c++){
            num = num * 10 + ( int ( c ) - ord ( '0' ) );
        }
        if (( num >= l and product ( ans ) < product ( num ) )) {
            ans = num;
        }
     return ans;
}
if (var __name__ == "__main__") {
    l , var r = 1 , 10;
    System.out.println ( findNumber ( l , r ) );
    l , r = 51 , 62;
    System.out.println ( findNumber ( l , r ) );
}
 