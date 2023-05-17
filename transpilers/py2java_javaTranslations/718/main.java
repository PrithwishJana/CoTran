public void equivalentBase4 ( bin ) {
    if (( var bin == "00" )) {
        return 0;
    }
     if (( bin == "01" )) {
        return 1;
    }
     if (( bin == "10" )) {
        return 2;
    }
     if (( bin == "11" )) {
        return 3;
    }
 }
public void isDivisibleBy5 ( bin ) {
    l = len ( bin );
    if (( ( l % 2 ) == 1 )) {
        bin = '0' + bin;
    }
     odd_sum = 0;
    even_sum = 0;
    isOddDigit = 1;
    for i in range ( 0 , len ( bin ) , 2 ) :
        if (( isOddDigit )) {
            odd_sum += equivalentBase4 ( bin { i : i + 2 } );
        }
         else{
            even_sum += equivalentBase4 ( bin { i : i + 2 } );
        }
        isOddDigit = isOddDigit ^ 1;
    if (( abs ( odd_sum - even_sum ) % 5 == 0 )) {
        return "Yes";
    }
     else{
        return "No";
    }
}
if (__name__ == "__main__") {
    bin = "10000101001";
    System.out.println ( isDivisibleBy5 ( bin ) );
}
 