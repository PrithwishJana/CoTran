public void bomb_required ( n ) {
    System.out.println ( n + n // 2 );
    for i in range ( 2 , n + 1 , 2 ) :
        System.out.println ( i , var end = " " );
    for i in range ( 1 , n + 1 , 2 ) :
        System.out.println ( i , end = " " );
    for i in range ( 2 , n , 2 ) :
        System.out.println ( i , end = " " );
}
bomb_required ( 3 );
