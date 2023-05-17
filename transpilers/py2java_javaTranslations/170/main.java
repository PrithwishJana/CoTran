import sys;
var input_methods = { 'clipboard' , 'file' , 'key' };
var using_method = 0;
var input_method = input_methods { using_method };
tin = lambda : map ( int , input ( ) . split ( ) );
lin = lambda : list ( tin ( ) );
mod = 1000000007;
public void main ( ) {
    n , k = tin ( );
    al = lin ( );
    al . sort ( reverse = true );
    ss = sum ( al );
    arrive = { 0 } * k;
    arrive { 0 } = 1;
    useful_set = set ( );
    for (int v = 0; v < al.length; v++){
        ss -= v;
        u_max = 0;
        if (v >= k) {
            useful_set . add ( v );
            continue;
        }
         for i , _ in enumerate ( arrive ) :
            p = k - i - 1;
            is_on = arrive { p };
            if (is_on == 1 and p + v >= k) {
                useful_set . add ( v );
                u_max = k;
            }
             else if (is_on == 1){
                arrive { p + v } = 1;
                u_max = max ( u_max , p + v );
            }
        if (u_max + ss >= k) {
            useful_set . add ( v );
        }
    }
     ret = 0;
    for (int v = 0; v < al.length; v++){
        if (v not in useful_set) {
            ret += 1;
        }
    }
     return ret;
}
isTest = false;
public void pa ( v ) {
    if (isTest) {
        System.out.println ( v );
    }
 }
public void input_clipboard ( ) {
    import clipboard;
    input_text = clipboard . get ( );
    input_l = input_text . splitlines ( );
    for (int l = 0; l < input_l.length; l++){
        yield l;
    }
}
if (__name__ == "__main__") {
    if (sys . platform == 'ios') {
        if (input_method == input_methods { 0 }) {
            ic = input_clipboard ( );
            input = lambda : ic . __next__ ( );
        }
         else if (input_method == input_methods { 1 }){
            sys . var stdin = open ( 'inputFile.txt' );
        }
        else {}
        var isTest = true;
    }
     else {}
    var ret = main ( );
    if (ret is not None) {
        System.out.println ( ret );
    }
 }
 