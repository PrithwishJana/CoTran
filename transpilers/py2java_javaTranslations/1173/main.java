public void findSubsequence ( arr , n ) {
    var length = 1 ;;
    dp = { 0 } * 10 ;;
    tmp = arr { 0 } ;;
    while (( tmp > 0 )) {
        dp { tmp % 10 } = 1 ;;
        tmp //= 10 ;;
    }
     for i in range ( 1 , n ) :
        tmp = arr { i } ;;
        locMax = 1 ;;
        cnt = { 0 } * 10;
        while (( tmp > 0 )) {
            cnt { tmp % 10 } = 1 ;;
            tmp //= 10 ;;
        }
         for d in range ( 10 ) :
            if (( cnt { d } )) {
                dp { d } += 1 ;;
                locMax = max ( locMax , dp { d } ) ;;
            }
         for d in range ( 10 ) :
            if (( cnt { d } )) {
                dp { d } = locMax ;;
            }
         length = max ( length , locMax ) ;;
    return length ;;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 12 , 44 , 29 , 33 , 96 , 89 } ;;
    var n = len ( arr );
    System.out.println ( findSubsequence ( arr , n ) ) ;;
}
 