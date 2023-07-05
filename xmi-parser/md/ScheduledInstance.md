
# Class: ScheduledInstance




URI: [https://cdisc.org/DDF/USDMUML/ScheduledInstance](https://cdisc.org/DDF/USDMUML/ScheduledInstance)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Timing]<scheduledInstanceTimings%200..*-++[ScheduledInstance&#124;defaultConditionId:string%20%3F;epochId:string%20%3F;scheduleTimelineExitId:string%20%3F;scheduledInstanceId:string%20%3F;scheduledInstanceTimelineId:string%20%3F;scheduledInstanceType:ScheduledInstanceType%20%3F],[ScheduleTimeline]++-%20scheduleTimelineInstances%200..*>[ScheduledInstance],[ScheduleTimeline])](https://yuml.me/diagram/nofunky;dir:TB/class/[Timing],[Timing]<scheduledInstanceTimings%200..*-++[ScheduledInstance&#124;defaultConditionId:string%20%3F;epochId:string%20%3F;scheduleTimelineExitId:string%20%3F;scheduledInstanceId:string%20%3F;scheduledInstanceTimelineId:string%20%3F;scheduledInstanceType:ScheduledInstanceType%20%3F],[ScheduleTimeline]++-%20scheduleTimelineInstances%200..*>[ScheduledInstance],[ScheduleTimeline])

## Referenced by Class

 *  **None** *[➞scheduleTimelineInstances](scheduleTimeline__scheduleTimelineInstances.md)*  <sub>0..\*</sub>  **[ScheduledInstance](ScheduledInstance.md)**

## Attributes


### Own

 * [➞defaultConditionId](scheduledInstance__defaultConditionId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞epochId](scheduledInstance__epochId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduleTimelineExitId](scheduledInstance__scheduleTimelineExitId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduledInstanceId](scheduledInstance__scheduledInstanceId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduledInstanceTimelineId](scheduledInstance__scheduledInstanceTimelineId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞scheduledInstanceTimings](scheduledInstance__scheduledInstanceTimings.md)  <sub>0..\*</sub>
     * Range: [Timing](Timing.md)
 * [➞scheduledInstanceType](scheduledInstance__scheduledInstanceType.md)  <sub>0..1</sub>
     * Range: [ScheduledInstanceType](ScheduledInstanceType.md)
