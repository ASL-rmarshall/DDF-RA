
# Class: Activity




URI: [https://cdisc.org/DDF/USDMUML/Activity](https://cdisc.org/DDF/USDMUML/Activity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Procedure],[Procedure]<definedProcedures%200..*-++[Activity&#124;activityDescription:string%20%3F;activityId:string%20%3F;activityIsConditional:boolean%20%3F;activityIsConditionalReason:string%20%3F;activityName:string%20%3F;activityTimelineId:string%20%3F;bcCategoryIds:string%20*;bcSurrogateIds:string%20*;biomedicalConceptIds:string%20*;nextActivityId:string%20%3F;previousActivityId:string%20%3F],[StudyDesign]++-%20activities%200..*>[Activity],[StudyDesign])](https://yuml.me/diagram/nofunky;dir:TB/class/[Procedure],[Procedure]<definedProcedures%200..*-++[Activity&#124;activityDescription:string%20%3F;activityId:string%20%3F;activityIsConditional:boolean%20%3F;activityIsConditionalReason:string%20%3F;activityName:string%20%3F;activityTimelineId:string%20%3F;bcCategoryIds:string%20*;bcSurrogateIds:string%20*;biomedicalConceptIds:string%20*;nextActivityId:string%20%3F;previousActivityId:string%20%3F],[StudyDesign]++-%20activities%200..*>[Activity],[StudyDesign])

## Referenced by Class

 *  **None** *[➞activities](studyDesign__activities.md)*  <sub>0..\*</sub>  **[Activity](Activity.md)**

## Attributes


### Own

 * [➞activityDescription](activity__activityDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞activityId](activity__activityId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞activityIsConditional](activity__activityIsConditional.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [➞activityIsConditionalReason](activity__activityIsConditionalReason.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞activityName](activity__activityName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞activityTimelineId](activity__activityTimelineId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞bcCategoryIds](activity__bcCategoryIds.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞bcSurrogateIds](activity__bcSurrogateIds.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞biomedicalConceptIds](activity__biomedicalConceptIds.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞definedProcedures](activity__definedProcedures.md)  <sub>0..\*</sub>
     * Range: [Procedure](Procedure.md)
 * [➞nextActivityId](activity__nextActivityId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞previousActivityId](activity__previousActivityId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
