public void multiply ( v , x ) {
    var carry = 0;
    size = len ( v );
    for i in range ( size ) :
        res = carry + v { i } * x;
        v { i } = res % 10;
        carry = res // 10;
    while (( carry != 0 )) {
        v . append ( carry % 10 );
        carry //= 10;
    }
 }
public void findSumOfDigits ( n ) {
    var v = {};
    v . append ( 1 );
    for i in range ( 1 , n + 1 ) :
        multiply ( v , i );
    var sum = 0;
    var size = len ( v );
    for i in range ( size ) :
        sum += v { i };
    return sum;
}
if (var __name__ == "__main__") {
    var n = 1000;
    System.out.println ( findSumOfDigits ( n ) );
}
 