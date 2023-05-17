import math;
public void cubeSide ( h , r ) {
    if (( h < 0 and r < 0 )) {
        return - 1;
    }
     var a = ( ( h * r * math . sqrt ( 2 ) ) / ( h + math . sqrt ( 2 ) * r ) );
    return a;
}
var h = 5 ; r = 6 ;;
System.out.println ( cubeSide ( h , r ) , "\n" );
