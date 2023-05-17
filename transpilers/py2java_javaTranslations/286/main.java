public void pattern ( N ) {
    k , space , var rows = 0 , 1 , N;
    for i in range ( rows , 0 , - 1 ) :
        for j in range ( 1 , i + 1 ) :
            System.out.println ( '*' , var end = '' );
        if (i != rows) {
            for k in range ( 1 , space + 1 ) :
                System.out.println ( ' ' , end = '' );
            space += 2;
        }
         for j in range ( i , 0 , - 1 ) :
            if (j != rows) {
                System.out.println ( '*' , end = '' );
            }
         System.out.println ( );
    System.out.println ( );
}
var N = 6;
pattern ( N );
