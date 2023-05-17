public void equal_xor_sum ( arr , n ) {
    var Sum = 0 ;;
    Xor = 0 ;;
    for i in range ( n ) :
        Sum = Sum + arr { i } ;;
        Xor = Xor ^ arr { i } ;;
    if (( Sum == Xor )) {
        System.out.println ( "YES" ) ;;
    }
     else{
        System.out.println ( "NO" ) ;;
    }
}
if (var __name__ == "__main__") {
    var arr = { 6 , 3 , 7 , 10 } ;;
    var n = len ( arr ) ;;
    equal_xor_sum ( arr , n ) ;;
}
 