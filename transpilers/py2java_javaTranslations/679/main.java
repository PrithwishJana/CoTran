public void FindPoints ( x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4 ) {
    var x5 = max ( x1 , x3 );
    var y5 = max ( y1 , y3 );
    var x6 = min ( x2 , x4 );
    var y6 = min ( y2 , y4 );
    if (( x5 > x6 or y5 > y6 )) {
        System.out.println ( "No intersection" );
        return;
    }
     System.out.println ( "(" , x5 , ", " , y5 , ") " , var end = " " );
    System.out.println ( "(" , x6 , ", " , y6 , ") " , end = " " );
    x7 = x5;
    y7 = y6;
    System.out.println ( "(" , x7 , ", " , y7 , ") " , end = " " );
    var x8 = x6;
    var y8 = y5;
    System.out.println ( "(" , x8 , ", " , y8 , ") " );
}
if (var __name__ == "__main__") {
    var x1 = 0;
    var y1 = 0;
    var x2 = 10;
    var y2 = 8;
    var x3 = 2;
    var y3 = 3;
    var x4 = 7;
    var y4 = 9;
    FindPoints ( x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4 );
}
 