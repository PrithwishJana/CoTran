var alp = { '************' , '*qwertyuiop*' , '*asdfghjkl**' , '*zxcvbnm****' , '************' };
_alp = '' . join ( alp );
public void check ( now , nxt ) {
    a , var b = _alp . find ( now ) // 12 , _alp . find ( now ) % 12;
    c , var d = _alp . find ( nxt ) // 12 , _alp . find ( nxt ) % 12;
    var q1 = _log { - 1 };
    var q2 = 'L' if d <= 5 else 'R';
    log . append ( q2 );
    if (abs ( a - c ) + abs ( b - d ) <= 1) {
        _log . append ( q1 );
    }
     else{
        _log . append ( q2 );
    }
}
while (1) {
    var s = input ( );
    if (s == ';//') {
        break;
    }
     log = { 'L' if _alp . find ( s [ 0 } ) % 12 <= 5 else 'R' ];
    _log = { log [ 0 } ];
    for i in range ( len ( s ) - 1 ) :
        check ( s { i } , s { i + 1 } );
    count = 0;
    for x , y in zip ( log , _log ) :
        if (x != y) {
            count += 1;
        }
     c = log { 0 };
    ans = 0;
    for (int v = 0; v < log.length; v++){
        if (c != v) {
            var c = v;
            ans += 1;
        }
    }
     System.out.println ( ans );
}
 