
# Class: ScheduleTimeline




URI: [https://cdisc.org/DDF/USDMUML/ScheduleTimeline](https://cdisc.org/DDF/USDMUML/ScheduleTimeline)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ScheduledInstance],[ScheduleTimelineExit],[ScheduledInstance]<scheduleTimelineInstances%200..*-++[ScheduleTimeline&#124;entryCondition:string%20%3F;mainTimeline:boolean%20%3F;scheduleTimelineDescription:string%20%3F;scheduleTimelineEntryId:string%20%3F;scheduleTimelineId:string%20%3F;scheduleTimelineName:string%20%3F],[ScheduleTimelineExit]<scheduleTimelineExits%200..*-++[ScheduleTimeline],[StudyDesign]++-%20studyScheduleTimelines%200..*>[ScheduleTimeline],[StudyDesign])](https://yuml.me/diagram/nofunky;dir:TB/class/[ScheduledInstance],[ScheduleTimelineExit],[ScheduledInstance]<scheduleTimelineInstances%200..*-++[ScheduleTimeline&#124;entryCondition:string%20%3F;mainTimeline:boolean%20%3F;scheduleTimelineDescription:string%20%3F;scheduleTimelineEntryId:string%20%3F;scheduleTimelineId:string%20%3F;scheduleTimelineName:string%20%3F],[ScheduleTimelineExit]<scheduleTimelineExits%200..*-++[ScheduleTimeline],[StudyDesign]++-%20studyScheduleTimelines%200..*>[ScheduleTimeline],[StudyDesign])

## Referenced by Class

 *  **None** *[➞studyScheduleTimelines](studyDesign__studyScheduleTimelines.md)*  <sub>0..\*</sub>  **[ScheduleTimeline](ScheduleTimeline.md)**

## Attributes


### Own

 * [➞entryCondition](scheduleTimeline__entryCondition.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞mainTimeline](scheduleTimeline__mainTimeline.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [➞scheduleTimelineDescription](scheduleTimeline__scheduleTimelineDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduleTimelineEntryId](scheduleTimeline__scheduleTimelineEntryId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduleTimelineExits](scheduleTimeline__scheduleTimelineExits.md)  <sub>0..\*</sub>
     * Range: [ScheduleTimelineExit](ScheduleTimelineExit.md)
 * [➞scheduleTimelineId](scheduleTimeline__scheduleTimelineId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduleTimelineInstances](scheduleTimeline__scheduleTimelineInstances.md)  <sub>0..\*</sub>
     * Range: [ScheduledInstance](ScheduledInstance.md)
 * [➞scheduleTimelineName](scheduleTimeline__scheduleTimelineName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
