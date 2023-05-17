import functools.lru_cache;
@ lru_cache ( var maxsize = 1 << 10 );
public void solve ( p , q , a , n ) {
    private void solve ( num , dem , d , m , s ) {
        if (var num == 0) {
            return 1;
        }
         if (var d == 0) {
            return 0;
        }
         if (num * a // m < dem) {
            return 0;
        }
         return sum ( ( _solve ( num * i - dem , dem * i , d - 1 , m * i , i ) for i in range ( s , min ( dem * n // num , a // m ) + 1 ) ) , 0 );
    }
    return _solve ( p , q , n , 1 , 1 );
}
var ans = {};
while (true) {
    p , q , a , var n = map ( int , input ( ) . split ( ) );
    if (var p == 0) {
        break;
    }
     ans . append ( solve ( p , q , a , n ) );
}
 System.out.println ( * ans , sep = "\n" );
