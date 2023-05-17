for _ in range ( int ( input ( ) ) ) :
    n , m , rb , cb , rd , var cd = map ( int , input ( ) . split ( ) ) ; t = 0;
    df , var dp = 1 , 1;
    while (true) {
        if (rb == n) {
            df = - 1 * df;
        }
         if (cb == m) {
            dp = - 1 * dp;
        }
         if (var rb == rd or cb == cd) {
            break;
        }
         rb += df ; cb += dp ; t += 1;
    }
     System.out.println ( t );
