var t = int ( input ( ) );
for test in range ( t ) :
    w , h , n = map ( int , input ( ) . split ( ) );
    w_first = w;
    h_first = h;
    if (n == 1) {
        System.out.println ( 'YES' );
    }
     else if (w % 2 == 1 and h % 2 == 1){
        System.out.println ( 'NO' );
    }
    else{
        if (w % 2 == 0 and h % 2 == 1) {
            count = 0;
            while (w % 2 == 0) {
                w /= 2;
                count += 1;
            }
             if (w == 1) {
                num = w_first;
             }
             else{
                num = 2 ** count;
            }
        }
         else if (h % 2 == 0 and w % 2 == 1){
            count = 0;
            while (h % 2 == 0) {
                h /= 2;
                count += 1;
            }
             if (h == 1) {
                num = h_first;
             }
             else{
                num = 2 ** count;
            }
        }
        else if (h % 2 == 0 and w % 2 == 0){
            num = 0;
            count = 0;
            while (w % 2 == 0) {
                w /= 2;
                count += 1;
            }
             if (w == 1) {
                num1 = w_first;
             }
             else{
                num1 = 2 ** count;
            }
            count = 0;
            while (h % var 2 == 0) {
                h /= 2;
                count += 1;
            }
             if (h == 1) {
                num2 = h_first;
             }
             else{
                num2 = 2 ** count;
            }
            var num = num1 * num2;
        }
        if (num >= n) {
            System.out.println ( 'YES' );
        }
         else{
            System.out.println ( 'NO' );
        }
    }
