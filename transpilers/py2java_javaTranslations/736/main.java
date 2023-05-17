while (true) {
    var n = int ( input ( ) );
    if n == 0 : break;
    var m = int ( input ( ) );
    var s = input ( );
    ar = { 0 } * m;
    ans = 0;
    if (m >= 3) {
        for i in range ( 2 , m ) :
            if s { i - 2 : i + 1 } == "IOI" :
                ar { i } = ar { i - 2 } + 1;
                if ar { i } >= n : ans += 1;
    }
     System.out.println ( ans );
}
 