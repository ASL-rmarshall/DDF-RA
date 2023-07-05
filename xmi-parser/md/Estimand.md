
# Class: Estimand




URI: [https://cdisc.org/DDF/USDMUML/Estimand](https://cdisc.org/DDF/USDMUML/Estimand)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[InvestigationalIntervention],[IntercurrentEvent],[Endpoint]<variableOfInterest%200..1-++[Estimand&#124;estimandId:string%20%3F;summaryMeasure:string%20%3F],[InvestigationalIntervention]<treatment%200..1-++[Estimand],[IntercurrentEvent]<intercurrentEvents%200..*-++[Estimand],[AnalysisPopulation]<analysisPopulation%200..1-++[Estimand],[StudyDesign]++-%20studyEstimands%200..*>[Estimand],[StudyDesign],[Endpoint],[AnalysisPopulation])](https://yuml.me/diagram/nofunky;dir:TB/class/[InvestigationalIntervention],[IntercurrentEvent],[Endpoint]<variableOfInterest%200..1-++[Estimand&#124;estimandId:string%20%3F;summaryMeasure:string%20%3F],[InvestigationalIntervention]<treatment%200..1-++[Estimand],[IntercurrentEvent]<intercurrentEvents%200..*-++[Estimand],[AnalysisPopulation]<analysisPopulation%200..1-++[Estimand],[StudyDesign]++-%20studyEstimands%200..*>[Estimand],[StudyDesign],[Endpoint],[AnalysisPopulation])

## Referenced by Class

 *  **None** *[➞studyEstimands](studyDesign__studyEstimands.md)*  <sub>0..\*</sub>  **[Estimand](Estimand.md)**

## Attributes


### Own

 * [➞analysisPopulation](estimand__analysisPopulation.md)  <sub>0..1</sub>
     * Range: [AnalysisPopulation](AnalysisPopulation.md)
 * [➞estimandId](estimand__estimandId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞intercurrentEvents](estimand__intercurrentEvents.md)  <sub>0..\*</sub>
     * Range: [IntercurrentEvent](IntercurrentEvent.md)
 * [➞summaryMeasure](estimand__summaryMeasure.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞treatment](estimand__treatment.md)  <sub>0..1</sub>
     * Range: [InvestigationalIntervention](InvestigationalIntervention.md)
 * [➞variableOfInterest](estimand__variableOfInterest.md)  <sub>0..1</sub>
     * Range: [Endpoint](Endpoint.md)
