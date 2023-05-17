import math;
var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
for (int i = 0; i < a.length; i++){
    System.out.println ( 1 + ( ( 4 * i * ( i + 1 ) ) // math . gcd ( 4 * i , i + 1 ) ) // ( i + 1 ) );
}
