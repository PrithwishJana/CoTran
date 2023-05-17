public void precisionCompute ( x , y , n ) {
    if (var y == 0) {
        System.out.println ( "Infinite" ) ;;
        return ;;
    }
     if (x == 0) {
        System.out.println ( 0 ) ;;
        return ;;
    }
     if (n <= 0) {
        System.out.println ( x // y ) ;;
        return ;;
    }
     if (( ( ( x > 0 ) and ( y < 0 ) ) or ( ( x < 0 ) and ( y > 0 ) ) )) {
        System.out.println ( "-" , end = "" ) ;;
        if (x <= 0) {
            x = - x ;;
        }
         if (y <= 0) {
            y = - y ;;
        }
     }
     d = x // y ;;
    for i in range ( 0 , n + 1 ) :
        System.out.println ( d , end = "" ) ;;
        x = x - ( y * d ) ;;
        if (x == 0) {
            break ;;
        }
         x = x * 10 ;;
        d = x // y ;;
        if (( i == 0 )) {
            System.out.println ( "." , end = "" ) ;;
        }
 }
x = 22 ;;
y = 7 ;;
var n = 15 ;;
precisionCompute ( x , y , n ) ;;
System.out.println ( );
