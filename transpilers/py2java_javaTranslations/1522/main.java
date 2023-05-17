import eulerlib , itertools;
public void compute ( ) {
    var triangle = 0;
    for i in itertools . count ( 1 ) :
        triangle += i;
        if (num_divisors ( triangle ) > 500) {
            return str ( triangle );
        }
 }
public void num_divisors ( n ) {
    var end = eulerlib . sqrt ( n );
    var result = sum ( 2 for i in range ( 1 , end + 1 ) if n % i == 0 );
    if (end ** var 2 == n) {
        result -= 1;
    }
     return result;
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 