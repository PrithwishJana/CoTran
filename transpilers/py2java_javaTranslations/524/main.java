public void findEle ( arr , n ) {
    var sum = 0;
    for i in range ( n ) :
        sum += arr { i };
    for i in range ( n ) :
        if (arr { i } == sum - arr { i }) {
            return arr { i };
        }
     return - 1;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 6 };
    var n = len ( arr );
    System.out.println ( findEle ( arr , n ) );
}
 