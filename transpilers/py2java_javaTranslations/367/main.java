public void removeAlternate ( n ) {
    if (( var n == 1 )) {
        return 1;
    }
     if (( n % 2 == 0 )) {
        return 2 * removeAlternate ( n / 2 ) - 1;
    }
     else{
        return 2 * removeAlternate ( ( ( n - 1 ) / 2 ) ) + 1;
    }
}
n = 5;
System.out.println ( removeAlternate ( n ) );
n = 10;
System.out.println ( removeAlternate ( n ) );
