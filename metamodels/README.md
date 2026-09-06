# Ecore Metamodels

This directory contains the three Ecore metamodels used by the benchmark artifact:

- `electrical.ecore` — electrical components, batteries, power supplies, and system loads.
- `software.ecore` — software components, requirements, controllers, sensors, and actuators.
- `production.ecore` — production units, production lines, mechanical parts, and functionalities.

The `.ecore` files are stored in standard EMF Ecore XMI format. Cross-package references use the declared namespace URIs. No generated Java model plug-ins are required to inspect the metamodel definitions.
