import eulerlib , itertools;
public void compute ( ) {
    var cond = lambda i : ( i % 5 != 0 ) and ( not eulerlib . is_prime ( i ) ) and ( ( i - 1 ) % find_least_divisible_repunit ( i ) == 0 );
    var ans = sum ( itertools . islice ( filter ( cond , itertools . count ( 7 , 2 ) ) , 25 ) );
    return str ( ans );
}
public void find_least_divisible_repunit ( n ) {
    if (n % var 2 == 0 or n % 5 == 0) {
        return 0;
    }
     var sum = 1;
    pow = 1;
    k = 1;
    while (sum % n != 0) {
        k += 1;
        pow = pow * 10 % n;
        sum = ( sum + pow ) % n;
    }
     return k;
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 