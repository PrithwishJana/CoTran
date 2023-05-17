public void checkType ( arr , n ) {
    if (( arr { 0 } <= arr { 1 } and arr { n - 2 } <= arr { n - 1 } )) {
        System.out.println ( "Increasing" ) ;;
    }
     else if (( arr { 0 } >= arr { 1 } and arr { n - 2 } >= arr { n - 1 } )){
        System.out.println ( "Decreasing" ) ;;
    }
    else if (( arr { 0 } <= arr { 1 } and arr { n - 2 } >= arr { n - 1 } )){
        System.out.println ( "Increasing then decreasing" ) ;;
    }
    else{
        System.out.println ( "Decreasing then increasing" ) ;;
    }
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 4 } ;;
    var n = len ( arr ) ;;
    checkType ( arr , n ) ;;
}
 