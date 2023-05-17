import math.*;
public void countCubes ( a , b ) {
    return ( floor ( b ** ( 1. / 3. ) ) - ceil ( a ** ( 1. / 3. ) ) + 1 );
}
var a = 7;
var b = 28;
System.out.println ( "Count of cubes is" , countCubes ( a , b ) );
