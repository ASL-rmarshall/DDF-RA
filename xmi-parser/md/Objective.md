
# Class: Objective




URI: [https://cdisc.org/DDF/USDMUML/Objective](https://cdisc.org/DDF/USDMUML/Objective)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<objectiveLevel%200..1-++[Objective&#124;objectiveDescription:string%20%3F;objectiveId:string%20%3F],[Endpoint]<objectiveEndpoints%200..*-++[Objective],[StudyDesign]++-%20studyObjectives%200..*>[Objective],[StudyDesign],[Endpoint],[Code])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<objectiveLevel%200..1-++[Objective&#124;objectiveDescription:string%20%3F;objectiveId:string%20%3F],[Endpoint]<objectiveEndpoints%200..*-++[Objective],[StudyDesign]++-%20studyObjectives%200..*>[Objective],[StudyDesign],[Endpoint],[Code])

## Referenced by Class

 *  **None** *[➞studyObjectives](studyDesign__studyObjectives.md)*  <sub>0..\*</sub>  **[Objective](Objective.md)**

## Attributes


### Own

 * [➞objectiveDescription](objective__objectiveDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞objectiveEndpoints](objective__objectiveEndpoints.md)  <sub>0..\*</sub>
     * Range: [Endpoint](Endpoint.md)
 * [➞objectiveId](objective__objectiveId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞objectiveLevel](objective__objectiveLevel.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
