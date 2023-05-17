public void properDivisorSum ( n ) {
    var sum = 0;
    for i in range ( n + 1 ) :
        for j in range ( 1 , i + 1 ) :
            if (j * j > i) {
                break;
            }
             if (( i % j == 0 )) {
                if (( i // j == j )) {
                    sum += j;
                }
                 else{
                    sum += j + i // j;
                }
            }
         sum = sum - i;
    return sum;
}
if (var __name__ == '__main__') {
    var n = 4;
    System.out.println ( properDivisorSum ( n ) );
    n = 5;
    System.out.println ( properDivisorSum ( n ) );
}
 