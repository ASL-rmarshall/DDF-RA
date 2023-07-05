
# Class: TransitionRule




URI: [https://cdisc.org/DDF/USDMUML/TransitionRule](https://cdisc.org/DDF/USDMUML/TransitionRule)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Encounter]++-%20transitionEndRule%200..1>[TransitionRule&#124;transitionRuleDescription:string%20%3F;transitionRuleId:string%20%3F],[Encounter]++-%20transitionStartRule%200..1>[TransitionRule],[StudyElement]++-%20transitionEndRule%200..1>[TransitionRule],[StudyElement]++-%20transitionStartRule%200..1>[TransitionRule],[StudyElement],[Encounter])](https://yuml.me/diagram/nofunky;dir:TB/class/[Encounter]++-%20transitionEndRule%200..1>[TransitionRule&#124;transitionRuleDescription:string%20%3F;transitionRuleId:string%20%3F],[Encounter]++-%20transitionStartRule%200..1>[TransitionRule],[StudyElement]++-%20transitionEndRule%200..1>[TransitionRule],[StudyElement]++-%20transitionStartRule%200..1>[TransitionRule],[StudyElement],[Encounter])

## Referenced by Class

 *  **None** *[➞transitionEndRule](encounter__transitionEndRule.md)*  <sub>0..1</sub>  **[TransitionRule](TransitionRule.md)**
 *  **None** *[➞transitionStartRule](encounter__transitionStartRule.md)*  <sub>0..1</sub>  **[TransitionRule](TransitionRule.md)**
 *  **None** *[➞transitionEndRule](studyElement__transitionEndRule.md)*  <sub>0..1</sub>  **[TransitionRule](TransitionRule.md)**
 *  **None** *[➞transitionStartRule](studyElement__transitionStartRule.md)*  <sub>0..1</sub>  **[TransitionRule](TransitionRule.md)**

## Attributes


### Own

 * [➞transitionRuleDescription](transitionRule__transitionRuleDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞transitionRuleId](transitionRule__transitionRuleId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
