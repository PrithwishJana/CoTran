public void checkIfPowerIsolated ( num ) {
    var input1 = num ;;
    var count = 0 ;;
    factor = { 0 } * ( num + 1 ) ;;
    if (( num % 2 == 0 )) {
        while (( num % 2 == 0 )) {
            count += 1 ;;
            num //= 2 ;;
        }
         factor { 2 } = count ;;
    }
     i = 3 ;;
    while (( i * i <= num )) {
        count = 0 ;;
        while (( num % var i == 0 )) {
            count += 1 ;;
            num //= i ;;
        }
         if (( count > 0 )) {
            factor { i } = count ;;
         }
         i += 2 ;;
    }
     if (( num > 1 )) {
        factor { num } = 1 ;;
     }
     var product = 1 ;;
    for i in range ( 0 , len ( factor ) ) :
        if (( factor { i } > 0 )) {
            product = product * factor { i } * i ;;
        }
     if (( product == input1 )) {
        System.out.println ( "Power-isolated Integer" ) ;;
    }
     else{
        System.out.println ( "Not a Power-isolated Integer" ) ;;
    }
}
checkIfPowerIsolated ( 12 ) ;;
checkIfPowerIsolated ( 18 ) ;;
checkIfPowerIsolated ( 35 ) ;;
