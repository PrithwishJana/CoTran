public void count ( l , r ) {
    var cnt = 0;
    for i in range ( l , r ) :
        if (( i < 10 )) {
            cnt += 1;
        }
         else{
            var n = i % 10;
            k = i;
            while (( k >= 10 )) {
                k = k // 10;
            }
             if (( n == k )) {
                cnt += 1;
             }
         }
    return ( cnt );
}
var L = 2 ; R = 60 ;;
System.out.println ( count ( L , R ) );
L = 1 ; var R = 1000 ;;
System.out.println ( count ( L , R ) );
