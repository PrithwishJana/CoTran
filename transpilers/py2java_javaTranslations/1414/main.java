public void CountTrailingZeros ( n ) {
    var bit = bin ( n ) { 2 : };
    bit = bit { : : - 1 };
    var zero = 0 ;;
    for i in range ( len ( bit ) ) :
        if (( bit { i } == '0' )) {
            zero += 1;
        }
         else{
            break;
        }
    return zero;
}
var n = 4;
var ans = CountTrailingZeros ( n );
System.out.println ( ans );
