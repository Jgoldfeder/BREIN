﻿// Experiment One from twoi plus LIF to twoi
#ExperimentOne[0] |=  $TwoiPlusLif "Exp1 initial expression pattern";
#ExperimentOne[0] |=  $TwoiCultureConditions "Exp1 culture conditions";
#ExperimentOne[0] |=  $NoKnockDowns "Exp1 no knockdowns"; 
#ExperimentOne[0] |=  $NoOverExpression "Exp1 no overexpression";
#ExperimentOne[18] |=  $Twoi "Exp1 penultimate state";
#ExperimentOne[19] |=  $Twoi "Exp1 final state";

// Experiment Two from twoi to twoi plus LIF
#ExperimentTwo[0] |=  $Twoi "Exptwo initial expression pattern"; 
#ExperimentTwo[0] |=  $TwoiPlusLifCultureConditions "Exptwo culture conditions";
#ExperimentTwo[0] |=  $NoKnockDowns "Exptwo no knockdowns"; 
#ExperimentTwo[0] |=  $NoOverExpression "Exptwo no overexpression";
#ExperimentTwo[18] |=  $TwoiPlusLif  "Exptwo penultimate state";
#ExperimentTwo[19] |=  $TwoiPlusLif "Exptwo final state";


// Experiment Three from twoi plus LIF to LIF plus PD
#ExperimentThree[0] |=  $TwoiPlusLif "Exp3 initial expression pattern";
#ExperimentThree[0] |=  $LifPlusPdCultureConditions "Exp3 culture conditions";
#ExperimentThree[0] |=  $NoKnockDowns "Exp3 knockdowns"; 
#ExperimentThree[0] |=  $NoOverExpression "Exp3 no overexpression";
#ExperimentThree[18] |=  $LifPlusPd  "Exp3 penultimate state";
#ExperimentThree[19] |=  $LifPlusPd "Exp3 final state";


// Experiment Four from LIF plus PD to twoi plus LIF
#ExperimentFour[0] |=  $LifPlusPd "Exp4 initial expression pattern";
#ExperimentFour[0] |=  $TwoiPlusLifCultureConditions "Exp4 culture conditions";
#ExperimentFour[0] |=  $NoKnockDowns "Exp4 no knockdowns"; 
#ExperimentFour[0] |=  $NoOverExpression "Exp4 no overexpression";
#ExperimentFour[18] |=  $TwoiPlusLif  "Exp4 penultimate state";
#ExperimentFour[19] |=  $TwoiPlusLif "Exp4 final state";


// Experiment Five from twoi plus LIF to LIF plus CH
#ExperimentFive[0] |=  $TwoiPlusLif "Exp5 initial expression pattern";
#ExperimentFive[0] |=  $LifPlusChCultureConditions "Exp5 culture conditions";
#ExperimentFive[0] |=  $NoKnockDowns "Exp5 no knockdowns";  
#ExperimentFive[0] |=  $NoOverExpression "Exp5 no overexpression";
#ExperimentFive[18] |=  $LifPlusCh  "Exp5 penultimate state";
#ExperimentFive[19] |=  $LifPlusCh "LIF plus CH final state Exp 5";


// Experiment Six from LIF plus CH to twoi plus LIF
#ExperimentSix[0] |=  $LifPlusCh "Exp6 initial expression pattern";
#ExperimentSix[0] |=  $TwoiPlusLifCultureConditions "Exp6 culture conditions";
#ExperimentSix[0] |=  $NoKnockDowns "Exp6 no knockdowns";  
#ExperimentSix[0] |=  $NoOverExpression "Exp6 no overexpression";
#ExperimentSix[18] |=  $TwoiPlusLif  "Exp6 penultimate state";
#ExperimentSix[19] |=  $TwoiPlusLif "Exp6 final state";


// Experiment Seven from twoi to LIF plus PD
#ExperimentSeven[0] |=  $Twoi "Exp7 initial expression pattern";
#ExperimentSeven[0] |=  $LifPlusPdCultureConditions "Exp7 culture conditions";
#ExperimentSeven[0] |=  $NoKnockDowns "Exp7 no knockdowns";  
#ExperimentSeven[0] |=  $NoOverExpression "Exp7 no overexpression";
#ExperimentSeven[18] |=  $LifPlusPd  "Exp7 penultimate state";
#ExperimentSeven[19] |=  $LifPlusPd "Exp7 final state";


// Experiment Eight from LIF plus PD to twoi 
#ExperimentEight[0] |=  $LifPlusPd "Exp8 initial expression pattern";
#ExperimentEight[0] |=  $TwoiCultureConditions "Exp8 culture conditions";
#ExperimentEight[0] |=  $NoKnockDowns "Exp8 no knockdowns";  
#ExperimentEight[0] |=  $NoOverExpression "Exp8 no overexpression";
#ExperimentEight[18] |=  $Twoi  "Exp 8 penultimate state";
#ExperimentEight[19] |=  $Twoi "Exp8 final state";


// Experiment Nine from twoi to LIF plus CH
#ExperimentNine[0] |=  $Twoi "Exp9 initial expression pattern";
#ExperimentNine[0] |=  $LifPlusChCultureConditions "Exp9 culture conditions";
#ExperimentNine[0] |=  $NoKnockDowns "Exp9 no knockdowns";  
#ExperimentNine[0] |=  $NoOverExpression "Exp9 no overexpression";
#ExperimentNine[18] |=  $LifPlusCh  "Exp9 penultimate state";
#ExperimentNine[19] |=  $LifPlusCh "Exp9 final state";

// Experiment Ten from LIF plus CH to twoi 
#ExperimentTen[0] |=  $LifPlusCh "Exp 10 initial expression state";
#ExperimentTen[0] |=  $TwoiCultureConditions "Exp10 culture conditions";
#ExperimentTen[0] |=  $NoKnockDowns "Exp10 no knockdowns";  
#ExperimentTen[0] |=  $NoOverExpression "Exp10 no overexpression";
#ExperimentTen[18] |=  $Twoi "Exp10 penultimate state";
#ExperimentTen[19] |=  $Twoi "Exp10 final state";


// Experiment Eleven from LIF plus CH to LIF plus PD
#ExperimentEleven[0] |=  $LifPlusCh "Exp11 initial expression pattern";
#ExperimentEleven[0] |=  $LifPlusPdCultureConditions "Exp11 culture conditions";
#ExperimentEleven[0] |=  $NoKnockDowns "Exp11 no knockdowns";  
#ExperimentEleven[0] |=  $NoOverExpression "Exp11 no overexpression";
#ExperimentEleven[18] |=  $LifPlusPd  "Exp11 penultimate state";
#ExperimentEleven[19] |=  $LifPlusPd "Exp11 final state";


// Experiment Twelve from LIF plus PD to LIF plus CH
#ExperimentTwelve[0] |=  $LifPlusPd "Exp1two initial expression pattern";
#ExperimentTwelve[0] |=  $LifPlusChCultureConditions "Exp1two culture conditions";
#ExperimentTwelve[0] |=  $NoKnockDowns "Exp1two no knockdowns";  
#ExperimentTwelve[0] |=  $NoOverExpression "Exp1two no overexpression";
#ExperimentTwelve[18] |=  $LifPlusCh "Exp1two penultimate state";
#ExperimentTwelve[19] |=  $LifPlusCh "Exp1two final state";

// Experiment Thirteen from LIF plus twoi to no signal
#ExperimentThirteen[0] |=  $TwoiPlusLif "Exp1two initial expression pattern";
#ExperimentThirteen[0] |=  $NoSignalCultureConditions "Exp13 culture conditions";
#ExperimentThirteen[0] |=  $NoKnockDowns "Exp13 no knockdowns"; 
#ExperimentThirteen[0] |=  $NoOverExpression "Exp13 no overexpression";
#ExperimentThirteen[18] |=  $NoSignal "Exp13 penultimate state";
#ExperimentThirteen[19] |=  $NoSignal "Exp13 final state";

// Experiment Fourteen from twoi to no signal
#ExperimentFourteen[0] |=  $Twoi "Exp14 initial expression pattern";
#ExperimentFourteen[0] |=  $NoSignalCultureConditions "Exp14 culture conditions";
#ExperimentFourteen[0] |=  $NoKnockDowns "Exp14 no knockdowns";  
#ExperimentFourteen[0] |=  $NoOverExpression "Exp14 no overexpression";
#ExperimentFourteen[18] |=  $NoSignal "Exp14 penultimate state";
#ExperimentFourteen[19] |=  $NoSignal "Exp14 final state";

// Experiment Fifteen from LIF plus PD to no signal
#ExperimentFifteen[0] |=  $LifPlusPd "Exp15 initial expression pattern";
#ExperimentFifteen[0] |=  $NoSignalCultureConditions "Exp15 culture conditions";
#ExperimentFifteen[0] |=  $NoKnockDowns "Exp15 no knockdowns";  
#ExperimentFifteen[0] |=  $NoOverExpression "Exp15 no overexpression";
#ExperimentFifteen[18] |=  $NoSignal "Exp15 penultimate state";
#ExperimentFifteen[19] |=  $NoSignal "Exp15 final state";

// Experiment Sixteen from twoi Oct4 Knockdown to everything repressed
#ExperimentSixteen[0] |=  $TwoiOctFourKnockout "Exp16 initial expression pattern";
#ExperimentSixteen[0] |=  $TwoiCultureConditions "Exp16 culture conditions";
#ExperimentSixteen[0] |=  $Oct4GeneKnockDown "Exp16 Oct4 knockdown";  
#ExperimentSixteen[0] |=  $NoOverExpression "Exp16 no overexpression";
#ExperimentSixteen[18] |=  $FinalStateAllZeroExpression "Exp16 penultimate state";
#ExperimentSixteen[19] |=  $FinalStateAllZeroExpression "Exp16 final state";

// Experiment Seventeen from twoi Soxtwo Knockdown to everything repressed
#ExperimentSeventeen[0] |=  $TwoiSoxTwoKnockout "Exp17 initial expression pattern";
#ExperimentSeventeen[0] |=  $TwoiCultureConditions "Exp17 culture conditions";
#ExperimentSeventeen[0] |=  $SoxtwoGeneKnockDown "Exp17 Soxtwo knockdown";  
#ExperimentSeventeen[0] |=  $NoOverExpression "Exp17 no overexpression";
#ExperimentSeventeen[18] |=  $FinalStateAllZeroExpression "Exp17 penultimate state";
#ExperimentSeventeen[19] |=  $FinalStateAllZeroExpression "Exp17 final state";

// Experiment Eighteen from twoi Stat3 Knockdown to everything repressed
#ExperimentEighteen[0] |=  $twoiStatThreeKnockout "Exp18 initial expression pattern";
#ExperimentEighteen[0] |=  $LifPlusPdCultureConditions "Exp18 culture conditions";
#ExperimentEighteen[0] |=  $Stat3GeneKnockDown "Exp18 Stat3 knockdown";  
#ExperimentEighteen[0] |=  $NoOverExpression "Exp18 no overexpression";
#ExperimentEighteen[18] |=  $FinalStateAllZeroExpression "Exp18 penultimate state";
#ExperimentEighteen[19] |=  $FinalStateAllZeroExpression "Exp18 final state";

// Experiment Nineteen from twoi Esrrb Knockdown to everything repressed
#ExperimentNineteen[0] |=  $twoiEsrrbKnockout "Exp19 initial expression pattern";
#ExperimentNineteen[0] |=  $TwoiCultureConditions "Exp19 culture conditions";
#ExperimentNineteen[0] |=  $EsrrbGeneKnockDown "Exp19 Esrrb knockdown";  
#ExperimentNineteen[0] |=  $NoOverExpression "Exp19 no overexpression";
#ExperimentNineteen[18] |=  $FinalStateAllZeroExpression "Exp19 penultimate state";
#ExperimentNineteen[19] |=  $FinalStateAllZeroExpression "Exp19 final state";

// Experiment Twenty from twoi plus LIF Esrrb Knockdown 
#ExperimentTwenty[0] |=  $twoiPlusLifEsrrbKnockout "Exptwo0 initial expression pattern";
#ExperimentTwenty[0] |=  $TwoiPlusLifCultureConditions "Exptwo0 culture conditions";
#ExperimentTwenty[0] |=  $EsrrbGeneKnockDown "Exptwo0 Esrrb knockdown";  
#ExperimentTwenty[0] |=  $NoOverExpression "Exptwo0 no overexpression";
#ExperimentTwenty[18] |=  $FinalStatetwoiPlusLifEsrrbKnockout "Exptwo0 penultimate state";
#ExperimentTwenty[19] |=  $FinalStatetwoiPlusLifEsrrbKnockout "Exptwo0 final state";

// Experiment Twenty One overexpression of Esrrb from twoi to just PD
#ExperimentTwentyOne[0] |=  $twoiEsrrbOverexpression "Exptwo1 initial expression pattern";
#ExperimentTwentyOne[0] |=  $JustPdCultureConditions "Exptwo1 culture conditions";
#ExperimentTwentyOne[0] |=  $NoKnockDowns "Exptwo1 no knockdowns";  
#ExperimentTwentyOne[0] |=  $EsrrbGeneOverExpression "Exptwo1 no overexpression";
#ExperimentTwentyOne[18] |=  $FinalStatePdOnlyEsrrbOverexpression "Exptwo1 penultimate state";
#ExperimentTwentyOne[19] |=  $FinalStatePdOnlyEsrrbOverexpression "Exptwo1 final state";

// Experiment Twenty Two Nanog knockdown in twoi plus lIF
#ExperimentTwentyTwo[0] |=  $twoiPlusLifNanogKnockdown "Exptwotwo initial expression pattern";
#ExperimentTwentyTwo[0] |=  $TwoiPlusLifCultureConditions "Exptwotwo culture conditions";
#ExperimentTwentyTwo[0] |=  $NanogKnockDown "Exptwotwo Nanog knockdown";
#ExperimentTwentyTwo[0] |=  $NoOverExpression "Exp twotwo no overexpression";
#ExperimentTwentyTwo[18] |=  $FinalStateNanogKnockout "Exptwotwo penultimate state";
#ExperimentTwentyTwo[19] |=  $FinalStateNanogKnockout "Exptwotwo final state";

// Experiment Twenty Three overexpression of Tfcptwol1 in twoi plus LIF
#ExperimentTwentyThree[0] |=  $twoiPlusLifTfcptwol1Overexpression "Exptwo3 initial expression pattern";
#ExperimentTwentyThree[0] |=  $JustPdCultureConditions "Exptwo3 culture conditions";
#ExperimentTwentyThree[0] |=  $NoKnockDowns "Exptwo3 no knockdowns";
#ExperimentTwentyThree[0] |=  $Tfcptwol1GeneOverExpression "Exptwo3 Tfcptwol1 overexpression";
#ExperimentTwentyThree[18] |=  $FinalStateTfcptwol1Overexpression "Exptwo3 penultimate state";
#ExperimentTwentyThree[19] |=  $FinalStateTfcptwol1Overexpression "Exp two3 final state";

// Culture conditions 

$TwoiPlusLifCultureConditions :=
{
 LIF = 1 and
 CH = 1 and 
 PD = 1
};

$TwoiCultureConditions :=
{
 LIF = 0 and
 CH = 1 and
 PD = 1
};

$LifPlusPdCultureConditions :=
{
 LIF = 1 and 
 CH = 0 and 
 PD = 1
};

$LifPlusChCultureConditions :=
{
 LIF = 1 and
 CH = 1 and 
 PD = 0
};

$NoSignalCultureConditions :=
{
 LIF = 0 and
 CH = 0 and 
 PD = 0
};

$JustPdCultureConditions :=
{
 LIF = 0 and
 CH = 0 and 
 PD = 1
};

// Knock downs and overexpressions

$NoKnockDowns :=
{
 KO(Oct4)=0 and
 KO(Soxtwo)=0 and
 KO(Esrrb)=0 and
 KO(Stat3)=0 and
 KO(Nanog)=0
};

$Oct4GeneKnockDown :=
{
 KO(Oct4)=1 and
 KO(Soxtwo)=0 and
 KO(Esrrb)=0 and
 KO(Stat3)=0 and
 KO(Nanog)=0
};

$SoxtwoGeneKnockDown :=
{
 KO(Oct4)=0 and
 KO(Soxtwo)=1 and
 KO(Esrrb)=0 and
 KO(Stat3)=0 and
 KO(Nanog)=0
};

$Stat3GeneKnockDown :=
{
 KO(Oct4)=0 and
 KO(Soxtwo)=0 and
 KO(Esrrb)=0 and
 KO(Stat3)=1 and
 KO(Nanog)=0
};

$EsrrbGeneKnockDown :=
{
 KO(Oct4)=0 and
 KO(Soxtwo)=0 and
 KO(Esrrb)=1 and
 KO(Stat3)=0 and
 KO(Nanog)=0
};

$NanogKnockDown :=
{
 KO(Oct4)=0 and
 KO(Soxtwo)=0 and
 KO(Esrrb)=0 and
 KO(Stat3)=0 and
 KO(Nanog)=1
};

$NoOverExpression :=
{
 FE(Esrrb)=0 and
 FE(Tfcptwol1)=0
};

$EsrrbGeneOverExpression :=
{
 FE(Esrrb)=1 and 
 FE(Tfcptwol1)=0
};

$Tfcptwol1GeneOverExpression:=
{
 FE(Esrrb)=0 and
 FE(Tfcptwol1)=1 
};


// Gene expression levels patterns under each culture condition 

$TwoiPlusLif:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=1
};

$Twoi:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=0 and
 Gbxtwo=0 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=0
};

$LifPlusPd:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=0 and
 Klftwo=1 and
 Tfcptwol1=0 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=0 and
 Tcf3=1 and
 Sall4=0 and
 Stat3=1
};

$LifPlusCh:=
{
 MEKERK = 1 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=1
};

$NoSignal:=
{
 MEKERK = 1 and
 Oct4=0 and
 Soxtwo=0 and
 Nanog=0 and
 Esrrb=0 and
 Klftwo=0 and
 Gbxtwo = 0 and 
 Tfcptwol1=0 and
 Klf4=0 and
 Tbx3=0 and
 Sall4=0 and
 Stat3=0
};

// Twoi conditions with Oct4 knockout
$TwoiOctFourKnockout:=
{
 MEKERK = 0 and
 Oct4=0 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=0 and
 Gbxtwo=0 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=0
};

// Twoi conditions with Soxtwo knockout
$TwoiSoxTwoKnockout:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=0 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=0 and
 Gbxtwo=0 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=0
};

// LIF plus PD conditions with Stat3 knockout
$twoiStatThreeKnockout :=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=0 and
 Gbxtwo=0 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=0
};
 
$FinalStateAllZeroExpression:=
{
 MEKERK = 0 and
 Oct4=0 and
 Soxtwo=0 and
 Nanog=0 and
 Esrrb=0 and
 Klftwo=0 and
 Gbxtwo=0 and 
 Tfcptwol1=0 and
 Klf4=0 and
 Tbx3=0 and
 Sall4=0 and
 Stat3=0
};

$twoiEsrrbKnockout:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=0 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=0 and
 Gbxtwo=0 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=0
};

$twoiPlusLifEsrrbKnockout:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=0 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=1
};

$FinalStatetwoiPlusLifEsrrbKnockout:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=0 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=1
};

// Twoi conditions with esrrb overexpression
$twoiEsrrbOverexpression :=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=0 and
 Gbxtwo=0 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=0
};

// Only PD
$FinalStatePdOnlyEsrrbOverexpression:=
{
 Oct4 = 1 and 
 Soxtwo = 1 and 
 Nanog = 1 and
 Esrrb = 1 and
 Klf4 = 0
};

// Nanog knock down in twoi plus LIF
$twoiPlusLifNanogKnockdown:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=0 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=1
};

// Final state
$FinalStateNanogKnockout:=
{
 Oct4=1 and
 Soxtwo=1 and
 Nanog=0 and
 Tbx3=1 and
 Esrrb=0
};

// Initial state Tfcptwol1 overexpression in twoi plus LIF
$twoiPlusLifTfcptwol1Overexpression:=
{
 MEKERK = 0 and
 Oct4=1 and
 Soxtwo=1 and
 Nanog=1 and
 Esrrb=1 and
 Klftwo=1 and
 Tfcptwol1=1 and
 Klf4=1 and
 Gbxtwo=1 and
 Tbx3=1 and
 Tcf3=0 and
 Sall4=1 and
 Stat3=1
};

// Final state Tfcptwol1 overexpression
$FinalStateTfcptwol1Overexpression:=
{
 Oct4=1 and
 Soxtwo=1 and 
 Nanog=1 and 
 Esrrb=1 and 
 Klf4=0
};