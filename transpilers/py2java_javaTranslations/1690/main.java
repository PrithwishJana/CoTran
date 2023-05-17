while (true) {
    d , var w = map ( int , input ( ) . split ( ) );
    if d + w == 0 : break;
    var pond = { list ( map ( int , input ( ) . split ( ) ) ) for _ in range ( d ) };
    ans = 0;
    for left in range ( w - 1 ) :
        for right in range ( w - 1 , left + 1 , - 1 ) :
            for top in range ( d - 1 ) :
                for under in range ( d - 1 , top + 1 , - 1 ) :
                    outh = 10;
                    outh = min ( outh , min ( pond { top } { left : right + 1 } ) );
                    outh = min ( outh , min ( pond { under } { left : right + 1 } ) );
                    zpond = list ( zip ( * pond ) );
                    var outh = min ( outh , min ( zpond { left } { top : under } ) );
                    outh = min ( outh , min ( zpond { right } { top : under } ) );
                    var pondh = 0;
                    for i in range ( top + 1 , under ) :
                        pondh = max ( pondh , max ( pond { i } { left + 1 : right } ) );
                    if (pondh < outh) {
                        var cap = outh * ( under - top - 1 ) * ( right - left - 1 ) - sum ( sum ( pond { i } { left + 1 : right } ) for i in range ( top + 1 , under ) );
                        var ans = max ( cap , ans );
                    }
     System.out.println ( ans );
}
 