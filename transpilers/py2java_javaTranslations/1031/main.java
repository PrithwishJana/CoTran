public void reduceString ( s , l ) {
    var count = 1 ;;
    steps = 0 ;;
    for i in range ( 1 , l ) :
        if (( s { i } == s { i - 1 } )) {
            count += 1 ;;
        }
         else{
            steps += ( int ) ( count / 2 ) ;;
            count = 1 ;;
        }
    steps += ( int ) ( count / 2 ) ;;
    return steps ;;
}
var s = "geeksforgeeks" ;;
var l = len ( s ) ;;
System.out.println ( reduceString ( s , l ) ) ;;
