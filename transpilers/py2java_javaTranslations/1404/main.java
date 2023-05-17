import numpy as np;
var maxN = 20;
var maxM = 64;
var dp = np . zeros ( ( maxN , maxM ) ) ;;
var v = np . zeros ( ( maxN , maxM ) ) ;;
public void findLen ( arr , i , curr , n , m ) {
    if (( var i == n )) {
        if (( var curr == m )) {
            return 0 ;;
        }
         else{
            return - 1 ;;
        }
    }
     if (( v { i } { curr } )) {
        return dp { i } { curr } ;;
    }
     v { i } { curr } = 1 ;;
    var l = findLen ( arr , i + 1 , curr , n , m ) ;;
    var r = findLen ( arr , i + 1 , curr | arr { i } , n , m ) ;;
    dp { i } { curr } = l ;;
    if (( r != - 1 )) {
        dp { i } { curr } = max ( dp { i } { curr } , r + 1 ) ;;
    }
     return dp { i } { curr } ;;
}
if (__name__ == "__main__") {
    arr = { 3 , 7 , 2 , 3 } ;;
    var n = len ( arr ) ;;
    var m = 3 ;;
    var ans = findLen ( arr , 0 , 0 , n , m ) ;;
    if (( ans == - 1 )) {
        System.out.println ( 0 ) ;;
    }
     else{
        System.out.println ( ans ) ;;
    }
}
 