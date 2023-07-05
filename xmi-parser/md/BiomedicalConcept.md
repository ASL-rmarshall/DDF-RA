
# Class: BiomedicalConcept




URI: [https://cdisc.org/DDF/USDMUML/BiomedicalConcept](https://cdisc.org/DDF/USDMUML/BiomedicalConcept)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BiomedicalConceptProperty],[BiomedicalConceptProperty]<bcProperties%200..*-++[BiomedicalConcept&#124;bcName:string%20%3F;bcReference:string%20%3F;bcSynonyms:string%20*;biomedicalConceptId:string%20%3F],[AliasCode]<bcConceptCode%200..1-++[BiomedicalConcept],[StudyDesign]++-%20biomedicalConcepts%200..*>[BiomedicalConcept],[StudyDesign],[AliasCode])](https://yuml.me/diagram/nofunky;dir:TB/class/[BiomedicalConceptProperty],[BiomedicalConceptProperty]<bcProperties%200..*-++[BiomedicalConcept&#124;bcName:string%20%3F;bcReference:string%20%3F;bcSynonyms:string%20*;biomedicalConceptId:string%20%3F],[AliasCode]<bcConceptCode%200..1-++[BiomedicalConcept],[StudyDesign]++-%20biomedicalConcepts%200..*>[BiomedicalConcept],[StudyDesign],[AliasCode])

## Referenced by Class

 *  **None** *[➞biomedicalConcepts](studyDesign__biomedicalConcepts.md)*  <sub>0..\*</sub>  **[BiomedicalConcept](BiomedicalConcept.md)**

## Attributes


### Own

 * [➞bcConceptCode](biomedicalConcept__bcConceptCode.md)  <sub>0..1</sub>
     * Range: [AliasCode](AliasCode.md)
 * [➞bcName](biomedicalConcept__bcName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcProperties](biomedicalConcept__bcProperties.md)  <sub>0..\*</sub>
     * Range: [BiomedicalConceptProperty](BiomedicalConceptProperty.md)
 * [➞bcReference](biomedicalConcept__bcReference.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcSynonyms](biomedicalConcept__bcSynonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞biomedicalConceptId](biomedicalConcept__biomedicalConceptId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
