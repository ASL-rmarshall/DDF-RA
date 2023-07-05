
# Class: AliasCode




URI: [https://cdisc.org/DDF/USDMUML/AliasCode](https://cdisc.org/DDF/USDMUML/AliasCode)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code],[Code]<standardCodeAliases%200..*-++[AliasCode&#124;aliasCodeId:string%20%3F],[Code]<standardCode%200..1-++[AliasCode],[BiomedicalConceptCategory]++-%20bcCategoryCode%200..1>[AliasCode],[BiomedicalConceptProperty]++-%20bcPropertyConceptCode%200..1>[AliasCode],[BiomedicalConcept]++-%20bcConceptCode%200..1>[AliasCode],[StudyDesign]++-%20studyDesignBlindingScheme%200..1>[AliasCode],[Study]++-%20studyPhase%200..1>[AliasCode],[StudyDesign],[Study],[BiomedicalConceptProperty],[BiomedicalConceptCategory],[BiomedicalConcept])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code],[Code]<standardCodeAliases%200..*-++[AliasCode&#124;aliasCodeId:string%20%3F],[Code]<standardCode%200..1-++[AliasCode],[BiomedicalConceptCategory]++-%20bcCategoryCode%200..1>[AliasCode],[BiomedicalConceptProperty]++-%20bcPropertyConceptCode%200..1>[AliasCode],[BiomedicalConcept]++-%20bcConceptCode%200..1>[AliasCode],[StudyDesign]++-%20studyDesignBlindingScheme%200..1>[AliasCode],[Study]++-%20studyPhase%200..1>[AliasCode],[StudyDesign],[Study],[BiomedicalConceptProperty],[BiomedicalConceptCategory],[BiomedicalConcept])

## Referenced by Class

 *  **None** *[➞bcCategoryCode](biomedicalConceptCategory__bcCategoryCode.md)*  <sub>0..1</sub>  **[AliasCode](AliasCode.md)**
 *  **None** *[➞bcPropertyConceptCode](biomedicalConceptProperty__bcPropertyConceptCode.md)*  <sub>0..1</sub>  **[AliasCode](AliasCode.md)**
 *  **None** *[➞bcConceptCode](biomedicalConcept__bcConceptCode.md)*  <sub>0..1</sub>  **[AliasCode](AliasCode.md)**
 *  **None** *[➞studyDesignBlindingScheme](studyDesign__studyDesignBlindingScheme.md)*  <sub>0..1</sub>  **[AliasCode](AliasCode.md)**
 *  **None** *[➞studyPhase](study__studyPhase.md)*  <sub>0..1</sub>  **[AliasCode](AliasCode.md)**

## Attributes


### Own

 * [➞aliasCodeId](aliasCode__aliasCodeId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞standardCode](aliasCode__standardCode.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞standardCodeAliases](aliasCode__standardCodeAliases.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
