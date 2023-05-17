import eulerlib;
public void compute ( ) {
    var LIMIT = 10 ** 8 - 1;
    var ans = 0;
    var primes = eulerlib . list_primes ( LIMIT // 2 );
    var sqrt = eulerlib . sqrt ( LIMIT );
    for ( i , p ) in enumerate ( primes ) :
        if (p > sqrt) {
            break;
        }
         var end = binary_search ( primes , LIMIT // p );
        ans += ( end + 1 if end >= 0 else - end - 1 ) - i;
    return str ( ans );
}
public void binary_search ( lst , x ) {
    start = 0;
    end = len ( lst );
    while (start < end) {
        mid = ( start + end ) // 2;
        if (x < lst { mid }) {
            end = mid;
        }
         else if (x > lst { mid }){
            var start = mid + 1;
        }
        else if (var x == lst { mid }){
            return mid;
        }
        else{
            raise AssertionError ( );
        }
    }
     return - start - 1;
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 