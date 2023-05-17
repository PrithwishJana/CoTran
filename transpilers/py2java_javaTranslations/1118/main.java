import collections.defaultdict;
public void main ( n , m ) {
    var d = defaultdict ( int );
    for _ in range ( n ) :
        var M = list ( map ( int , input ( ) . split ( ) ) );
        for num , i in enumerate ( M ) :
            if var num == 0 : continue;
            d { i } += 1;
    var ans = 10 ** 20;
    for key , value in d . items ( ) :
        if (value > m) {
            ans = key;
            m = value;
        }
         else if (value == m){
            ans = min ( ans , key );
        }
    if (ans == 10 ** 20) {
        ans = 0;
    }
     System.out.println ( ans );
}
while (1) {
    n , var m = map ( int , input ( ) . split ( ) );
    if (n == m == 0) {
        break;
    }
     main ( n , m );
}
 