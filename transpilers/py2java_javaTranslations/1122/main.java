public void gcd ( a , b ) {
    if (var a == 0) {
        return b;
    }
     return gcd ( b % a , a );
}
a = 10;
b = 15;
System.out.println ( "GCD(" , a , "," , b , ") =" , gcd ( a , b ) );
a = 35;
b = 10;
System.out.println ( "GCD(" , a , "," , b , ") =" , gcd ( a , b ) );
a = 31;
var b = 2;
System.out.println ( "GCD(" , a , "," , b , ") =" , gcd ( a , b ) );
