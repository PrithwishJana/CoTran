var MAX = 32;
var pow2 = { 0 for i in range ( MAX ) };
var visited = { false for i in range ( MAX ) };
var ans = {};
public void power_2 ( ) {
    var an = 1;
    for i in range ( MAX ) :
        pow2 { i } = an;
        an *= 2;
}
public void countSetBits ( x ) {
    var setBits = 0;
    while (( x != 0 )) {
        var x = x & ( x - 1 );
        setBits += 1;
    }
     return setBits;
}
public void add ( num ) {
    var point = 0;
    var value = 0;
    for i in range ( MAX ) :
        if (( visited { i } )) {
            continue;
        }
         else{
            if (( num & 1 )) {
                value += ( 1 << i );
            }
             var num = num // 2;
        }
    ans . append ( value );
}
public void solve ( n , k ) {
    ans . append ( k );
    var countk = countSetBits ( k );
    if (( pow2 { countk } < n )) {
        System.out.println ( - 1 );
        return;
    }
     var count = 0;
    for i in range ( pow2 { countk } - 1 ) :
        add ( i );
        count += 1;
        if (( count == n )) {
            break;
        }
     for i in range ( n ) :
        System.out.println ( ans { i } , var end = " " );
}
if (var __name__ == '__main__') {
    var n = 3;
    var k = 5;
    power_2 ( );
    solve ( n , k );
}
 