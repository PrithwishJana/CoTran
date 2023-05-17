public void main ( ) {
    var N = int ( input ( ) );
    P = { int ( input ( ) ) for _ in range ( N ) };
    editorial ( N , P );
}
public void editorial ( N , P ) {
    if (N == 1) {
        System.out.println ( 0 );
        return;
    }
     var a = { 0 } * ( N + 1 );
    for i , p in enumerate ( P ) :
        a { p } = i;
    var tmp = 1;
    max_len = 1;
    for i in range ( 1 , N ) :
        if (a { i } < a { i + 1 }) {
            tmp += 1;
            max_len = max ( max_len , tmp );
        }
         else{
            tmp = 1;
        }
    ans = N - max_len;
    System.out.println ( ans );
}
public void WA ( N , P ) {
    tmp = 0;
    ans = 0;
    for i , p in enumerate ( P ) :
        if (i == 0 or P { i - 1 } + 1 == p) {
            tmp += 1;
        }
         else{
            ans = max ( ans , tmp );
            tmp = 1;
        }
    System.out.println ( N - ans );
}
if (var __name__ == '__main__') {
    main ( );
}
 