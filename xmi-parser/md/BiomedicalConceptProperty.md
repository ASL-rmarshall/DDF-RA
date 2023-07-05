
# Class: BiomedicalConceptProperty




URI: [https://cdisc.org/DDF/USDMUML/BiomedicalConceptProperty](https://cdisc.org/DDF/USDMUML/BiomedicalConceptProperty)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ResponseCode],[ResponseCode]<bcPropertyResponseCodes%200..*-++[BiomedicalConceptProperty&#124;bcPropertyDatatype:string%20%3F;bcPropertyEnabled:boolean%20%3F;bcPropertyId:string%20%3F;bcPropertyName:string%20%3F;bcPropertyRequired:boolean%20%3F],[AliasCode]<bcPropertyConceptCode%200..1-++[BiomedicalConceptProperty],[BiomedicalConcept]++-%20bcProperties%200..*>[BiomedicalConceptProperty],[BiomedicalConcept],[AliasCode])](https://yuml.me/diagram/nofunky;dir:TB/class/[ResponseCode],[ResponseCode]<bcPropertyResponseCodes%200..*-++[BiomedicalConceptProperty&#124;bcPropertyDatatype:string%20%3F;bcPropertyEnabled:boolean%20%3F;bcPropertyId:string%20%3F;bcPropertyName:string%20%3F;bcPropertyRequired:boolean%20%3F],[AliasCode]<bcPropertyConceptCode%200..1-++[BiomedicalConceptProperty],[BiomedicalConcept]++-%20bcProperties%200..*>[BiomedicalConceptProperty],[BiomedicalConcept],[AliasCode])

## Referenced by Class

 *  **None** *[➞bcProperties](biomedicalConcept__bcProperties.md)*  <sub>0..\*</sub>  **[BiomedicalConceptProperty](BiomedicalConceptProperty.md)**

## Attributes


### Own

 * [➞bcPropertyConceptCode](biomedicalConceptProperty__bcPropertyConceptCode.md)  <sub>0..1</sub>
     * Range: [AliasCode](AliasCode.md)
 * [➞bcPropertyDatatype](biomedicalConceptProperty__bcPropertyDatatype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcPropertyEnabled](biomedicalConceptProperty__bcPropertyEnabled.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [➞bcPropertyId](biomedicalConceptProperty__bcPropertyId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcPropertyName](biomedicalConceptProperty__bcPropertyName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcPropertyRequired](biomedicalConceptProperty__bcPropertyRequired.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [➞bcPropertyResponseCodes](biomedicalConceptProperty__bcPropertyResponseCodes.md)  <sub>0..\*</sub>
     * Range: [ResponseCode](ResponseCode.md)
