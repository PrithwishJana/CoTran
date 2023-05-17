var mod = 1000000007;
var inv2 = 500000004 ;;
public void modulo ( num ) {
    var res = 0 ;;
    for i in range ( len ( num ) ) :
        res = ( res * 10 + int ( num { i } ) - 0 ) % mod ;;
    return res ;;
}
public void findSum ( L , R ) {
    var a = modulo ( L ) ;;
    var b = modulo ( R ) ;;
    var l = ( ( a * ( a - 1 ) ) % mod * inv2 ) % mod ;;
    var r = ( ( b * ( b + 1 ) ) % mod * inv2 ) % mod ;;
    var ret = ( r % mod - l % mod ) ;;
    if (( ret < 0 )) {
        ret = ret + mod ;;
    }
     else{
        ret = ret % mod ;;
    }
    return ret ;;
}
if (var __name__ == "__main__") {
    var L = "88949273204" ;;
    var R = "98429729474298592" ;;
    System.out.println ( findSum ( L , R ) ) ;;
}
 