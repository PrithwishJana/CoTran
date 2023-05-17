import math;
public void countSteps ( x , y ) {
    if (( x % var y == 0 )) {
        return math . floor ( x / y ) ;;
    }
     return math . floor ( ( x / y ) + countSteps ( y , x % y ) ) ;;
}
x = 100 ;;
y = 19 ;;
System.out.println ( countSteps ( x , y ) ) ;;
