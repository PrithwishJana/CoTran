var MAXN = 1000005 ;;
var even = { 0 } * MAXN ;;
var odd = { 0 } * MAXN ;;
public void precompute ( arr , n ) {
    for i in range ( n ) :
        if (( arr { i } % var 2 == 1 )) {
            odd { i } = 1 ;;
        }
         if (( arr { i } % 2 == 0 )) {
            even { i } = 1 ;;
        }
     for i in range ( 1 , n ) :
        even { i } = even { i } + even { i - 1 } ;;
        odd { i } = odd { i } + odd { i - 1 } ;;
}
public void isOdd ( L , R ) {
    var cnt = odd { R } ;;
    if (( L > 0 )) {
        cnt -= odd { L - 1 } ;;
    }
     if (( cnt == R - L + 1 )) {
        return true ;;
    }
     return false ;;
}
public void performQueries ( a , n , q , m ) {
    precompute ( a , n ) ;;
    for i in range ( m ) :
        var L = q { i } { 0 } ;;
        var R = q { i } { 1 } ;;
        if (( isOdd ( L , R ) )) {
            System.out.println ( "Odd" ) ;;
        }
         else{
            System.out.println ( "Even" ) ;;
        }
}
if (var __name__ == '__main__') {
    var a = { 2 , 1 , 5 , 7 , 6 , 8 , 9 } ;;
    var n = len ( a ) ;;
    var q = { [ 0 , 2 } , { 1 , 2 } , { 2 , 3 } , { 3 , 6 } ] ;;
    var m = len ( q ) ;;
    performQueries ( a , n , q , m ) ;;
}
 