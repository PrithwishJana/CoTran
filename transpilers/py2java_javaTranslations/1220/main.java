public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return gcd ( b % a , a );
}
public void findNumber ( arr , n ) {
    var ans = arr { 0 };
    for i in range ( 0 , n ) :
        ans = gcd ( ans , arr { i } );
    for i in range ( 0 , n ) :
        if (( arr { i } == ans )) {
            return ans;
        }
     return - 1;
}
var arr = { 2 , 2 , 4 } ;;
var n = len ( arr );
System.out.println ( findNumber ( arr , n ) );
