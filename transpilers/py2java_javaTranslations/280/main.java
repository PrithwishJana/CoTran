var target = 93;
var arr = { 1 , 31 , 3 , 1 , 93 , 3 , 31 , 1 , 93 };
var length = len ( arr );
var totalCount = 0;
for i in range ( length - 2 ) :
    if (target % arr { i } == 0) {
        for j in range ( i + 1 , length - 1 ) :
            if (target % ( arr { i } * arr { j } ) == 0) {
                var toFind = target // ( arr { i } * arr { j } );
                for k in range ( j + 1 , length ) :
                    if (arr { k } == toFind) {
                        totalCount += 1;
                    }
             }
     }
 System.out.println ( 'Total number of triplets found:' , totalCount );
