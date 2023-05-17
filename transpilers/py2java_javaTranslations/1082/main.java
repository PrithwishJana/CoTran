import math ;;
public void cal_sin ( n ) {
    var accuracy = 0.0001 ;;
    var n = n * ( 3.142 / 180.0 ) ;;
    x1 = n ;;
    sinx = n ;;
    sinval = math . sin ( n ) ;;
    i = 1 ;;
    while (( true )) {
        denominator = 2 * i * ( 2 * i + 1 ) ;;
        x1 = - x1 * n * n / denominator ;;
        sinx = sinx + x1 ;;
        i = i + 1 ;;
        if (( accuracy <= abs ( sinval - sinx ) )) {
            break ;;
        }
     }
     System.out.println ( round ( sinx ) ) ;;
}
n = 90 ;;
cal_sin ( n ) ;;
