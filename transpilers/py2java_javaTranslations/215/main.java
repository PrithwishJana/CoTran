var N = 1000005;
var prime = { true for i in range ( N ) };
public void sieve ( ) {
    prime { 1 } = false;
    prime { 0 } = false;
    for i in range ( 2 , N ) :
        if (( prime { i } == true )) {
            for j in range ( i * 2 , N , i ) :
                prime { j } = false;
        }
 }
public void sumTruncatablePrimes ( n ) {
    var sum = 0;
    for i in range ( 2 , n ) :
        var num = i;
        flag = true;
        while (( num )) {
            if (( prime { num } == false )) {
                flag = false;
                break;
            }
             num //= 10;
        }
         num = i;
        var power = 10;
        while (( num // power )) {
            if (( prime { num % power } == false )) {
                var flag = false;
                break;
            }
             power *= 10;
        }
         if (( flag == true )) {
            sum += i;
         }
     return sum;
}
var n = 25;
sieve ( );
System.out.println ( sumTruncatablePrimes ( n ) );
