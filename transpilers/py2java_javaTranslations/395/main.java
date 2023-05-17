public void generateArr ( arr , n ) {
    if (( var n == 1 )) {
        System.out.println ( arr { 0 } ) ;;
        return ;;
    }
     barr = { 0 } * n ;;
    barr { 0 } = arr { 0 } & arr { 1 } ;;
    barr { n - 1 } = arr { n - 1 } & arr { n - 2 } ;;
    for i in range ( 1 , n - 1 ) :
        barr { i } = arr { i - 1 } & arr { i + 1 } ;;
    for i in range ( n ) :
        System.out.println ( barr { i } , end = " " ) ;;
}
if (__name__ == '__main__') {
    arr = { 1 , 2 , 3 , 4 , 5 , 6 } ;;
    n = len ( arr ) ;;
    generateArr ( arr , n ) ;;
}
 