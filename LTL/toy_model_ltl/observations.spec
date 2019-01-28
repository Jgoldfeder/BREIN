﻿// Observation predicates
$Conditions1 := { S1 = 0 and S2 = 1};
$Conditions2 := { S1 = 1 and S2 = 1};
$Expression1 := {A = 1 and B = 1 and C = 1};
$Expression2 := {A = 0 and B = 1 and C = 1};

// Observations
#Experiment1 |= $Conditions1;
#Experiment1|= $Expression1;
F (G(#Experiment1 |= $Expression2));

#Experiment2 |= $Conditions2;
#Experiment2 |= $Expression2;
F (G(#Experiment2 |= $Expression1));
