public void negProdSubArr ( arr , n ) {
    var positive = 1;
    var negative = 0;
    for i in range ( n ) :
        if (( arr { i } > 0 )) {
            arr { i } = 1;
        }
         else{
            arr { i } = - 1;
        }
        if (( i > 0 )) {
            arr { i } *= arr { i - 1 };
        }
         if (( arr { i } == 1 )) {
            positive += 1;
        }
         else{
            negative += 1;
        }
    return ( positive * negative );
}
public void posProdSubArr ( arr , n ) {
    var total = ( n * ( n + 1 ) ) / 2 ;;
    var cntNeg = negProdSubArr ( arr , n ) ;;
    return ( total - cntNeg ) ;;
}
var arr = { 5 , - 4 , - 3 , 2 , - 5 };
var n = len ( arr );
System.out.println ( int ( posProdSubArr ( arr , n ) ) );
