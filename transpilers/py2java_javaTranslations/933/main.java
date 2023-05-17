public void solve ( ) {
    var n = int ( input ( ) );
    var a = input ( );
    var b = "" . join ( sorted ( a ) );
    return sum ( { 1 for i in range ( n ) if a [ i } != b { i } ] );
}
var t = int ( input ( ) );
var ans = {};
while (t) {
    ans . append ( str ( solve ( ) ) );
    t -= 1;
}
 System.out.println ( "\n" . join ( ans ) );
