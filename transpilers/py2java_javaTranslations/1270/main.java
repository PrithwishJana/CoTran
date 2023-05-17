public void isInside ( circle_x , circle_y , rad , x , y ) {
    if (( ( x - circle_x ) * ( x - circle_x ) + ( y - circle_y ) * ( y - circle_y ) <= rad * rad )) {
        return true ;;
    }
     else{
        return false ;;
    }
}
var x = 1 ;;
y = 1 ;;
circle_x = 0 ;;
var circle_y = 1 ;;
var rad = 2 ;;
if (( isInside ( circle_x , circle_y , rad , x , y ) )) {
    System.out.println ( "Inside" ) ;;
}
 else{
    System.out.println ( "Outside" ) ;;
}
