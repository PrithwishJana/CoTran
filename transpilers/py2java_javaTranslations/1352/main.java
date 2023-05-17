m , var n = 6 , 4 ;;
public void linearCheck ( ar , arr ) {
    for i in range ( m ) :
        var matched = true ;;
        for j in range ( n ) :
            if (( ar { i } { j } != arr { j } )) {
                matched = false ;;
                break ;;
            }
         if (( matched )) {
            return i + 1 ;;
        }
     return - 1 ;;
}
if (var __name__ == "__main__") {
    var mat = { [ 0 , 0 , 1 , 0 } , { 10 , 9 , 22 , 23 } , { 40 , 40 , 40 , 40 } , { 43 , 44 , 55 , 68 } , { 81 , 73 , 100 , 132 } , { 100 , 75 , 125 , 133 } ] ;;
    var row = { 10 , 9 , 22 , 23 } ;;
    System.out.println ( linearCheck ( mat , row ) ) ;;
}
 