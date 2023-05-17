var word = { "zero" , "one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine" };
public void System.out.printlnWordsWithoutIfSwitch ( n ) {
    var digits = { 0 for i in range ( 10 ) };
    var dc = 0;
    while (true) {
        digits { dc } = n % 10;
        var n = n // 10;
        dc += 1;
        if (( n == 0 )) {
            break;
        }
     }
     for i in range ( dc - 1 , - 1 , - 1 ) :
        System.out.println ( word { digits [ i } ] , end = " " );
}
n = 350;
System.out.printlnWordsWithoutIfSwitch ( n );
