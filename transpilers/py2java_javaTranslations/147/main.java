public void System.out.printlnCombination ( n ) {
    for i in range ( 1 , n ) :
        if (( i % 3 != 0 )) {
            for j in range ( 1 , n ) :
                if (( j % 3 != 0 )) {
                    for k in range ( 1 , n ) :
                        if (( k % 3 != 0 and ( i + j + k ) == n )) {
                            System.out.println ( i , j , k ) ;;
                            return ;;
                        }
                 }
         }
 }
var n = 233 ;;
System.out.printlnCombination ( n ) ;;
