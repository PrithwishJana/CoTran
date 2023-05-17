public void findDivisors ( n ) {
    var div = { 0 for i in range ( n + 1 ) };
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if (j * i <= n) {
                div { i * j } += 1;
            }
     for i in range ( 1 , n + 1 ) :
        System.out.println ( div { i } , var end = " " );
}
if (var __name__ == "__main__") {
    var n = 10;
    findDivisors ( n );
}
 