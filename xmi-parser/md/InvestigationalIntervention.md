
# Class: InvestigationalIntervention




URI: [https://cdisc.org/DDF/USDMUML/InvestigationalIntervention](https://cdisc.org/DDF/USDMUML/InvestigationalIntervention)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<codes%200..*-++[InvestigationalIntervention&#124;interventionDescription:string%20%3F;investigationalInterventionId:string%20%3F],[Estimand]++-%20treatment%200..1>[InvestigationalIntervention],[StudyDesign]++-%20studyInvestigationalInterventions%200..*>[InvestigationalIntervention],[StudyDesign],[Estimand],[Code])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<codes%200..*-++[InvestigationalIntervention&#124;interventionDescription:string%20%3F;investigationalInterventionId:string%20%3F],[Estimand]++-%20treatment%200..1>[InvestigationalIntervention],[StudyDesign]++-%20studyInvestigationalInterventions%200..*>[InvestigationalIntervention],[StudyDesign],[Estimand],[Code])

## Referenced by Class

 *  **None** *[➞treatment](estimand__treatment.md)*  <sub>0..1</sub>  **[InvestigationalIntervention](InvestigationalIntervention.md)**
 *  **None** *[➞studyInvestigationalInterventions](studyDesign__studyInvestigationalInterventions.md)*  <sub>0..\*</sub>  **[InvestigationalIntervention](InvestigationalIntervention.md)**

## Attributes


### Own

 * [➞codes](investigationalIntervention__codes.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
 * [➞interventionDescription](investigationalIntervention__interventionDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞investigationalInterventionId](investigationalIntervention__investigationalInterventionId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
