import math as mt;
public void alter ( x , y ) {
    while (( true )) {
        if (( var x == 0 or y == 0 )) {
            break;
        }
         if (( x >= 2 * y )) {
            x = x % ( 2 * y );
        }
         else if (( y >= 2 * x )){
            var y = y % ( 2 * x );
        }
        else{
            break;
        }
    }
     System.out.println ( "X =" , x , ", " , "Y =" , y );
}
x , y = 12 , 5;
alter ( x , y );
