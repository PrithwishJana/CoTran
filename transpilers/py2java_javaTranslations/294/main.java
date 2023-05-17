var MAX = 100 ;;
var n = 0 ;;
store = { 0 } * MAX ;;
graph = { [ 0 for i in range ( MAX ) } for j in range ( MAX ) ] ;;
d = { 0 } * MAX ;;
public void is_clique ( b ) {
    for i in range ( 1 , b ) :
        for j in range ( i + 1 , b ) :
            if (( graph { store [ i } ] { store [ j } ] == 0 )) {
                return false ;;
            }
     return true ;;
}
public void maxCliques ( i , l ) {
    max_ = 0 ;;
    for j in range ( i + 1 , n + 1 ) :
        store { l } = j ;;
        if (( is_clique ( l + 1 ) )) {
            max_ = max ( max_ , l ) ;;
            max_ = max ( max_ , maxCliques ( j , l + 1 ) ) ;;
        }
     return max_ ;;
}
if (__name__ == '__main__') {
    edges = { [ 1 , 2 } , { 2 , 3 } , { 3 , 1 } , { 4 , 3 } , { 4 , 1 } , { 4 , 2 } ] ;;
    size = len ( edges ) ;;
    n = 4 ;;
    for i in range ( size ) :
        graph { edges [ i } { 0 } ] { edges [ i } { 1 } ] = 1 ;;
        graph { edges [ i } { 1 } ] { edges [ i } { 0 } ] = 1 ;;
        d { edges [ i } { 0 } ] += 1 ;;
        d { edges [ i } { 1 } ] += 1 ;;
    System.out.println ( maxCliques ( 0 , 1 ) ) ;;
}
 