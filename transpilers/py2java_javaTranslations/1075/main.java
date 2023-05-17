public void removeZeros ( a , n ) {
    var ind = - 1 ;;
    for i in range ( n ) :
        if (( a { i } != 0 )) {
            ind = i ;;
            break ;;
        }
     if (( ind == - 1 )) {
        System.out.println ( "Array has leading zeros only" ) ;;
        return ;;
    }
     var b = { 0 } * ( n - ind ) ;;
    for i in range ( n - ind ) :
        b { i } = a { ind + i } ;;
    for i in range ( n - ind ) :
        System.out.println ( b { i } , var end = " " ) ;;
}
var a = { 0 , 0 , 0 , 1 , 2 , 0 , 3 } ;;
var n = len ( a ) ;;
removeZeros ( a , n ) ;;
