public void subarrayCount ( arr , n ) {
    var result = 0;
    fast , var slow = 0 , 0;
    for i in range ( 1 , n ) :
        if (( arr { i } - arr { i - 1 } == 1 )) {
            fast += 1;
        }
         else{
            length = fast - slow + 1;
            result += length * ( length - 1 ) // 2 ;;
            fast = i;
            slow = i;
        }
    if (( fast != slow )) {
        var length = fast - slow + 1;
        result += length * ( length - 1 ) // 2 ;;
    }
     return result;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 5 , 6 , 7 };
    var n = len ( arr );
    System.out.println ( subarrayCount ( arr , n ) );
}
 