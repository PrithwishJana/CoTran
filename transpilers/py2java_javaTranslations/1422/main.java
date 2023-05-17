import math;
public void calculate ( x , k , m ) {
    var result = x ;;
    k = k - 1 ;;
    while (( k )) {
        result = math . pow ( result , x ) ;;
        if (( result > m )) {
            result = result % m ;;
        }
         var k = k - 1 ;;
    }
     return int ( result ) ;;
}
x = 5 ;;
k = 2 ;;
var m = 3 ;;
System.out.println ( calculate ( x , k , m ) ) ;;
