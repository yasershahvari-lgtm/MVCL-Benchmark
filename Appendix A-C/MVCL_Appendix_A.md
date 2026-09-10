# Appendix A: Benchmark Data Models

This appendix defines the benchmark metamodels used by the MVCL
controlled automotive benchmark scenario. The definitions are aligned
with the executable rule set in Appendix B so that every rule refers
only to declared classes, attributes, references, and cardinalities.

## A.1 Electrical Metamodel (Electrical.ecore)

``` text

@namespace(uri="http://www.mvcl.org/electrical", prefix="electrical")
```

``` text

package electrical;
```

``` text

class ElectricalComponent {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

attribute type: ComponentType;
```

``` text

attribute voltage: EDouble;
```

``` text

attribute current: EDouble;
```

``` text

attribute powerRating: EDouble;
```

``` text

reference connectedTo: ElectricalComponent[0..*];
```

``` text

}
```

``` text

enum ComponentType {
```

BATTERY;

RESISTOR;

CAPACITOR;

MOTOR;

SENSOR;

CONTROLLER;

POWER_SUPPLY;

``` text

}
```

``` text

class Battery extends ElectricalComponent {
```

``` text

attribute capacity: EDouble;
```

``` text

attribute chemistry: BatteryChemistry;
```

``` text

attribute cycles: EInt;
```

``` text

attribute health: EDouble;
```

``` text

reference supplies: PowerSupply[0..1];
```

``` text

}
```

``` text

enum BatteryChemistry {
```

LITHIUM_ION;

LEAD_ACID;

NICKEL_METAL_HYDRIDE;

SOLID_STATE;

``` text

}
```

``` text

class PowerSupply extends ElectricalComponent {
```

``` text

attribute maxPower: EDouble;
```

``` text

attribute efficiency: EDouble;
```

``` text

attribute inputVoltage: EDouble;
```

``` text

attribute outputVoltage: EDouble;
```

``` text

reference powers: SystemLoad[0..*];
```

``` text

}
```

``` text

class SystemLoad extends ElectricalComponent {
```

``` text

attribute peakLoad: EDouble;
```

``` text

attribute averageLoad: EDouble;
```

``` text

attribute priority: LoadPriority;
```

``` text

reference connectedTo: PowerSupply[1..*];
```

``` text

}
```

``` text

enum LoadPriority {
```

CRITICAL;

HIGH;

MEDIUM;

LOW;

BACKUP;

``` text

}
```

## A.2 Software Metamodel (Software.ecore)

``` text

@namespace(uri="http://www.mvcl.org/software", prefix="software")
```

``` text

package software;
```

``` text

class SoftwareComponent {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

attribute version: EString;
```

``` text

attribute vendor: EString;
```

``` text

attribute deploymentDate: EDate;
```

``` text

reference requires: Requirement[0..*];
```

``` text

reference implements: Functionality[0..*];
```

``` text

}
```

``` text

class Requirement {
```

``` text

attribute id: EString;
```

``` text

attribute description: EString;
```

``` text

attribute type: RequirementType;
```

``` text

attribute priority: RequirementPriority;
```

``` text

attribute minRequiredCapacity: EDouble;
```

``` text

attribute minResponseTime: EDouble;
```

``` text

attribute maxLatency: EDouble;
```

``` text

attribute isMandatory: EBoolean;
```

``` text

reference assignedTo: SoftwareComponent[1];
```

``` text

}
```

``` text

enum RequirementType {
```

FUNCTIONAL;

NON_FUNCTIONAL;

PERFORMANCE;

SECURITY;

RELIABILITY;

USABILITY;

``` text

}
```

``` text

enum RequirementPriority {
```

MUST_HAVE;

SHOULD_HAVE;

COULD_HAVE;

WON_T_HAVE;

``` text

}
```

``` text

class Functionality {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

attribute description: EString;
```

``` text

attribute complexity: ComplexityLevel;
```

``` text

reference providedBy: SoftwareComponent[1];
```

``` text

reference dependsOn: Functionality[0..*];
```

``` text

}
```

``` text

enum ComplexityLevel {
```

LOW;

MEDIUM;

HIGH;

VERY_HIGH;

``` text

}
```

``` text

class Controller extends SoftwareComponent {
```

``` text

attribute firmwareVersion: EString;
```

``` text

attribute updateStatus: UpdateStatus;
```

``` text

attribute lastValidationDate: EDate;
```

``` text

attribute controlLoopFrequency: EDouble;
```

``` text

reference linkedSensor: Sensor[0..*];
```

``` text

reference controls: Actuator[0..*];
```

``` text

}
```

``` text

class Actuator {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

}
```

``` text

class Sensor {
```

``` text

attribute id: EString;
```

``` text

attribute type: SensorType;
```

``` text

attribute accuracy: EDouble;
```

``` text

attribute range: EDouble;
```

``` text

attribute units: EString;
```

``` text

reference connectedTo: Controller[1];
```

``` text

}
```

``` text

enum SensorType {
```

TEMPERATURE;

PRESSURE;

CURRENT;

VOLTAGE;

SPEED;

POSITION;

``` text

}
```

``` text

enum UpdateStatus {
```

UP_TO_DATE;

UPDATE_AVAILABLE;

UPDATE_IN_PROGRESS;

UPDATE_FAILED;

``` text

}
```

## A.3 Production Metamodel (Production.ecore)

``` text

@namespace(uri="http://www.mvcl.org/production", prefix="production")
```

``` text

package production;
```

``` text

class ProductionUnit {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

attribute status: ProductionStatus;
```

``` text

attribute location: EString;
```

``` text

attribute capacity: EDouble;
```

``` text

attribute validated: EBoolean;
```

``` text

attribute startDate: EDate;
```

``` text

reference parts: MechanicalPart[0..*];
```

``` text

reference line: ProductionLine[1];
```

``` text

}
```

``` text

enum ProductionStatus {
```

DESIGN;

PROTOTYPE;

TESTING;

PRODUCTION;

MAINTENANCE;

DECOMMISSIONED;

``` text

}
```

``` text

class ProductionLine {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

attribute type: LineType;
```

``` text

attribute speed: EDouble;
```

``` text

attribute efficiency: EDouble;
```

``` text

attribute validated: EBoolean;
```

``` text

attribute location: EString;
```

``` text

attribute lastValidationDate: EDate;
```

``` text

reference units: ProductionUnit[0..*];
```

``` text

reference parts: MechanicalPart[0..*];
```

``` text

}
```

``` text

enum LineType {
```

ASSEMBLY;

PAINTING;

TESTING;

PACKAGING;

QUALITY_CONTROL;

``` text

}
```

``` text

class MechanicalPart {
```

``` text

attribute id: EString;
```

``` text

attribute name: EString;
```

``` text

attribute partId: EString;
```

``` text

attribute type: PartType;
```

``` text

attribute material: EString;
```

``` text

attribute weight: EDouble;
```

``` text

attribute dimensions: EString;
```

``` text

attribute validated: EBoolean;
```

``` text

attribute inspectionDate: EDate;
```

``` text

reference usedIn: ProductionLine[1];
```

``` text

reference linkedController: Controller[0..1];
```

``` text

}
```

``` text

enum PartType {
```

STRUCTURAL;

ELECTRICAL;

MECHANICAL;

ELECTRONIC;

PLASTIC;

COMPOSITE;

``` text

}
```
