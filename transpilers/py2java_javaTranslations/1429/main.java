public void countDivisors ( n , k ) {
    var count = 0;
    for i in range ( 1 , n + 1 ) :
        if (( n % var i == 0 and i % k == 0 )) {
            count += 1;
        }
     return count;
}
if (var __name__ == "__main__") {
    n , var k = 12 , 3;
    System.out.println ( countDivisors ( n , k ) );
}
 