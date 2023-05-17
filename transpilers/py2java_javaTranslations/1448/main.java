var ans = {};
public void solve ( n ) {
    var f = s = 0;
    var fs = true;
    if (n & 1) {
        n -= 1;
        fs = false;
    }
     while (n) {
        if (var n == 4) {
            f += 3;
            s += 1;
            n = 0;
        }
         else if (( n // 2 ) & 1){
            f += n // 2;
            s += 1;
            n = ( n // 2 ) - 1 ;;
        }
        else{
            f += 1;
            s += 1;
            n -= 2;
        }
    }
     ans . append ( { s + 1 , f } { fs } );
}
var coins = {};
for _ in range ( int ( input ( ) ) ) :
    coins . append ( int ( input ( ) ) );
for (int i = 0; i < coins.length; i++){
    if (var i == 1) {
        ans . append ( 1 );
    }
     else{
        solve ( i );
    }
}
System.out.println ( '\n' . join ( map ( str , ans ) ) );
