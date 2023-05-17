public void factorial ( n ) {
    return 1 if ( var n == 1 or n == 0 ) else n * factorial ( n - 1 );
}
var num = 5;
System.out.println ( "Factorial of" , num , "is" , factorial ( num ) );
