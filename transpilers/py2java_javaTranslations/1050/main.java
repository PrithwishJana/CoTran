public void compute ( ) {
    var ans = 0;
    var stack = { ( 1 , 3 , 1 , 2 ) };
    while (len ( stack ) > 0) {
        leftn , leftd , rightn , var rightd = stack . pop ( );
        var d = leftd + rightd;
        if (d <= 12000) {
            var n = leftn + rightn;
            ans += 1;
            stack . append ( ( n , d , rightn , rightd ) );
            stack . append ( ( leftn , leftd , n , d ) );
        }
     }
     return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 