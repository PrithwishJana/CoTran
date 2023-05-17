public void count ( x , y ) {
    var ans = 0;
    var m = dict ( );
    while (x % y != 0) {
        x %= y;
        ans += 1;
        if (x in m) {
            return - 1;
        }
         m { x } = 1;
        x *= 10;
    }
     return ans;
}
if (var __name__ == "__main__") {
    var res = count ( 1 , 2 );
    System.out.println ( "INF" ) if res == - 1 else System.out.println ( res );
    res = count ( 5 , 3 );
    System.out.println ( "INF" ) if res == - 1 else System.out.println ( res );
    res = count ( 3 , 5 );
    System.out.println ( "INF" ) if res == - 1 else System.out.println ( res );
}
 