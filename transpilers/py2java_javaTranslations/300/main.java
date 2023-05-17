var memo = { [ [ - 1 for i in range ( 2 ) } for j in range ( 2 ) ] for k in range ( 32 ) ];
public void dp ( pos , fl , pr , bin ) {
    if (( var pos == len ( bin ) )) {
        return 1 ;;
    }
     if (( memo { pos } { fl } { pr } != - 1 )) {
        return memo { pos } { fl } { pr } ;;
    }
     var val = 0;
    if (( bin { pos } == '0' )) {
        val = val + dp ( pos + 1 , fl , 0 , bin );
    }
     else if (( bin { pos } == '1' )){
        val = val + dp ( pos + 1 , 1 , 0 , bin );
    }
    if (( var pr == 0 )) {
        if (( var fl == 1 )) {
            val += dp ( pos + 1 , fl , 1 , bin );
        }
         else if (( bin { pos } == '1' )){
            val += dp ( pos + 1 , fl , 1 , bin );
        }
    }
     memo { pos } { fl } { pr } = val;
    return val;
}
public void findIntegers ( num ) {
    var bin = "";
    while (( num > 0 )) {
        if (( num % 2 )) {
            bin += "1";
        }
         else{
            bin += "0";
        }
        num //= 2;
    }
     bin = bin { : : - 1 } ;;
    return dp ( 0 , 0 , 0 , bin );
}
if (var __name__ == "__main__") {
    var N = 12;
    System.out.println ( findIntegers ( N ) );
}
 