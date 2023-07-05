
# Class: Endpoint




URI: [https://cdisc.org/DDF/USDMUML/Endpoint](https://cdisc.org/DDF/USDMUML/Endpoint)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<endpointLevel%200..1-++[Endpoint&#124;endpointDescription:string%20%3F;endpointId:string%20%3F;endpointPurposeDescription:string%20%3F],[Estimand]++-%20variableOfInterest%200..1>[Endpoint],[Objective]++-%20objectiveEndpoints%200..*>[Endpoint],[Objective],[Estimand],[Code])](https://yuml.me/diagram/nofunky;dir:TB/class/[Code]<endpointLevel%200..1-++[Endpoint&#124;endpointDescription:string%20%3F;endpointId:string%20%3F;endpointPurposeDescription:string%20%3F],[Estimand]++-%20variableOfInterest%200..1>[Endpoint],[Objective]++-%20objectiveEndpoints%200..*>[Endpoint],[Objective],[Estimand],[Code])

## Referenced by Class

 *  **None** *[➞variableOfInterest](estimand__variableOfInterest.md)*  <sub>0..1</sub>  **[Endpoint](Endpoint.md)**
 *  **None** *[➞objectiveEndpoints](objective__objectiveEndpoints.md)*  <sub>0..\*</sub>  **[Endpoint](Endpoint.md)**

## Attributes


### Own

 * [➞endpointDescription](endpoint__endpointDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞endpointId](endpoint__endpointId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞endpointLevel](endpoint__endpointLevel.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞endpointPurposeDescription](endpoint__endpointPurposeDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
