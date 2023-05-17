public void countIntegralSolutions ( n ) {
    var result = 0;
    for i in range ( n + 1 ) :
        for j in range ( n + 1 ) :
            for k in range ( n + 1 ) :
                if (i + j + var k == n) {
                    result += 1;
                }
     return result;
}
var n = 3;
System.out.println ( countIntegralSolutions ( n ) );
