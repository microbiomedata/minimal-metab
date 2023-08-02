## SampleOperations-minimal
### Input
```yaml
id: example:SampleOperations001

```
## SampleOperationsCollection-minimal
### Input
```yaml
entries:
- description: abc
  id: example:123
  name: abc

```
## SampleOperationsCollection-minimal-plus
### Input
```yaml
entries:
- id: example:SampleOperations001
  name: foo bar
- id: example:SampleOperations002
  name: foo bar

```
## SampleOperationsCollection-undefined-slot
### Input
```yaml
entries:
- id: example:SampleOperations001
  name: foo bar
- id: example:SampleOperations002
  name: foo bar
  undefined: undefined

```
## SampleOperationsCollection-missing-id
### Input
```yaml
entries:
- description: abc
  has_input: abc
  has_output: abc
  name: abc

```
## SampleOperationsCollection-no-id
### Input
```yaml
entries:
- age_in_years: 33
  name: foo bar
  primary_email: foo.bar@example.com

```
## SampleOperationsCollection-bad-id-pattern
### Input
```yaml
entries:
- id: example_Person001
  name: foo bar
- id: example_Person002
  name: foo bar

```
