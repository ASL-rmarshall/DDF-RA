
# Class: BiomedicalConceptCategory




URI: [https://cdisc.org/DDF/USDMUML/BiomedicalConceptCategory](https://cdisc.org/DDF/USDMUML/BiomedicalConceptCategory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AliasCode]<bcCategoryCode%200..1-++[BiomedicalConceptCategory&#124;bcCategoryChildIds:string%20*;bcCategoryDescription:string%20%3F;bcCategoryMemberIds:string%20*;bcCategoryName:string%20%3F;biomedicalConceptCategoryId:string%20%3F],[StudyDesign]++-%20bcCategories%200..*>[BiomedicalConceptCategory],[StudyDesign],[AliasCode])](https://yuml.me/diagram/nofunky;dir:TB/class/[AliasCode]<bcCategoryCode%200..1-++[BiomedicalConceptCategory&#124;bcCategoryChildIds:string%20*;bcCategoryDescription:string%20%3F;bcCategoryMemberIds:string%20*;bcCategoryName:string%20%3F;biomedicalConceptCategoryId:string%20%3F],[StudyDesign]++-%20bcCategories%200..*>[BiomedicalConceptCategory],[StudyDesign],[AliasCode])

## Referenced by Class

 *  **None** *[➞bcCategories](studyDesign__bcCategories.md)*  <sub>0..\*</sub>  **[BiomedicalConceptCategory](BiomedicalConceptCategory.md)**

## Attributes


### Own

 * [➞bcCategoryChildIds](biomedicalConceptCategory__bcCategoryChildIds.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞bcCategoryCode](biomedicalConceptCategory__bcCategoryCode.md)  <sub>0..1</sub>
     * Range: [AliasCode](AliasCode.md)
 * [➞bcCategoryDescription](biomedicalConceptCategory__bcCategoryDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcCategoryMemberIds](biomedicalConceptCategory__bcCategoryMemberIds.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞bcCategoryName](biomedicalConceptCategory__bcCategoryName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞biomedicalConceptCategoryId](biomedicalConceptCategory__biomedicalConceptCategoryId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
