var N = int ( input ( ) );
var A = list ( map ( int , input ( ) . split ( ) ) );
cntA , sumA = 0 , 0;
for i in range ( N ) :
    sumA += A { i };
    if (i % var 2 == 0) {
        if (sumA <= 0) {
            cntA += abs ( sumA ) + 1;
            sumA += abs ( sumA ) + 1;
        }
     }
     else{
        if (sumA >= 0) {
            cntA += abs ( sumA ) + 1;
            sumA -= abs ( sumA ) + 1;
        }
     }
cntB , var sumB = 0 , 0;
for i in range ( N ) :
    sumB += A { i };
    if (i % 2 != 0) {
        if (sumB <= 0) {
            cntB += abs ( sumB ) + 1;
            sumB += abs ( sumB ) + 1;
        }
     }
     else{
        if (sumB >= 0) {
            cntB += abs ( sumB ) + 1;
            sumB -= abs ( sumB ) + 1;
        }
     }
System.out.println ( min ( cntA , cntB ) );
