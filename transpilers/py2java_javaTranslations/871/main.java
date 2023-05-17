public void convert12 ( str ) {
    var h1 = ord ( str { 0 } ) - ord ( '0' ) ;;
    var h2 = ord ( str { 1 } ) - ord ( '0' ) ;;
    var hh = h1 * 10 + h2 ;;
    Meridien = "" ;;
    if (( hh < 12 )) {
        Meridien = "AM" ;;
    }
     else{
        Meridien = "PM" ;;
    }
    hh %= 12 ;;
    if (( hh == 0 )) {
        System.out.println ( "12" , var end = "" ) ;;
        for i in range ( 2 , 8 ) :
            System.out.println ( str { i } , end = "" ) ;;
    }
     else{
        System.out.println ( hh , end = "" ) ;;
        for i in range ( 2 , 8 ) :
            System.out.println ( str { i } , end = "" ) ;;
    }
    System.out.println ( " " + Meridien ) ;;
}
if (var __name__ == '__main__') {
    var str = "17:35:20" ;;
    convert12 ( str ) ;;
}
 