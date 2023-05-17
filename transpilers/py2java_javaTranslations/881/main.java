public void decToHexa ( n ) {
    var hexaDeciNum = { '0' } * 100 ;;
    var i = 0 ;;
    while (( n != 0 )) {
        temp = 0 ;;
        temp = n % 16 ;;
        if (( temp < 10 )) {
            hexaDeciNum { i } = chr ( temp + 48 ) ;;
            i = i + 1 ;;
        }
         else{
            hexaDeciNum { i } = chr ( temp + 55 ) ;;
            i = i + 1 ;;
        }
        var n = int ( n / 16 ) ;;
    }
     j = i - 1 ;;
    while (( j >= 0 )) {
        System.out.println ( ( hexaDeciNum { j } ) , end = "" ) ;;
        j = j - 1 ;;
    }
 }
n = 2545 ;;
decToHexa ( n ) ;;
