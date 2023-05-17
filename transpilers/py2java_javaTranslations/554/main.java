public void countSetBits ( n ) {
    var count = 0 ;;
    while (( n )) {
        n &= ( n - 1 ) ;;
        count += 1;
    }
     return count ;;
}
public void pairs ( arr , n , k ) {
    count = 0 ;;
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            var sum = countSetBits ( arr { i } ) + countSetBits ( arr { j } ) ;;
            if (( sum == k )) {
                count += 1 ;;
            }
     return count ;;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 4 , 5 } ;;
    var n = len ( arr ) ;;
    var k = 4 ;;
    System.out.println ( pairs ( arr , n , k ) ) ;;
}
 