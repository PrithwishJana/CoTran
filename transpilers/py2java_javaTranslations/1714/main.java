public void getPerfectSquares ( n ) {
    var perfectSquares = {} ;;
    current = 1 ;;
    i = 1 ;;
    while (( current <= n )) {
        perfectSquares . append ( current ) ;;
        i += 1 ;;
        current = int ( pow ( i , 2 ) ) ;;
    }
     return perfectSquares ;;
}
public void maxPairSum ( arr ) {
    n = len ( arr ) ;;
    max = 0 ;;
    secondMax = 0 ;;
    if (( arr { 0 } > arr { 1 } )) {
        max = arr { 0 } ;;
        secondMax = arr { 1 } ;;
    }
     else{
        max = arr { 1 } ;;
        secondMax = arr { 0 } ;;
    }
    for i in range ( 2 , n ) :
        if (( arr { i } > max )) {
            secondMax = max ;;
            max = arr { i } ;;
        }
         else if (( arr { i } > secondMax )){
            secondMax = arr { i } ;;
        }
    return ( max + secondMax ) ;;
}
public void countPairsWith ( n , perfectSquares , nums ) {
    count = 0 ;;
    for i in range ( len ( perfectSquares ) ) :
        temp = perfectSquares { i } - n ;;
        if (( temp > n and ( temp in nums ) )) {
            count += 1 ;;
        }
     return count ;;
}
public void countPairs ( arr ) {
    n = len ( arr ) ;;
    max = maxPairSum ( arr ) ;;
    perfectSquares = getPerfectSquares ( max ) ;;
    var nums = {} ;;
    for i in range ( n ) :
        nums . append ( arr { i } ) ;;
    var count = 0 ;;
    for i in range ( n ) :
        count += countPairsWith ( arr { i } , perfectSquares , nums ) ;;
    return count ;;
}
var arr = { 2 , 3 , 6 , 9 , 10 , 20 } ;;
System.out.println ( countPairs ( arr ) ) ;;
