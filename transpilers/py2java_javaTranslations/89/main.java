var t = int ( input ( ) );
for test in range ( t ) :
    n , var k = map ( int , input ( ) . split ( ) );
    if (k == 1) {
        if (n % var 2 == 1) {
            System.out.println ( 'YES' );
        }
         else{
            System.out.println ( 'NO' );
        }
    }
     else{
        if (n <= k) {
            System.out.println ( 'NO' );
        }
         else{
            if (n % 2 == 0 and k % 2 == 1) {
                System.out.println ( 'NO' );
            }
             else if (n % 2 == 1 and k % 2 == 0){
                System.out.println ( 'NO' );
            }
            else{
                x = 2 * k - 1;
                min_sum = ( ( 1 + x ) ** 2 ) / 4;
                if (min_sum > n) {
                    System.out.println ( 'NO' );
                }
                 else if (min_sum == n){
                    System.out.println ( 'YES' );
                }
                else{
                    if (( n - min_sum ) % 2 == 0) {
                        System.out.println ( 'YES' );
                    }
                     else{
                        System.out.println ( 'NO' );
                    }
                }
            }
        }
    }
