public void possibleTripletInRange ( L , R ) {
    var flag = false ;;
    possibleA = 0 ;;
    possibleB = 0 ;;
    possibleC = 0 ;;
    numbersInRange = ( R - L + 1 ) ;;
    if (( numbersInRange < 3 )) {
        flag = false ;;
    }
     else if (( numbersInRange > 3 )){
        flag = true ;;
        if (( ( L % 2 ) > 0 )) {
            L += 1 ;;
        }
         possibleA = L ;;
        possibleB = L + 1 ;;
        possibleC = L + 2 ;;
    }
    else{
        if (( ( L % 2 ) == 0 )) {
            flag = true ;;
            possibleA = L ;;
            possibleB = L + 1 ;;
            possibleC = L + 2 ;;
        }
         else{
            flag = false ;;
        }
    }
    if (( flag == true )) {
        System.out.println ( "(" , possibleA , "," , possibleB , "," , possibleC , ") is one such","possible triplet between" , L , "and" , R ) ;;
    }
     else{
        System.out.println ( "No Such Triplet exists between" , L , "and" , R ) ;;
    }
}
var L = 2 ;;
R = 10 ;;
possibleTripletInRange ( L , R ) ;;
L = 23 ;;
var R = 46 ;;
possibleTripletInRange ( L , R ) ;;
