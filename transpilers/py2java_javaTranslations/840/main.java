public void Vertices ( x , y ) {
    var val = abs ( x ) + abs ( y ) ;;
    if (x < 0) {
        var x = - 1;
    }
     else{
        x = 1;
    }
    System.out.println ( val * x , "0" , end = " " ) ;;
    if (y < 0) {
        y = - 1;
    }
     else{
        y = 1;
    }
    System.out.println ( "0" , val * y ) ;;
}
if (__name__ == "__main__") {
    x = 3 ; var y = 3 ;;
    Vertices ( x , y ) ;;
}
 