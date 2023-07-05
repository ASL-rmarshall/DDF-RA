
# Class: Organization




URI: [https://cdisc.org/DDF/USDMUML/Organization](https://cdisc.org/DDF/USDMUML/Organization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<organizationType%200..1-++[Organization&#124;organizationId:string%20%3F;organizationIdentifier:string%20%3F;organizationIdentifierScheme:string%20%3F;organizationName:string%20%3F],[Address]<organizationLegalAddress%200..1-++[Organization],[StudyIdentifier]++-%20studyIdentifierScope%200..1>[Organization],[StudyIdentifier],[Code],[Address])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<organizationType%200..1-++[Organization&#124;organizationId:string%20%3F;organizationIdentifier:string%20%3F;organizationIdentifierScheme:string%20%3F;organizationName:string%20%3F],[Address]<organizationLegalAddress%200..1-++[Organization],[StudyIdentifier]++-%20studyIdentifierScope%200..1>[Organization],[StudyIdentifier],[Code],[Address])

## Referenced by Class

 *  **None** *[➞studyIdentifierScope](studyIdentifier__studyIdentifierScope.md)*  <sub>0..1</sub>  **[Organization](Organization.md)**

## Attributes


### Own

 * [➞organizationId](organization__organizationId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞organizationIdentifier](organization__organizationIdentifier.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞organizationIdentifierScheme](organization__organizationIdentifierScheme.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞organizationLegalAddress](organization__organizationLegalAddress.md)  <sub>0..1</sub>
     * Range: [Address](Address.md)
 * [➞organizationName](organization__organizationName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞organizationType](organization__organizationType.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
