
# Class: Study




URI: [https://cdisc.org/DDF/USDMUML/Study](https://cdisc.org/DDF/USDMUML/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyProtocolVersion],[StudyIdentifier],[StudyDesign],[Code]<studyType%200..1-++[Study&#124;studyAcronym:string%20%3F;studyId:string%20%3F;studyRationale:string%20%3F;studyTitle:string%20%3F;studyVersion:string%20%3F],[StudyProtocolVersion]<studyProtocolVersions%200..*-++[Study],[AliasCode]<studyPhase%200..1-++[Study],[StudyIdentifier]<studyIdentifiers%200..*-++[Study],[StudyDesign]<studyDesigns%200..*-++[Study],[Code]<businessTherapeuticAreas%200..*-++[Study],[Code],[AliasCode])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyProtocolVersion],[StudyIdentifier],[StudyDesign],[Code]<studyType%200..1-++[Study&#124;studyAcronym:string%20%3F;studyId:string%20%3F;studyRationale:string%20%3F;studyTitle:string%20%3F;studyVersion:string%20%3F],[StudyProtocolVersion]<studyProtocolVersions%200..*-++[Study],[AliasCode]<studyPhase%200..1-++[Study],[StudyIdentifier]<studyIdentifiers%200..*-++[Study],[StudyDesign]<studyDesigns%200..*-++[Study],[Code]<businessTherapeuticAreas%200..*-++[Study],[Code],[AliasCode])

## Attributes


### Own

 * [➞businessTherapeuticAreas](study__businessTherapeuticAreas.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
 * [➞studyAcronym](study__studyAcronym.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyDesigns](study__studyDesigns.md)  <sub>0..\*</sub>
     * Range: [StudyDesign](StudyDesign.md)
 * [➞studyId](study__studyId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyIdentifiers](study__studyIdentifiers.md)  <sub>0..\*</sub>
     * Range: [StudyIdentifier](StudyIdentifier.md)
 * [➞studyPhase](study__studyPhase.md)  <sub>0..1</sub>
     * Range: [AliasCode](AliasCode.md)
 * [➞studyProtocolVersions](study__studyProtocolVersions.md)  <sub>0..\*</sub>
     * Range: [StudyProtocolVersion](StudyProtocolVersion.md)
 * [➞studyRationale](study__studyRationale.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyTitle](study__studyTitle.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyType](study__studyType.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞studyVersion](study__studyVersion.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
