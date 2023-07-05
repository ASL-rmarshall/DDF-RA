
# Class: Encounter




URI: [https://cdisc.org/DDF/USDMUML/Encounter](https://cdisc.org/DDF/USDMUML/Encounter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TransitionRule],[TransitionRule]<transitionStartRule%200..1-++[Encounter&#124;encounterDescription:string%20%3F;encounterId:string%20%3F;encounterName:string%20%3F;encounterScheduledAtTimingId:string%20%3F;nextEncounterId:string%20%3F;previousEncounterId:string%20%3F],[TransitionRule]<transitionEndRule%200..1-++[Encounter],[Code]<encounterType%200..1-++[Encounter],[Code]<encounterEnvironmentalSetting%200..1-++[Encounter],[Code]<encounterContactModes%200..*-++[Encounter],[StudyDesign]++-%20encounters%200..*>[Encounter],[StudyDesign],[Code])](https://yuml.me/diagram/nofunky;dir:TB/class/[TransitionRule],[TransitionRule]<transitionStartRule%200..1-++[Encounter&#124;encounterDescription:string%20%3F;encounterId:string%20%3F;encounterName:string%20%3F;encounterScheduledAtTimingId:string%20%3F;nextEncounterId:string%20%3F;previousEncounterId:string%20%3F],[TransitionRule]<transitionEndRule%200..1-++[Encounter],[Code]<encounterType%200..1-++[Encounter],[Code]<encounterEnvironmentalSetting%200..1-++[Encounter],[Code]<encounterContactModes%200..*-++[Encounter],[StudyDesign]++-%20encounters%200..*>[Encounter],[StudyDesign],[Code])

## Referenced by Class

 *  **None** *[➞encounters](studyDesign__encounters.md)*  <sub>0..\*</sub>  **[Encounter](Encounter.md)**

## Attributes


### Own

 * [➞encounterContactModes](encounter__encounterContactModes.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
 * [➞encounterDescription](encounter__encounterDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞encounterEnvironmentalSetting](encounter__encounterEnvironmentalSetting.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞encounterId](encounter__encounterId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞encounterName](encounter__encounterName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞encounterScheduledAtTimingId](encounter__encounterScheduledAtTimingId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞encounterType](encounter__encounterType.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞nextEncounterId](encounter__nextEncounterId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞previousEncounterId](encounter__previousEncounterId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞transitionEndRule](encounter__transitionEndRule.md)  <sub>0..1</sub>
     * Range: [TransitionRule](TransitionRule.md)
 * [➞transitionStartRule](encounter__transitionStartRule.md)  <sub>0..1</sub>
     * Range: [TransitionRule](TransitionRule.md)
