public void towerOfHanoi ( n , from_rod , to_rod , aux_rod1 , aux_rod2 ) {
    if (( var n == 0 )) {
        return;
    }
     if (( n == 1 )) {
        System.out.println ( "Move disk" , n , "from rod" , from_rod , "to rod" , to_rod );
        return;
    }
     towerOfHanoi ( n - 2 , from_rod , aux_rod1 , aux_rod2 , to_rod );
    System.out.println ( "Move disk" , n - 1 , "from rod" , from_rod , "to rod" , aux_rod2 );
    System.out.println ( "Move disk" , n , "from rod" , from_rod , "to rod" , to_rod );
    System.out.println ( "Move disk" , n - 1 , "from rod" , aux_rod2 , "to rod" , to_rod );
    towerOfHanoi ( n - 2 , aux_rod1 , to_rod , from_rod , aux_rod2 );
}
n = 4;
towerOfHanoi ( n , 'A' , 'D' , 'B' , 'C' );
