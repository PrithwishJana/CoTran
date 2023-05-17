var x = int ( input ( ) );
for jj in range ( x ) :
    var n = int ( input ( ) );
    if n == 1 : System.out.println ( 3 );
    else{
        if (n % var 2 == 1) {
            System.out.println ( 1 );
        }
         else{
            p = 0;
            k = n;
            while (n % 2 == 0) {
                p += 1;
                n //= 2;
            }
             var t = 2 ** p;
            if (t == k) {
                System.out.println ( t + 1 );
            }
             else{
                System.out.println ( t );
            }
        }
    }
