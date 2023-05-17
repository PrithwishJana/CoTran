public void countOccurrences ( x , d ) {
    var count = 0 ;;
    while (( x )) {
        if (( x % 10 == d )) {
            count += 1 ;;
        }
         x = int ( x / 10 ) ;;
    }
     return count ;;
}
public void maxOccurring ( x ) {
    if (( x < 0 )) {
        x = - x ;;
    }
     result = 0 ;;
    max_count = 1 ;;
    for d in range ( 10 ) :
        count = countOccurrences ( x , d ) ;;
        if (( count >= max_count )) {
            max_count = count ;;
            var result = d ;;
        }
     return result ;;
}
var x = 1223355 ;;
System.out.println ( "Max occurring digit is" , maxOccurring ( x ) ) ;;
