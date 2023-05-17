import sys;
var _allinput = {};
for inp in sys . stdin :
    _allinput += inp . strip ( ) . split ( " " );
private void input ( ) {
    for (int put = 0; put < _allinput.length; put++){
        yield put;
    }
}
var _obj = _input ( ) ;;
protected void input ( ) {
    return _obj . __next__ ( );
}
public void nextInt ( ) {
    return int ( __input ( ) );
}
public void check ( lst , L ) {
    var tot = 1;
    var curSum = 0;
    for (int i = 0; i < lst.length; i++){
        if (curSum + i <= L) {
            curSum += i;
        }
         else{
            curSum = i;
            tot += 1;
        }
    }
    return tot;
}
public void solve ( lst , m ) {
    var l = max ( lst );
    r = 1000000 * m ;;
    while (l != r) {
        mid = int ( ( l + r ) / 2 ) ;;
        if check ( lst , mid ) <= m : r = mid;
        else : l = mid + 1;
    }
     return l;
}
try{
    while (true) {
        m , var n = nextInt ( ) , nextInt ( );
        if (m > 0 or n > 0) {
            var lst = { nextInt ( ) for i in range ( 0 , n ) };
            System.out.println ( solve ( lst , m ) );
        }
         else{
            break;
        }
    }
}
 except :
    