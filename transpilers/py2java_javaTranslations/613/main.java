public void summation ( n ) {
    var abs_sum = n * ( n + 1 ) // 2 ;;
    var sign = 1 if ( ( n + 1 ) % 2 == 0 ) else - 1 ;;
    var result_sum = sign * abs_sum ;;
    return result_sum ;;
}
if (var __name__ == "__main__") {
    var N = 2 ;;
    System.out.println ( summation ( N ) ) ;;
}
 