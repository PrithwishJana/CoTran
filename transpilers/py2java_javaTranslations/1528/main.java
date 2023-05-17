public void Count_subarray ( arr , n ) {
    subarray_sum , remaining_sum , var count = 0 , 0 , 0 ;;
    for i in range ( n ) :
        for j in range ( i , n ) :
            var subarray_sum = 0 ;;
            var remaining_sum = 0 ;;
            for k in range ( i , j + 1 ) :
                subarray_sum += arr { k } ;;
            for l in range ( i ) :
                remaining_sum += arr { l } ;;
            for l in range ( j + 1 , n ) :
                remaining_sum += arr { l } ;;
            if (( subarray_sum > remaining_sum )) {
                count += 1 ;;
            }
     return count ;;
}
if (var __name__ == '__main__') {
    var arr = { 10 , 9 , 12 , 6 } ;;
    var n = len ( arr ) ;;
    System.out.println ( Count_subarray ( arr , n ) ) ;;
}
 