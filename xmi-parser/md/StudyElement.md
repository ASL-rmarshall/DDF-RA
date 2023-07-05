
# Class: StudyElement




URI: [https://cdisc.org/DDF/USDMUML/StudyElement](https://cdisc.org/DDF/USDMUML/StudyElement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TransitionRule],[TransitionRule]<transitionStartRule%200..1-++[StudyElement&#124;studyElementDescription:string%20%3F;studyElementId:string%20%3F;studyElementName:string%20%3F],[TransitionRule]<transitionEndRule%200..1-++[StudyElement],[StudyDesign]++-%20studyElements%200..*>[StudyElement],[StudyDesign])](https://yuml.me/diagram/nofunky;dir:TB/class/[TransitionRule],[TransitionRule]<transitionStartRule%200..1-++[StudyElement&#124;studyElementDescription:string%20%3F;studyElementId:string%20%3F;studyElementName:string%20%3F],[TransitionRule]<transitionEndRule%200..1-++[StudyElement],[StudyDesign]++-%20studyElements%200..*>[StudyElement],[StudyDesign])

## Referenced by Class

 *  **None** *[➞studyElements](studyDesign__studyElements.md)*  <sub>0..\*</sub>  **[StudyElement](StudyElement.md)**

## Attributes


### Own

 * [➞studyElementDescription](studyElement__studyElementDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyElementId](studyElement__studyElementId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyElementName](studyElement__studyElementName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞transitionEndRule](studyElement__transitionEndRule.md)  <sub>0..1</sub>
     * Range: [TransitionRule](TransitionRule.md)
 * [➞transitionStartRule](studyElement__transitionStartRule.md)  <sub>0..1</sub>
     * Range: [TransitionRule](TransitionRule.md)
