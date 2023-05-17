var tests = int ( input ( ) );
for _ in range ( tests ) :
    var windows = int ( input ( ) );
    var test = true;
    for k in range ( ( windows // 3 + 1 ) ) :
        if (test) {
            for j in range ( ( windows // 5 + 1 ) ) :
                if (test) {
                    for i in range ( ( windows // 7 + 1 ) ) :
                        if (i * 7 + j * 5 + k * 3 == windows) {
                            System.out.println ( k , j , i );
                            test = false;
                            break;
                        }
                 }
         }
     if (test) {
        System.out.println ( - 1 );
    }
 