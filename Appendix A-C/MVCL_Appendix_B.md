# Appendix B: MVCL Rule Set

The rule set below resolves the type, cardinality, and navigation
inconsistencies identified during the audit of the previous draft. The
intended distinction between syntactic, structural, and semantic
inconsistency detection is preserved.

## B.1 Syntactic Rules (syntactic_rules.mvcl)

``` text

// SR-01: Required attributes
```

``` text

rule SR_01_AttributeExistence : syntactic
```

``` text

context ElectricalComponent ec
```

``` text

check ec.id <> null and ec.name <> null
```

``` text

// SR-02: Non-negative requirement capacity
```

``` text

rule SR_02_TypeCompatibility : syntactic
```

``` text

context Requirement r
```

``` text

check r.minRequiredCapacity >= 0.0
```

``` text

// SR-03: Enumeration validity
```

``` text

rule SR_03_EnumValidity : syntactic
```

``` text

context ProductionUnit pu
```

``` text

check pu.status <> null
```

``` text

// SR-04: Reference validity
```

``` text

rule SR_04_ReferenceValidity : syntactic
```

``` text

context MechanicalPart mp
```

``` text

check mp.linkedController <> null implies mp.linkedController.id <> null
```

``` text

// SR-05: Battery attribute-domain consistency
```

``` text

rule SR_05_DataTypeConsistency : syntactic
```

``` text

context Battery b
```

``` text

check b.capacity >= 0.0 and b.chemistry <> null
```

``` text

// SR-06: Software component completeness
```

``` text

rule SR_06_SoftwareCompleteness : syntactic
```

``` text

context SoftwareComponent sc
```

``` text

check sc.vendor <> null and sc.version matches "[0-9]+\.[0-9]+\.[0-9]+"
```

``` text

// SR-07: Production unit completion
```

``` text

rule SR_07_ProductionCompleteness : syntactic
```

``` text

context ProductionUnit pu
```

``` text

check pu.startDate <> null and pu.capacity > 0
```

``` text

// SR-08: Controller firmware validity
```

``` text

rule SR_08_FirmwareValidity : syntactic
```

``` text

context Controller c
```

``` text

check c.firmwareVersion matches "[0-9]+\.[0-9]+"
```

## B.2 Structural Rules (structural_rules.mvcl)

``` text

// ST-01: Required sensor connections
```

``` text

rule ST_01_RequiredConnection : structural
```

``` text

context Controller c
```

``` text

check c.linkedSensor->size() > 0
```

``` text

// ST-02: Production-line completeness
```

``` text

rule ST_02_LineCompleteness : structural
```

``` text

context ProductionLine pl
```

``` text

check pl.units->size() = pl.parts->size()
```

``` text

// ST-03: Controller mapping uniqueness
```

``` text

rule ST_03_ReferenceUniqueness : structural
```

``` text

context MechanicalPart mp
```

``` text

check MechanicalPart.allInstances()->isUnique(p | p.linkedController)
```

``` text

// ST-04: Bidirectional part-line consistency
```

``` text

rule ST_04_BidirectionalConsistency : structural
```

``` text

context ProductionLine pl
```

``` text

check pl.parts->forAll(p | p.usedIn = pl)
```

``` text

// ST-05: Hardware-controller mapping
```

``` text

rule ST_05_HardwareSoftwareMapping : structural
```

``` text

context ElectricalComponent ec
```

``` text

check ec.connectedTo->forAll(c |
```

c.type = ComponentType::CONTROLLER implies c.id \<\> null)

``` text

// ST-06: Controller-sensor linkage
```

``` text

rule ST_06_ControllerSensorLink : structural
```

``` text

context Controller c
```

``` text

check c.linkedSensor->forAll(s | s.connectedTo = c)
```

``` text

// ST-07: Requirement assignment
```

``` text

rule ST_07_RequirementAssignment : structural
```

``` text

context Requirement r
```

``` text

check r.assignedTo <> null
```

``` text

// ST-08: Dependency graph acyclicity
```

``` text

rule ST_08_DependencyAcyclicity : structural
```

``` text

context Functionality f
```

``` text

check f.dependsOn->closure(d | d.dependsOn)->excludes(f)
```

``` text

// ST-09: Production unit-line relationship
```

``` text

rule ST_09_ProductionUnitLine : structural
```

``` text

context ProductionUnit pu
```

``` text

check pu.line <> null and pu.line.units->includes(pu)
```

``` text

// ST-10: Part-line relationship
```

``` text

rule ST_10_PartLineRelationship : structural
```

``` text

context MechanicalPart mp
```

``` text

check mp.usedIn <> null and mp.usedIn.parts->includes(mp)
```

## B.3 Semantic Rules (semantic_rules.mvcl)

``` text

// SE-01: Battery capacity adequacy
```

``` text

rule SE_01_BatteryCapacity : semantic
```

``` text

context Battery b, Requirement r
```

``` text

check b.capacity >= r.minRequiredCapacity
```

``` text

// SE-02: Power-supply adequacy with safety factor
```

``` text

rule SE_02_PowerSupplyAdequacy : semantic
```

``` text

context PowerSupply ps, SystemLoad sl
```

``` text

check ps.maxPower >= sl.peakLoad * 1.2
```

``` text

// SE-03: Production readiness
```

``` text

rule SE_03_ProductionReadiness : semantic
```

``` text

context ProductionUnit pu
```

``` text

check (pu.status = ProductionStatus::PRODUCTION)
```

``` text

implies (pu.validated = true and pu.capacity > 0)
```

``` text

// SE-04: Effective software-hardware capacity alignment
```

``` text

rule SE_04_CapacityAlignment : semantic
```

``` text

context Requirement r, Battery b
```

``` text

check r.minRequiredCapacity <= b.capacity * b.health / 100
```

``` text

// SE-05: Validation timing constraint
```

``` text

rule SE_05_ValidationTiming : semantic
```

``` text

context Controller c
```

``` text

check daysBetween(c.deploymentDate, c.lastValidationDate) <= 30
```

``` text

// SE-05 uses an implementation-defined daysBetween helper that returns elapsed calendar days; the helper is provided by the MVCL-to-EVL mapping layer to avoid relying on implicit date-minus-integer coercion.
// SE-06: Production-line efficiency
```

``` text

rule SE_06_LineEfficiency : semantic
```

``` text

context ProductionLine pl
```

``` text

check pl.efficiency >= 75.0
```

``` text

// SE-07: Performance requirement versus sensor accuracy
```

``` text

rule SE_07_SensorAccuracy : semantic
```

``` text

context Sensor s, Requirement r
```

``` text

check (r.type = RequirementType::PERFORMANCE and
```

r.assignedTo = s.connectedTo)

``` text

implies s.accuracy >= 95.0
```

``` text

// SE-08: Battery lifecycle constraint
```

``` text

rule SE_08_BatteryLifecycle : semantic
```

``` text

context Battery b
```

``` text

check b.cycles < 1000
```

``` text

// SE-09: MUST_HAVE requirement has a versioned assigned component
```

``` text

rule SE_09_RequirementPriority : semantic
```

``` text

context Requirement r
```

``` text

check (r.priority = RequirementPriority::MUST_HAVE)
```

``` text

implies (r.assignedTo.version <> null)
```

``` text

// SE-10: Production-unit location validity
```

``` text

rule SE_10_LocationValidity : semantic
```

``` text

context ProductionUnit pu
```

``` text

check pu.location = pu.line.location
```

``` text

// SE-11: Controller sensor coverage
```

``` text

rule SE_11_SensorCoverage : semantic
```

``` text

context Controller c, SystemLoad sl
```

``` text

check c.linkedSensor->size() >=
```

(sl.priority = LoadPriority::CRITICAL ? 2 : 1)

``` text

// SE-12: Power-supply redundancy
```

``` text

rule SE_12_PowerRedundancy : semantic
```

``` text

context SystemLoad sl
```

``` text

check sl.connectedTo->size() >=
```

(sl.priority = LoadPriority::CRITICAL ? 2 : 1)

## B.4 Tolerance Context Definitions (contexts.json)

``` text

{
```

``` text

"contexts": [
```

``` text

{
```

``` text

"id": "prototype-phase",
```

``` text

"description": "Development prototype phase with relaxed constraints",
```

``` text

"parameters": {
```

``` text

"phase": "Prototype",
```

``` text

"criticality": "Low",
```

``` text

"deadline": "2026-12-31",
```

``` text

"team_size": 5,
```

``` text

"budget": 1000000
```

``` text

}
```

``` text

},
```

``` text

{
```

``` text

"id": "production-phase",
```

``` text

"description": "Production phase with strict constraints",
```

``` text

"parameters": {
```

``` text

"phase": "Production",
```

``` text

"criticality": "High",
```

``` text

"deadline": "2026-09-01",
```

``` text

"team_size": 20,
```

``` text

"budget": 10000000
```

``` text

}
```

``` text

},
```

``` text

{
```

``` text

"id": "maintenance-phase",
```

``` text

"description": "Maintenance phase with balanced constraints",
```

``` text

"parameters": {
```

``` text

"phase": "Maintenance",
```

``` text

"criticality": "Medium",
```

``` text

"deadline": "2026-12-01",
```

``` text

"team_size": 8,
```

``` text

"budget": 3000000
```

``` text

}
```

``` text

}
```

\]

``` text

}
```

The numerical tolerance thresholds for SE-01--SE-12 remain in the
machine-readable contexts.json artifact used by the tolerance module.
They are intentionally separated from the detection rules, preserving
the detection--tolerance separation adopted by the framework.
