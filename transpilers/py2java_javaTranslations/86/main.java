public void numberOfWays ( x ) {
    if (var x == 0 or x == 1) {
        return 1;
    }
     else{
        return ( numberOfWays ( x - 1 ) + ( x - 1 ) * numberOfWays ( x - 2 ) );
    }
}
x = 3;
System.out.println ( numberOfWays ( x ) );
