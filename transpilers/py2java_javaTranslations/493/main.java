public void minimumSwaps ( arr ) {
    var count = 0 ;;
    var i = 0 ;;
    while (( i < len ( arr ) )) {
        if (( arr { i } != i + 1 )) {
            while (( arr { i } != i + 1 )) {
                var temp = 0 ;;
                temp = arr { arr [ i } - 1 ] ;;
                arr { arr [ i } - 1 ] = arr { i } ;;
                arr { i } = temp ;;
                count += 1 ;;
            }
        }
          i += 1 ;;
    }
     return count ;;
}
if (var __name__ == '__main__') {
    var arr = { 2 , 3 , 4 , 1 , 5 } ;;
    System.out.println ( minimumSwaps ( arr ) ) ;;
}
 