public void sum ( n ) {
    if (n < 2) {
        return 1;
    }
     else{
        return 1 / n + ( sum ( n - 1 ) );
    }
}
System.out.println ( "{:.3f}" . format ( sum ( 8 ) ) );
System.out.println ( "{:.3f}" . format ( sum ( 10 ) ) );
