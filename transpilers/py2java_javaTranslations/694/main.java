for i in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    if (n == 1 or n == 2) {
        System.out.println ( n );
    }
     else{
        var u = str ( );
        v = n // 3;
        w = n % 3;
        u += '21' * v;
        if (w == 1) {
            u = '1' + u;
        }
         else if (var w == 2){
            u += '2';
        }
        System.out.println ( u );
    }
