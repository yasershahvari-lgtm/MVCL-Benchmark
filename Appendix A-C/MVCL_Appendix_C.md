# Appendix C: Reproducible Benchmark Generation and Evaluation Protocol

## C.1. Evaluation Objectives

The benchmark suite evaluates rule coverage, mutation effectiveness, and
detection quality. Rule coverage is assessed by exercising all 30
inconsistency rules in Appendix B; mutation effectiveness is assessed by
verifying that each mutation operator introduces its targeted
inconsistency; and detection quality is assessed by comparing evaluator
output with an independently generated ground-truth set.

## C.2. Benchmark Model and Mutation Design

A clean multi-view automotive model instance is generated first and then
subjected to a rule-specific mutation operator. Each of the 30 operators
corresponds to one MVCL rule and records the benchmark identifier, rule
identifier, affected element identifiers, mutation type, and expected
violation.

## C.3. Independent Ground Truth

Ground truth is generated independently from evaluator output. A true
positive is a detected violation matching a ground-truth rule and
affected element identifiers; a false positive is a reported violation
without a ground-truth match; and a false negative is a ground-truth
violation not reported by the evaluator. Ground-truth records are
serialized as JSON and validated against the accompanying schema. For
the tolerance experiment, the benchmark generator additionally produces
reference tolerance labels through a separate deterministic policy
function based on the predefined context-action mappings; these labels
are independent of the GPT-5.6 responses and are not produced by the
LLM. No human expert panel is used for the current tolerance labels.

## C.4. Benchmark Configurations

Five benchmark configurations are used: B-100, B-500, B-1000, B-TOL, and
B-COMP. The first three increase model scale; B-TOL emphasizes
tolerance-related context; and B-COMP provides a larger composite stress
case.

Five configurations are used: B-100, B-500, B-1000, B-TOL, and B-COMP.
The first three increase model scale; B-TOL emphasizes tolerance-related
context; and B-COMP provides a larger composite stress case.

Each benchmark exercises all 30 mutation operators. Zero failed mutation
constructions establish generator-level coverage and are not interpreted
as final MVCL detection accuracy.

## C.5. Evaluation Metrics

For ground-truth set G and detection set D, TP denotes a detected
violation matching a ground-truth rule and affected element; FP denotes
a reported violation without a ground-truth match; and FN denotes a
ground-truth violation not reported by the evaluator.

Runtime is recorded independently of correctness metrics and is reported
only for executions of the actual MVCL implementation used in the paper.

## C.6. Execution Protocol

The final pipeline is: (i) generate a clean model; (ii) apply one
controlled mutation; (iii) serialize the mutated model; (iv) execute the
actual MVCL/Xtext/EVL implementation; (v) serialize detected
inconsistencies; and (vi) compare them with independent ground truth.
The Python reference evaluator is used only for development and
benchmark sanity checking.

## C.7. Generator Sanity Check

The benchmark package successfully constructs 30 mutation cases for each
of the five configurations with zero mutation-construction failures.
Because randomly generated larger models may contain additional
pre-existing violations, reference-evaluator precision values are not
reported as final MVCL detection results. Final precision, recall, F1,
and runtime values must be obtained from the actual implementation.

## C.8. Reproducibility Artifacts

The artifacts are organized in the public GitHub repository
https://github.com/yasershahvari-lgtm/MVCL-Benchmark. The repository
contains the benchmark code and artifacts used for the publication; an
archived release DOI can be added when available.

## C.9. Threats to Validity and Scope

The benchmark models are synthetic and do not represent the full
variability of industrial automotive systems. Mutation-based evaluation
measures detection of predefined inconsistency patterns and does not
establish completeness for all possible modeling errors. Future work
should complement the benchmark with industrial models and naturally
occurring inconsistencies.

## C.10. Relation to the Main Evaluation

Appendix C provides the experimental infrastructure underlying Section
3. The main evaluation should report only measurements obtained from the
actual MVCL implementation and should reference the benchmark
identifiers defined here. This separation keeps the reference data
independent of the system under test.

### Benchmark Configuration Table

| Benchmark \| Realized Model Elements \| Mutation Cases \|
  Mutation-Construction Failures \|

| --- \| --- \| --- \| --- \|

| B-100 \| 139 \| 30 \| 0 \|

| B-500 \| 696 \| 30 \| 0 \|

| B-1000 \| 1,589 \| 30 \| 0 \|

| B-TOL \| 698 \| 30 \| 0 \|

| B-COMP \| 7,959 \| 30 \| 0 \|
