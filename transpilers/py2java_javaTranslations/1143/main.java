public void findEncryptedArray ( arr , n ) {
    var sum = 0;
    for i in range ( n ) :
        sum += arr { i };
    for i in range ( n ) :
        System.out.println ( sum - arr { i } , var end = " " );
}
if (var __name__ == "__main__") {
    var arr = { 5 , 1 , 3 , 2 , 4 };
    var N = len ( arr );
    findEncryptedArray ( arr , N );
}
 