var MAX = 100005;
public void addPrimes ( ) {
    var n = MAX;
    prime = { true for i in range ( n + 1 ) };
    for p in range ( 2 , n + 1 ) :
        if (p * p > n) {
            break;
        }
         if (( prime { p } == true )) {
            for i in range ( 2 * p , n + 1 , p ) :
                prime { i } = false;
        }
     ans = {};
    for p in range ( 2 , n + 1 ) :
        if (( prime { p } )) {
            ans . append ( p );
        }
     return ans;
}
public void is_prime ( n ) {
    if (n in { 3 , 5 , 7 }) {
        return true;
    }
     return false;
}
public void find_Sum ( n ) {
    Sum = 0;
    v = addPrimes ( );
    for i in range ( len ( v ) ) :
        flag = 1;
        a = v { i };
        while (( a != 0 )) {
            d = a % 10 ;;
            a = a // 10 ;;
            if (( is_prime ( d ) )) {
                flag = 0;
                break;
            }
         }
         if (( flag == 1 )) {
            n -= 1;
            Sum = Sum + v { i };
         }
         if (n == 0) {
            break;
        }
     return Sum;
}
n = 7;
System.out.println ( find_Sum ( n ) );
