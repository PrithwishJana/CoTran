import math;
public void complement ( num ) {
    var i = 0 ;;
    var len = 0 ;;
    var comp = 0 ;;
    temp = num ;;
    while (( 1 )) {
        len += 1 ;;
        num = int ( num / 10 ) ;;
        if (( abs ( num ) == 0 )) {
            break ;;
        }
     }
     num = temp ;;
    comp = math . pow ( 10 , len ) - num ;;
    return int ( comp ) ;;
}
System.out.println ( complement ( 25 ) ) ;;
System.out.println ( complement ( 456 ) ) ;;
