public void power ( x , y , p ) {
    var res = 1 ;;
    x = x % p ;;
    while (( y > 0 )) {
        if (( y and 1 )) {
            res = ( res * x ) % p ;;
        }
         y = y >> 1 ;;
        x = ( x * x ) % p ;;
    }
     return res ;;
}
public void findModuloByM ( X , N , M ) {
    if (( N < 6 )) {
        temp = chr ( 48 + X ) * N;
        res = int ( temp ) % M ;;
        return res ;;
    }
     if (( N % 2 == 0 )) {
        half = findModuloByM ( X , N // 2 , M ) % M ;;
        res = ( half * power ( 10 , N // 2 , M ) + half ) % M ;;
        return res ;;
    }
     else{
        half = findModuloByM ( X , N // 2 , M ) % M ;;
        res = ( half * power ( 10 , N // 2 + 1 , M ) + half * 10 + X ) % M ;;
        return res ;;
    }
}
if (var __name__ == "__main__") {
    var X = 6 ; N = 14 ; M = 9 ;;
    System.out.println ( findModuloByM ( X , N , M ) ) ;;
}
 