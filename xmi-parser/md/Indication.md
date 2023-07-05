
# Class: Indication




URI: [https://cdisc.org/DDF/USDMUML/Indication](https://cdisc.org/DDF/USDMUML/Indication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<codes%200..*-++[Indication&#124;indicationDescription:string%20%3F;indicationId:string%20%3F],[StudyDesign]++-%20studyIndications%200..*>[Indication],[StudyDesign],[Code])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<codes%200..*-++[Indication&#124;indicationDescription:string%20%3F;indicationId:string%20%3F],[StudyDesign]++-%20studyIndications%200..*>[Indication],[StudyDesign],[Code])

## Referenced by Class

 *  **None** *[➞studyIndications](studyDesign__studyIndications.md)*  <sub>0..\*</sub>  **[Indication](Indication.md)**

## Attributes


### Own

 * [➞codes](indication__codes.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
 * [➞indicationDescription](indication__indicationDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞indicationId](indication__indicationId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
