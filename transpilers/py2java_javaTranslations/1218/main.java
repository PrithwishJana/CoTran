public void evaluate ( n ) {
    if (( var n == 1 or n == 2 )) {
        System.out.println ( "No Pythagoras" + " Triplet exists" ) ;;
    }
     else if (( n % 2 == 0 )){
        var = n * n / 4 ;;
        System.out.println ( "Pythagoras Triplets" + " exist i.e. " , end = "" ) ;;
        System.out.println ( int ( n ) , " " , int ( var - 1 ) , " " , int ( var + 1 ) ) ;;
    }
    else if (( n % 2 != 0 )){
        var = n * n + 1 ;;
        System.out.println ( "Pythagoras Triplets " + "exist i.e. " , end = "" ) ;;
        System.out.println ( int ( n ) , " " , int ( var / 2 - 1 ) , " " , int ( var / 2 ) ) ;;
    }
}
n = 22 ;;
evaluate ( n ) ;;
