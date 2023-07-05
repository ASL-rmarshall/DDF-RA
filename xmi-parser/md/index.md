
# USDMUML


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [Activity](Activity.md)
 * [Address](Address.md)
 * [AliasCode](AliasCode.md)
 * [AnalysisPopulation](AnalysisPopulation.md)
 * [BiomedicalConcept](BiomedicalConcept.md)
 * [BiomedicalConceptCategory](BiomedicalConceptCategory.md)
 * [BiomedicalConceptProperty](BiomedicalConceptProperty.md)
 * [BiomedicalConceptSurrogate](BiomedicalConceptSurrogate.md)
 * [Code](Code.md)
 * [Encounter](Encounter.md)
 * [Endpoint](Endpoint.md)
 * [Estimand](Estimand.md)
 * [Indication](Indication.md)
 * [IntercurrentEvent](IntercurrentEvent.md)
 * [InvestigationalIntervention](InvestigationalIntervention.md)
 * [Objective](Objective.md)
 * [Organization](Organization.md)
 * [Procedure](Procedure.md)
 * [ResponseCode](ResponseCode.md)
 * [ScheduleTimeline](ScheduleTimeline.md)
 * [ScheduleTimelineExit](ScheduleTimelineExit.md)
 * [ScheduledActivityInstance](ScheduledActivityInstance.md)
 * [ScheduledDecisionInstance](ScheduledDecisionInstance.md)
 * [ScheduledInstance](ScheduledInstance.md)
 * [Study](Study.md)
 * [StudyArm](StudyArm.md)
 * [StudyCell](StudyCell.md)
 * [StudyDesign](StudyDesign.md)
 * [StudyDesignPopulation](StudyDesignPopulation.md)
 * [StudyElement](StudyElement.md)
 * [StudyEpoch](StudyEpoch.md)
 * [StudyIdentifier](StudyIdentifier.md)
 * [StudyProtocolVersion](StudyProtocolVersion.md)
 * [Timing](Timing.md)
 * [TransitionRule](TransitionRule.md)

### Mixins


### Slots

 * [➞activityDescription](activity__activityDescription.md)
 * [➞activityId](activity__activityId.md)
 * [➞activityIsConditional](activity__activityIsConditional.md)
 * [➞activityIsConditionalReason](activity__activityIsConditionalReason.md)
 * [➞activityName](activity__activityName.md)
 * [➞activityTimelineId](activity__activityTimelineId.md)
 * [➞bcCategoryIds](activity__bcCategoryIds.md)
 * [➞bcSurrogateIds](activity__bcSurrogateIds.md)
 * [➞biomedicalConceptIds](activity__biomedicalConceptIds.md)
 * [➞definedProcedures](activity__definedProcedures.md)
 * [➞nextActivityId](activity__nextActivityId.md)
 * [➞previousActivityId](activity__previousActivityId.md)
 * [➞city](address__city.md)
 * [➞country](address__country.md)
 * [➞district](address__district.md)
 * [➞line](address__line.md)
 * [➞postalCode](address__postalCode.md)
 * [➞state](address__state.md)
 * [➞text](address__text.md)
 * [➞aliasCodeId](aliasCode__aliasCodeId.md)
 * [➞standardCode](aliasCode__standardCode.md)
 * [➞standardCodeAliases](aliasCode__standardCodeAliases.md)
 * [➞analysisPopulationId](analysisPopulation__analysisPopulationId.md)
 * [➞populationDescription](analysisPopulation__populationDescription.md)
 * [➞bcCategoryChildIds](biomedicalConceptCategory__bcCategoryChildIds.md)
 * [➞bcCategoryCode](biomedicalConceptCategory__bcCategoryCode.md)
 * [➞bcCategoryDescription](biomedicalConceptCategory__bcCategoryDescription.md)
 * [➞bcCategoryMemberIds](biomedicalConceptCategory__bcCategoryMemberIds.md)
 * [➞bcCategoryName](biomedicalConceptCategory__bcCategoryName.md)
 * [➞biomedicalConceptCategoryId](biomedicalConceptCategory__biomedicalConceptCategoryId.md)
 * [➞bcPropertyConceptCode](biomedicalConceptProperty__bcPropertyConceptCode.md)
 * [➞bcPropertyDatatype](biomedicalConceptProperty__bcPropertyDatatype.md)
 * [➞bcPropertyEnabled](biomedicalConceptProperty__bcPropertyEnabled.md)
 * [➞bcPropertyId](biomedicalConceptProperty__bcPropertyId.md)
 * [➞bcPropertyName](biomedicalConceptProperty__bcPropertyName.md)
 * [➞bcPropertyRequired](biomedicalConceptProperty__bcPropertyRequired.md)
 * [➞bcPropertyResponseCodes](biomedicalConceptProperty__bcPropertyResponseCodes.md)
 * [➞bcSurrogateDescription](biomedicalConceptSurrogate__bcSurrogateDescription.md)
 * [➞bcSurrogateId](biomedicalConceptSurrogate__bcSurrogateId.md)
 * [➞bcSurrogateName](biomedicalConceptSurrogate__bcSurrogateName.md)
 * [➞bcSurrogateReference](biomedicalConceptSurrogate__bcSurrogateReference.md)
 * [➞bcConceptCode](biomedicalConcept__bcConceptCode.md)
 * [➞bcName](biomedicalConcept__bcName.md)
 * [➞bcProperties](biomedicalConcept__bcProperties.md)
 * [➞bcReference](biomedicalConcept__bcReference.md)
 * [➞bcSynonyms](biomedicalConcept__bcSynonyms.md)
 * [➞biomedicalConceptId](biomedicalConcept__biomedicalConceptId.md)
 * [➞code](code__code.md)
 * [➞codeId](code__codeId.md)
 * [➞codeSystem](code__codeSystem.md)
 * [➞codeSystemVersion](code__codeSystemVersion.md)
 * [➞decode](code__decode.md)
 * [➞encounterContactModes](encounter__encounterContactModes.md)
 * [➞encounterDescription](encounter__encounterDescription.md)
 * [➞encounterEnvironmentalSetting](encounter__encounterEnvironmentalSetting.md)
 * [➞encounterId](encounter__encounterId.md)
 * [➞encounterName](encounter__encounterName.md)
 * [➞encounterScheduledAtTimingId](encounter__encounterScheduledAtTimingId.md)
 * [➞encounterType](encounter__encounterType.md)
 * [➞nextEncounterId](encounter__nextEncounterId.md)
 * [➞previousEncounterId](encounter__previousEncounterId.md)
 * [➞transitionEndRule](encounter__transitionEndRule.md)
 * [➞transitionStartRule](encounter__transitionStartRule.md)
 * [➞endpointDescription](endpoint__endpointDescription.md)
 * [➞endpointId](endpoint__endpointId.md)
 * [➞endpointLevel](endpoint__endpointLevel.md)
 * [➞endpointPurposeDescription](endpoint__endpointPurposeDescription.md)
 * [➞analysisPopulation](estimand__analysisPopulation.md)
 * [➞estimandId](estimand__estimandId.md)
 * [➞intercurrentEvents](estimand__intercurrentEvents.md)
 * [➞summaryMeasure](estimand__summaryMeasure.md)
 * [➞treatment](estimand__treatment.md)
 * [➞variableOfInterest](estimand__variableOfInterest.md)
 * [➞codes](indication__codes.md)
 * [➞indicationDescription](indication__indicationDescription.md)
 * [➞indicationId](indication__indicationId.md)
 * [➞intercurrentEventDescription](intercurrentEvent__intercurrentEventDescription.md)
 * [➞intercurrentEventId](intercurrentEvent__intercurrentEventId.md)
 * [➞intercurrentEventName](intercurrentEvent__intercurrentEventName.md)
 * [➞intercurrentEventStrategy](intercurrentEvent__intercurrentEventStrategy.md)
 * [➞codes](investigationalIntervention__codes.md)
 * [➞interventionDescription](investigationalIntervention__interventionDescription.md)
 * [➞investigationalInterventionId](investigationalIntervention__investigationalInterventionId.md)
 * [➞objectiveDescription](objective__objectiveDescription.md)
 * [➞objectiveEndpoints](objective__objectiveEndpoints.md)
 * [➞objectiveId](objective__objectiveId.md)
 * [➞objectiveLevel](objective__objectiveLevel.md)
 * [➞organizationId](organization__organizationId.md)
 * [➞organizationIdentifier](organization__organizationIdentifier.md)
 * [➞organizationIdentifierScheme](organization__organizationIdentifierScheme.md)
 * [➞organizationLegalAddress](organization__organizationLegalAddress.md)
 * [➞organizationName](organization__organizationName.md)
 * [➞organizationType](organization__organizationType.md)
 * [➞procedureCode](procedure__procedureCode.md)
 * [➞procedureDescription](procedure__procedureDescription.md)
 * [➞procedureId](procedure__procedureId.md)
 * [➞procedureIsConditional](procedure__procedureIsConditional.md)
 * [➞procedureIsConditionalReason](procedure__procedureIsConditionalReason.md)
 * [➞procedureName](procedure__procedureName.md)
 * [➞procedureType](procedure__procedureType.md)
 * [➞code](responseCode__code.md)
 * [➞responseCodeEnabled](responseCode__responseCodeEnabled.md)
 * [➞responseCodeId](responseCode__responseCodeId.md)
 * [➞scheduleTimelineExitId](scheduleTimelineExit__scheduleTimelineExitId.md)
 * [➞entryCondition](scheduleTimeline__entryCondition.md)
 * [➞mainTimeline](scheduleTimeline__mainTimeline.md)
 * [➞scheduleTimelineDescription](scheduleTimeline__scheduleTimelineDescription.md)
 * [➞scheduleTimelineEntryId](scheduleTimeline__scheduleTimelineEntryId.md)
 * [➞scheduleTimelineExits](scheduleTimeline__scheduleTimelineExits.md)
 * [➞scheduleTimelineId](scheduleTimeline__scheduleTimelineId.md)
 * [➞scheduleTimelineInstances](scheduleTimeline__scheduleTimelineInstances.md)
 * [➞scheduleTimelineName](scheduleTimeline__scheduleTimelineName.md)
 * [➞activityIds](scheduledActivityInstance__activityIds.md)
 * [➞scheduledActivityInstanceEncounterId](scheduledActivityInstance__scheduledActivityInstanceEncounterId.md)
 * [➞conditionAssignments](scheduledDecisionInstance__conditionAssignments.md)
 * [➞defaultConditionId](scheduledInstance__defaultConditionId.md)
 * [➞epochId](scheduledInstance__epochId.md)
 * [➞scheduleTimelineExitId](scheduledInstance__scheduleTimelineExitId.md)
 * [➞scheduledInstanceId](scheduledInstance__scheduledInstanceId.md)
 * [➞scheduledInstanceTimelineId](scheduledInstance__scheduledInstanceTimelineId.md)
 * [➞scheduledInstanceTimings](scheduledInstance__scheduledInstanceTimings.md)
 * [➞scheduledInstanceType](scheduledInstance__scheduledInstanceType.md)
 * [➞studyArmDataOriginDescription](studyArm__studyArmDataOriginDescription.md)
 * [➞studyArmDataOriginType](studyArm__studyArmDataOriginType.md)
 * [➞studyArmDescription](studyArm__studyArmDescription.md)
 * [➞studyArmId](studyArm__studyArmId.md)
 * [➞studyArmName](studyArm__studyArmName.md)
 * [➞studyArmType](studyArm__studyArmType.md)
 * [➞studyArmId](studyCell__studyArmId.md)
 * [➞studyCellId](studyCell__studyCellId.md)
 * [➞studyElementIds](studyCell__studyElementIds.md)
 * [➞studyEpochId](studyCell__studyEpochId.md)
 * [➞plannedMaximumAgeOfParticipants](studyDesignPopulation__plannedMaximumAgeOfParticipants.md)
 * [➞plannedMinimumAgeOfParticipants](studyDesignPopulation__plannedMinimumAgeOfParticipants.md)
 * [➞plannedNumberOfParticipants](studyDesignPopulation__plannedNumberOfParticipants.md)
 * [➞plannedSexOfParticipants](studyDesignPopulation__plannedSexOfParticipants.md)
 * [➞populationDescription](studyDesignPopulation__populationDescription.md)
 * [➞studyDesignPopulationId](studyDesignPopulation__studyDesignPopulationId.md)
 * [➞activities](studyDesign__activities.md)
 * [➞bcCategories](studyDesign__bcCategories.md)
 * [➞bcSurrogates](studyDesign__bcSurrogates.md)
 * [➞biomedicalConcepts](studyDesign__biomedicalConcepts.md)
 * [➞encounters](studyDesign__encounters.md)
 * [➞interventionModel](studyDesign__interventionModel.md)
 * [➞studyArms](studyDesign__studyArms.md)
 * [➞studyCells](studyDesign__studyCells.md)
 * [➞studyDesignBlindingScheme](studyDesign__studyDesignBlindingScheme.md)
 * [➞studyDesignDescription](studyDesign__studyDesignDescription.md)
 * [➞studyDesignId](studyDesign__studyDesignId.md)
 * [➞studyDesignName](studyDesign__studyDesignName.md)
 * [➞studyDesignRationale](studyDesign__studyDesignRationale.md)
 * [➞studyElements](studyDesign__studyElements.md)
 * [➞studyEpochs](studyDesign__studyEpochs.md)
 * [➞studyEstimands](studyDesign__studyEstimands.md)
 * [➞studyIndications](studyDesign__studyIndications.md)
 * [➞studyInvestigationalInterventions](studyDesign__studyInvestigationalInterventions.md)
 * [➞studyObjectives](studyDesign__studyObjectives.md)
 * [➞studyPopulations](studyDesign__studyPopulations.md)
 * [➞studyScheduleTimelines](studyDesign__studyScheduleTimelines.md)
 * [➞therapeuticAreas](studyDesign__therapeuticAreas.md)
 * [➞trialIntentTypes](studyDesign__trialIntentTypes.md)
 * [➞trialType](studyDesign__trialType.md)
 * [➞studyElementDescription](studyElement__studyElementDescription.md)
 * [➞studyElementId](studyElement__studyElementId.md)
 * [➞studyElementName](studyElement__studyElementName.md)
 * [➞transitionEndRule](studyElement__transitionEndRule.md)
 * [➞transitionStartRule](studyElement__transitionStartRule.md)
 * [➞nextStudyEpochId](studyEpoch__nextStudyEpochId.md)
 * [➞previousStudyEpochId](studyEpoch__previousStudyEpochId.md)
 * [➞studyEpochDescription](studyEpoch__studyEpochDescription.md)
 * [➞studyEpochId](studyEpoch__studyEpochId.md)
 * [➞studyEpochName](studyEpoch__studyEpochName.md)
 * [➞studyEpochType](studyEpoch__studyEpochType.md)
 * [➞studyIdentifier](studyIdentifier__studyIdentifier.md)
 * [➞studyIdentifierId](studyIdentifier__studyIdentifierId.md)
 * [➞studyIdentifierScope](studyIdentifier__studyIdentifierScope.md)
 * [➞briefTitle](studyProtocolVersion__briefTitle.md)
 * [➞officialTitle](studyProtocolVersion__officialTitle.md)
 * [➞protocolAmendment](studyProtocolVersion__protocolAmendment.md)
 * [➞protocolEffectiveDate](studyProtocolVersion__protocolEffectiveDate.md)
 * [➞protocolStatus](studyProtocolVersion__protocolStatus.md)
 * [➞protocolVersion](studyProtocolVersion__protocolVersion.md)
 * [➞publicTitle](studyProtocolVersion__publicTitle.md)
 * [➞scientificTitle](studyProtocolVersion__scientificTitle.md)
 * [➞studyProtocolVersionId](studyProtocolVersion__studyProtocolVersionId.md)
 * [➞businessTherapeuticAreas](study__businessTherapeuticAreas.md)
 * [➞studyAcronym](study__studyAcronym.md)
 * [➞studyDesigns](study__studyDesigns.md)
 * [➞studyId](study__studyId.md)
 * [➞studyIdentifiers](study__studyIdentifiers.md)
 * [➞studyPhase](study__studyPhase.md)
 * [➞studyProtocolVersions](study__studyProtocolVersions.md)
 * [➞studyRationale](study__studyRationale.md)
 * [➞studyTitle](study__studyTitle.md)
 * [➞studyType](study__studyType.md)
 * [➞studyVersion](study__studyVersion.md)
 * [➞relativeFromScheduledInstanceId](timing__relativeFromScheduledInstanceId.md)
 * [➞relativeToScheduledInstanceId](timing__relativeToScheduledInstanceId.md)
 * [➞timingDescription](timing__timingDescription.md)
 * [➞timingId](timing__timingId.md)
 * [➞timingRelativeToFrom](timing__timingRelativeToFrom.md)
 * [➞timingType](timing__timingType.md)
 * [➞timingValue](timing__timingValue.md)
 * [➞timingWindow](timing__timingWindow.md)
 * [➞timingWindowLower](timing__timingWindowLower.md)
 * [➞timingWindowUpper](timing__timingWindowUpper.md)
 * [➞transitionRuleDescription](transitionRule__transitionRuleDescription.md)
 * [➞transitionRuleId](transitionRule__transitionRuleId.md)

### Enums

 * [ScheduledInstanceType](ScheduledInstanceType.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
