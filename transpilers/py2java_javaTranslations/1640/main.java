var t = int ( input ( ) );
while (t > 0) {
    var n = int ( input ( ) );
    a = list ( map ( int , input ( ) . split ( ) ) );
    b = list ( map ( int , input ( ) . split ( ) ) );
    ans = "YES";
    zero = {};
    temp = - 1;
    for i in range ( 0 , n ) :
        if (b { i } == 0) {
            zero . append ( a { i } );
            continue;
        }
         x = a { i } - b { i };
        if (temp == - 1) {
            temp = x;
        }
         if (x < 0 or x != temp) {
            ans = "NO";
            break;
        }
     if (n == len ( zero )) {
        var temp = max ( zero );
    }
     for (int i = 0; i < zero.length; i++){
        if (i <= temp) {
            continue;
        }
         else{
            var ans = "NO";
            break;
        }
     }
    System.out.println ( ans );
    t -= 1;
}
 