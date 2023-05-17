public void factorial ( n ) {
    var i = n;
    var fact = 1;
    while (( n / i != n )) {
        fact = fact * i;
        i -= 1;
    }
     return fact;
}
var num = 5 ;;
System.out.println ( "Factorial of" , num , "is" , factorial ( num ) );
