
# Class: StudyIdentifier




URI: [https://cdisc.org/DDF/USDMUML/StudyIdentifier](https://cdisc.org/DDF/USDMUML/StudyIdentifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization]<studyIdentifierScope%200..1-++[StudyIdentifier&#124;studyIdentifier:string%20%3F;studyIdentifierId:string%20%3F],[Study]++-%20studyIdentifiers%200..*>[StudyIdentifier],[Study],[Organization])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization]<studyIdentifierScope%200..1-++[StudyIdentifier&#124;studyIdentifier:string%20%3F;studyIdentifierId:string%20%3F],[Study]++-%20studyIdentifiers%200..*>[StudyIdentifier],[Study],[Organization])

## Referenced by Class

 *  **None** *[➞studyIdentifiers](study__studyIdentifiers.md)*  <sub>0..\*</sub>  **[StudyIdentifier](StudyIdentifier.md)**

## Attributes


### Own

 * [➞studyIdentifier](studyIdentifier__studyIdentifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyIdentifierId](studyIdentifier__studyIdentifierId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyIdentifierScope](studyIdentifier__studyIdentifierScope.md)  <sub>0..1</sub>
     * Range: [Organization](Organization.md)
