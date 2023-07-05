
# Class: StudyDesign




URI: [https://cdisc.org/DDF/USDMUML/StudyDesign](https://cdisc.org/DDF/USDMUML/StudyDesign)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyEpoch],[StudyElement],[StudyDesignPopulation],[Code]<trialType%200..*-++[StudyDesign&#124;studyDesignDescription:string%20%3F;studyDesignId:string%20%3F;studyDesignName:string%20%3F;studyDesignRationale:string%20%3F],[Code]<trialIntentTypes%200..*-++[StudyDesign],[Code]<therapeuticAreas%200..*-++[StudyDesign],[ScheduleTimeline]<studyScheduleTimelines%200..*-++[StudyDesign],[StudyDesignPopulation]<studyPopulations%200..*-++[StudyDesign],[Objective]<studyObjectives%200..*-++[StudyDesign],[InvestigationalIntervention]<studyInvestigationalInterventions%200..*-++[StudyDesign],[Indication]<studyIndications%200..*-++[StudyDesign],[Estimand]<studyEstimands%200..*-++[StudyDesign],[StudyEpoch]<studyEpochs%200..*-++[StudyDesign],[StudyElement]<studyElements%200..*-++[StudyDesign],[AliasCode]<studyDesignBlindingScheme%200..1-++[StudyDesign],[StudyCell]<studyCells%200..*-++[StudyDesign],[StudyArm]<studyArms%200..*-++[StudyDesign],[Code]<interventionModel%200..1-++[StudyDesign],[Encounter]<encounters%200..*-++[StudyDesign],[BiomedicalConcept]<biomedicalConcepts%200..*-++[StudyDesign],[BiomedicalConceptSurrogate]<bcSurrogates%200..*-++[StudyDesign],[BiomedicalConceptCategory]<bcCategories%200..*-++[StudyDesign],[Activity]<activities%200..*-++[StudyDesign],[Study]++-%20studyDesigns%200..*>[StudyDesign],[StudyCell],[StudyArm],[Study],[ScheduleTimeline],[Objective],[InvestigationalIntervention],[Indication],[Estimand],[Encounter],[Code],[BiomedicalConceptSurrogate],[BiomedicalConceptCategory],[BiomedicalConcept],[AliasCode],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyEpoch],[StudyElement],[StudyDesignPopulation],[Code]<trialType%200..*-++[StudyDesign&#124;studyDesignDescription:string%20%3F;studyDesignId:string%20%3F;studyDesignName:string%20%3F;studyDesignRationale:string%20%3F],[Code]<trialIntentTypes%200..*-++[StudyDesign],[Code]<therapeuticAreas%200..*-++[StudyDesign],[ScheduleTimeline]<studyScheduleTimelines%200..*-++[StudyDesign],[StudyDesignPopulation]<studyPopulations%200..*-++[StudyDesign],[Objective]<studyObjectives%200..*-++[StudyDesign],[InvestigationalIntervention]<studyInvestigationalInterventions%200..*-++[StudyDesign],[Indication]<studyIndications%200..*-++[StudyDesign],[Estimand]<studyEstimands%200..*-++[StudyDesign],[StudyEpoch]<studyEpochs%200..*-++[StudyDesign],[StudyElement]<studyElements%200..*-++[StudyDesign],[AliasCode]<studyDesignBlindingScheme%200..1-++[StudyDesign],[StudyCell]<studyCells%200..*-++[StudyDesign],[StudyArm]<studyArms%200..*-++[StudyDesign],[Code]<interventionModel%200..1-++[StudyDesign],[Encounter]<encounters%200..*-++[StudyDesign],[BiomedicalConcept]<biomedicalConcepts%200..*-++[StudyDesign],[BiomedicalConceptSurrogate]<bcSurrogates%200..*-++[StudyDesign],[BiomedicalConceptCategory]<bcCategories%200..*-++[StudyDesign],[Activity]<activities%200..*-++[StudyDesign],[Study]++-%20studyDesigns%200..*>[StudyDesign],[StudyCell],[StudyArm],[Study],[ScheduleTimeline],[Objective],[InvestigationalIntervention],[Indication],[Estimand],[Encounter],[Code],[BiomedicalConceptSurrogate],[BiomedicalConceptCategory],[BiomedicalConcept],[AliasCode],[Activity])

## Referenced by Class

 *  **None** *[➞studyDesigns](study__studyDesigns.md)*  <sub>0..\*</sub>  **[StudyDesign](StudyDesign.md)**

## Attributes


### Own

 * [➞activities](studyDesign__activities.md)  <sub>0..\*</sub>
     * Range: [Activity](Activity.md)
 * [➞bcCategories](studyDesign__bcCategories.md)  <sub>0..\*</sub>
     * Range: [BiomedicalConceptCategory](BiomedicalConceptCategory.md)
 * [➞bcSurrogates](studyDesign__bcSurrogates.md)  <sub>0..\*</sub>
     * Range: [BiomedicalConceptSurrogate](BiomedicalConceptSurrogate.md)
 * [➞biomedicalConcepts](studyDesign__biomedicalConcepts.md)  <sub>0..\*</sub>
     * Range: [BiomedicalConcept](BiomedicalConcept.md)
 * [➞encounters](studyDesign__encounters.md)  <sub>0..\*</sub>
     * Range: [Encounter](Encounter.md)
 * [➞interventionModel](studyDesign__interventionModel.md)  <sub>0..1</sub>
     * Range: [Code](Code.md)
 * [➞studyArms](studyDesign__studyArms.md)  <sub>0..\*</sub>
     * Range: [StudyArm](StudyArm.md)
 * [➞studyCells](studyDesign__studyCells.md)  <sub>0..\*</sub>
     * Range: [StudyCell](StudyCell.md)
 * [➞studyDesignBlindingScheme](studyDesign__studyDesignBlindingScheme.md)  <sub>0..1</sub>
     * Range: [AliasCode](AliasCode.md)
 * [➞studyDesignDescription](studyDesign__studyDesignDescription.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyDesignId](studyDesign__studyDesignId.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyDesignName](studyDesign__studyDesignName.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyDesignRationale](studyDesign__studyDesignRationale.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞studyElements](studyDesign__studyElements.md)  <sub>0..\*</sub>
     * Range: [StudyElement](StudyElement.md)
 * [➞studyEpochs](studyDesign__studyEpochs.md)  <sub>0..\*</sub>
     * Range: [StudyEpoch](StudyEpoch.md)
 * [➞studyEstimands](studyDesign__studyEstimands.md)  <sub>0..\*</sub>
     * Range: [Estimand](Estimand.md)
 * [➞studyIndications](studyDesign__studyIndications.md)  <sub>0..\*</sub>
     * Range: [Indication](Indication.md)
 * [➞studyInvestigationalInterventions](studyDesign__studyInvestigationalInterventions.md)  <sub>0..\*</sub>
     * Range: [InvestigationalIntervention](InvestigationalIntervention.md)
 * [➞studyObjectives](studyDesign__studyObjectives.md)  <sub>0..\*</sub>
     * Range: [Objective](Objective.md)
 * [➞studyPopulations](studyDesign__studyPopulations.md)  <sub>0..\*</sub>
     * Range: [StudyDesignPopulation](StudyDesignPopulation.md)
 * [➞studyScheduleTimelines](studyDesign__studyScheduleTimelines.md)  <sub>0..\*</sub>
     * Range: [ScheduleTimeline](ScheduleTimeline.md)
 * [➞therapeuticAreas](studyDesign__therapeuticAreas.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
 * [➞trialIntentTypes](studyDesign__trialIntentTypes.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
 * [➞trialType](studyDesign__trialType.md)  <sub>0..\*</sub>
     * Range: [Code](Code.md)
