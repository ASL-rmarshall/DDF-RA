
# Class: Timing




URI: [https://cdisc.org/DDF/USDMUML/Timing](https://cdisc.org/DDF/USDMUML/Timing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<timingType%200..1-++[Timing&#124;relativeFromScheduledInstanceId:string%20%3F;relativeToScheduledInstanceId:string%20%3F;timingDescription:string%20%3F;timingId:string%20%3F;timingValue:string%20%3F;timingWindow:string%20%3F;timingWindowLower:string%20%3F;timingWindowUpper:string%20%3F],[Code]<timingRelativeToFrom%200..1-++[Timing],[ScheduledInstance]++-%20scheduledInstanceTimings%200..*>[Timing],[ScheduledInstance],[Code])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<timingType%200..1-++[Timing&#124;relativeFromScheduledInstanceId:string%20%3F;relativeToScheduledInstanceId:string%20%3F;timingDescription:string%20%3F;timingId:string%20%3F;timingValue:string%20%3F;timingWindow:string%20%3F;timingWindowLower:string%20%3F;timingWindowUpper:string%20%3F],[Code]<timingRelativeToFrom%200..1-++[Timing],[ScheduledInstance]++-%20scheduledInstanceTimings%200..*>[Timing],[ScheduledInstance],[Code])

## Referenced by Class

 *  **None** *[➞scheduledInstanceTimings](scheduledInstance__scheduledInstanceTimings.md)*  <sub>0..\*</sub>  **[Timing](Timing.md)**

## Attributes


### Own

 * [➞relativeFromScheduledInstanceId](timing__relativeFromScheduledInstanceId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞relativeToScheduledInstanceId](timing__relativeToScheduledInstanceId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞timingDescription](timing__timingDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞timingId](timing__timingId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞timingRelativeToFrom](timing__timingRelativeToFrom.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞timingType](timing__timingType.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞timingValue](timing__timingValue.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞timingWindow](timing__timingWindow.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞timingWindowLower](timing__timingWindowLower.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞timingWindowUpper](timing__timingWindowUpper.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
