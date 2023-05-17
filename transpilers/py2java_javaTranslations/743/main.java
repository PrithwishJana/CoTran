var a = int ( input ( ) );
for i in range ( a , 0 , - 1 ) :
    if (a % i == 0) {
        System.out.println ( i , end = ' ' );
        a = i;
    }
 