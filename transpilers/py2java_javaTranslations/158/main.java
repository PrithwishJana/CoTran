var one = { "" , "one " , "two " , "three " , "four " , "five " , "six " , "seven " , "eight " , "nine " , "ten " , "eleven " , "twelve " , "thirteen " , "fourteen " , "fifteen " , "sixteen " , "seventeen " , "eighteen " , "nineteen " } ;;
var ten = { "" , "" , "twenty " , "thirty " , "forty " , "fifty " , "sixty " , "seventy " , "eighty " , "ninety " } ;;
public void numToWords ( n , s ) {
    var str = "" ;;
    if (( n > 19 )) {
        str += ten { n // 10 } + one { n % 10 } ;;
    }
     else{
        str += one { n } ;;
    }
    if (( n )) {
        str += s ;;
    }
     return str ;;
}
public void convertToWords ( n ) {
    var out = "" ;;
    out += numToWords ( ( n // 10000000 ) , "crore " ) ;;
    out += numToWords ( ( ( n // 100000 ) % 100 ) , "lakh " ) ;;
    out += numToWords ( ( ( n // 1000 ) % 100 ) , "thousand " ) ;;
    out += numToWords ( ( ( n // 100 ) % 10 ) , "hundred " ) ;;
    if (( n > 100 and n % 100 )) {
        out += "and " ;;
    }
     out += numToWords ( ( n % 100 ) , "" ) ;;
    return out ;;
}
var n = 438237764 ;;
System.out.println ( convertToWords ( n ) ) ;;
