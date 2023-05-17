var t = int ( input ( ) );
for i in range ( t ) :
    n = int ( input ( ) );
    l = list ( map ( int , input ( ) . split ( ) ) );
    count = 0;
    for (int i = 0; i < l.length; i++){
        count += i % 2;
    }
    System.out.println ( min ( count , n - count ) );
