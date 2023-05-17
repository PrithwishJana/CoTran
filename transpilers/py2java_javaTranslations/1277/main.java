import math;
public void tri ( x1 , y1 , x2 , y2 , x3 , y3 ) {
    return math . fabs ( ( x2 - x1 ) * ( y3 - y1 ) - ( y2 - y1 ) * ( x3 - x1 ) ) / 2;
}
while (true) {
    try{
        x1 , y1 , x2 , y2 , x3 , y3 , x , var y = map ( float , input ( ) . split ( ) );
    }
    except :
        break;
    abc = tri ( x1 , y1 , x2 , y2 , x3 , y3 );
    abp = tri ( x1 , y1 , x2 , y2 , x , y );
    acp = tri ( x1 , y1 , x3 , y3 , x , y );
    bcp = tri ( x2 , y2 , x3 , y3 , x , y );
    x , y = int ( abc * pow ( 10 , 5 ) ) , int ( ( abp + acp + bcp ) * pow ( 10 , 5 ) );
    System.out.println ( "YES" if x >= y else "NO" );
}
 