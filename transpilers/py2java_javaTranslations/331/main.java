var M = list ( map ( int , input ( ) . split ( ' ' ) ) );
var a = M { 0 };
var b = M { 1 };
n = M { 2 };
if (a != 0) {
    if (b % a != 0) {
        System.out.println ( 'No solution' );
    }
     else{
        b = b // a;
        x , y = 0 , - 2000;
        if (b >= 0) {
            while (y < b) {
                y = pow ( x , n );
                x = x + 1;
            }
             if (y > b) {
                System.out.println ( 'No solution' );
             }
             else{
                System.out.println ( x - 1 );
            }
        }
         else{
            if (n % 2 == 0) {
                System.out.println ( 'No solution' );
            }
             else{
                x = - 1;
                y = 2000;
                while (y > b) {
                    y = pow ( x , n );
                    x = x - 1;
                }
                 if (y < b) {
                    System.out.println ( 'No solution' );
                 }
                 else{
                    System.out.println ( x + 1 );
                }
            }
        }
    }
}
 else{
    if (b == 0) {
        System.out.println ( 5 );
    }
     else{
        System.out.println ( 'No solution' );
    }
}
