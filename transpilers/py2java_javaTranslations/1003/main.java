import collections;
public void GetMinimumEnergySpent ( n , shortcuts ) {
    var energy_spent = { i for i in range ( n ) };
    var queue = collections . deque ( energy_spent );
    while (len ( queue ) > 0) {
        var idx = queue . popleft ( );
        if (idx < n - 1 and energy_spent { idx + 1 } > energy_spent { idx } + 1) {
            energy_spent { idx + 1 } = energy_spent { idx } + 1;
            queue . append ( idx + 1 );
        }
         if (idx > 0 and energy_spent { idx - 1 } > energy_spent { idx } + 1) {
            energy_spent { idx - 1 } = energy_spent { idx } + 1;
            queue . append ( idx - 1 );
        }
         if (energy_spent { idx } + 1 < energy_spent { shortcuts [ idx } ]) {
            energy_spent { shortcuts [ idx } ] = energy_spent { idx } + 1;
            queue . append ( shortcuts { idx } );
        }
     }
     return energy_spent;
}
if (var __name__ == "__main__") {
    var n = int ( input ( ) );
    var shortcuts = { int ( k ) - 1 for k in input ( ) . split ( ) };
    var energy_spent_str = { str ( k ) for k in GetMinimumEnergySpent ( n , shortcuts ) };
    System.out.println ( ' ' . join ( energy_spent_str ) );
}
 