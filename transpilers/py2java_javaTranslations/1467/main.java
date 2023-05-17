public void max_sum ( a , n ) {
    var dp = { 0 } * n ;;
    if (( var n == 1 )) {
        dp { 0 } = max ( 0 , a { 0 } ) ;;
    }
     else if (( n == 2 )){
        dp { 0 } = max ( 0 , a { 0 } ) ;;
        dp { 1 } = max ( a { 1 } , dp { 0 } ) ;;
    }
    else if (( n >= 3 )){
        dp { 0 } = max ( 0 , a { 0 } ) ;;
        dp { 1 } = max ( a { 1 } , max ( 0 , a { 0 } ) ) ;;
        dp { 2 } = max ( a { 2 } , max ( a { 1 } , max ( 0 , a { 0 } ) ) ) ;;
        i = 3 ;;
        while (( i < n )) {
            dp { i } = max ( dp { i - 1 } , a { i } + dp { i - 3 } ) ;;
            i += 1 ;;
        }
    }
     return dp { n - 1 } ;;
}
if (__name__ == "__main__") {
    arr = { 1 , 2 , - 2 , 4 , 3 } ;;
    n = len ( arr ) ;;
    System.out.println ( max_sum ( arr , n ) ) ;;
}
 