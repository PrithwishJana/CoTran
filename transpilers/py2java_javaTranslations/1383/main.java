public void countSetBits ( n ) {
    var count = 0;
    while (( n )) {
        count += n & 1;
        n >>= 1;
    }
     return count;
}
public void totalPairs ( s1 , s2 ) {
    count = 0 ;;
    var arr1 = { 0 } * 7 ; arr2 = { 0 } * 7 ;;
    for i in range ( len ( s1 ) ) :
        var set_bits = countSetBits ( ord ( s1 { i } ) );
        arr1 { set_bits } += 1 ;;
    for i in range ( len ( s2 ) ) :
        set_bits = countSetBits ( ord ( s2 { i } ) ) ;;
        arr2 { set_bits } += 1 ;;
    for i in range ( 1 , 7 ) :
        count += ( arr1 { i } * arr2 { i } ) ;;
    return count ;;
}
if (var __name__ == "__main__") {
    var s1 = "geeks" ;;
    var s2 = "forgeeks" ;;
    System.out.println ( totalPairs ( s1 , s2 ) ) ;;
}
 