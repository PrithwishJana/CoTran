var t = int ( input ( ) );
for i in range ( 0 , t ) :
    n = int ( input ( ) );
    start_point = 0;
    var numb_moves = 0;
    if (var n == 1) {
        System.out.println ( 2 );
    }
     else if (n % 3 == 0){
        System.out.println ( int ( n / 3 ) );
        continue;
    }
    else if (n == 2 or n == 3){
        System.out.println ( 1 );
    }
    else{
        var x = n % 3;
        System.out.println ( int ( ( n - x ) / 3 + 1 ) );
    }
