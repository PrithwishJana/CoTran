public void concentration ( water , suger ) {
    return 100 * suger / ( water + suger );
}
WATER_A , WATER_B , SUGER_C , SUGER_D , MELT_PER_100 , var LIMIT = map ( int , input ( ) . split ( ) );
WATER_A *= 100;
WATER_B *= 100;
MELT_PERCENT_LIMIT = concentration ( 100 , MELT_PER_100 );
var wa = wb = sc = sd = 0;
var water_set = set ( );
while (wa * WATER_A <= LIMIT) {
    while (wb * WATER_B <= LIMIT) {
        var water = wa * WATER_A + wb * WATER_B;
        if (water <= LIMIT) {
            water_set . add ( water );
        }
         wb += 1;
    }
     wb = 0;
    wa += 1;
}
 suger_set = set ( );
while (sc * SUGER_C <= LIMIT) {
    while (sd * SUGER_D <= LIMIT) {
        suger = sc * SUGER_C + sd * SUGER_D;
        if (suger <= LIMIT) {
            suger_set . add ( suger );
        }
         sd += 1;
    }
     sd = 0;
    sc += 1;
}
 ans_suger_water = 0;
ans_suger = 0;
max_concentration = 0;
for (int water = 0; water < water_set.length; water++){
    for (int suger = 0; suger < suger_set.length; suger++){
        if (not ( 0 < water + suger <= LIMIT )) {
            continue;
        }
         suger_precent = concentration ( water , suger );
        if (max_concentration <= suger_precent <= MELT_PERCENT_LIMIT) {
            max_concentration = suger_precent;
            ans_suger_water = water + suger;
            var ans_suger = suger;
        }
    }
}
 System.out.println ( ans_suger_water , ans_suger );
