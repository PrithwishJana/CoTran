var N = 3 ;;
public void rotateMatrix ( mat ) {
    var i = N - 1 ;;
    while (( i >= 0 )) {
        j = N - 1 ;;
        while (( j >= 0 )) {
            System.out.println ( mat { i } { j } , end = " " ) ;;
            j = j - 1 ;;
        }
         System.out.println ( ) ;;
        i = i - 1 ;;
    }
 }
var mat = { [ 1 , 2 , 3 } , { 4 , 5 , 6 } , { 7 , 8 , 9 } ] ;;
rotateMatrix ( mat ) ;;
