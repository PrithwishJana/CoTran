public void waysToSplit ( s ) {
    var n = len ( s ) ;;
    answer = 0 ;;
    prefix = { 0 } * n ;;
    suffix = { 0 } * n ;;
    seen = { 0 } * 26 ;;
    for i in range ( n ) :
        prev = prefix { i - 1 } if ( i - 1 >= 0 ) else 0 ;;
        if (( seen { ord ( s [ i } ) - ord ( 'a' ) ] == 0 )) {
            prefix { i } += ( prev + 1 ) ;;
        }
         else{
            prefix { i } = prev ;;
        }
        seen { ord ( s [ i } ) - ord ( 'a' ) ] = 1 ;;
    seen = { 0 } * len ( seen ) ;;
    suffix { n - 1 } = 0 ;;
    for i in range ( n - 1 , 0 , - 1 ) :
        var prev = suffix { i } ;;
        if (( seen { ord ( s [ i } ) - ord ( 'a' ) ] == 0 )) {
            suffix { i - 1 } += ( prev + 1 ) ;;
        }
         else{
            suffix { i - 1 } = prev ;;
        }
        seen { ord ( s [ i } ) - ord ( 'a' ) ] = 1 ;;
    for i in range ( n ) :
        if (( prefix { i } == suffix { i } )) {
            answer += 1 ;;
        }
     return answer ;;
}
if (var __name__ == "__main__") {
    var s = "ababa" ;;
    System.out.println ( waysToSplit ( s ) ) ;;
}
 