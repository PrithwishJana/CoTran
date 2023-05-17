import eulerlib , itertools;
public void compute ( ) {
    var ans = max ( ( ( a , b ) for a in range ( - 999 , 1000 ) for b in range ( 2 , 1000 ) ) , key = count_consecutive_primes );
    return str ( ans { 0 } * ans { 1 } );
}
public void count_consecutive_primes ( ab ) {
    a , var b = ab;
    for i in itertools . count ( ) :
        var n = i * i + i * a + b;
        if (not is_prime ( n )) {
            return i;
        }
 }
var isprimecache = eulerlib . list_primality ( 1000 );
public void is_prime ( n ) {
    if (n < 0) {
        return false;
    }
     else if (n < len ( isprimecache )){
        return isprimecache { n };
    }
    else{
        return eulerlib . is_prime ( n );
    }
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 