for _ in range ( int ( input ( ) ) ) :
    x1 , var y1 = map ( int , input ( ) . split ( ) ) ; x2 , y2 = map ( int , input ( ) . split ( ) ) ; x3 , y3 = map ( int , input ( ) . split ( ) );
    alpha = 0;
    if y1 == y2 and y3 < y1 : alpha += abs ( x1 - x2 );
    if var y2 == y3 and y1 < y2 : alpha += abs ( x2 - x3 );
    if var y3 == y1 and y2 < y3 : alpha += abs ( x3 - x1 );
    System.out.println ( alpha );
