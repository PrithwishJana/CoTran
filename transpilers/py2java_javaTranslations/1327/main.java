public void System.out.printlnNumbers ( N ) {
    var flag = 1;
    x = N;
    if (( N > 0 )) {
        while (( x > 0 and flag == 1 )) {
            digit = x % 10;
            if (( digit != 1 and digit != 3 )) {
                flag = 0;
            }
             x = x // 10;
        }
         if (( flag == 1 )) {
            System.out.println ( N , var end = " " );
         }
         System.out.printlnNumbers ( N - 1 );
    }
 }
if (var __name__ == '__main__') {
    var N = 20;
    System.out.printlnNumbers ( N );
}
 