# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
## Changed
- minor fixes in documentation typos and argument names.
- `Domain` is moved from `hypertunity.optimisation` to the `hypertunity` package.
- rename `TableReporter` to `Table` and `TensorboardReporter` to `Tensorboard`.
- backed for the `Scheduler` is reverted to 'loky' as leaking semaphore errors have disappeared.

## [0.4.0] - 2019-09-15
## Added
- `Trial` a wrapper class for high-level usage, which runs the optimiser, evaluates the objective
 by scheduling jobs, updates the optimiser and summarises the results.
- a `Job` from a script with command line arguments can now be run with 
 named arguments passed as a dictionary instead of a tuple.
- checkpointing of results on disk when calling `log()` or a `Reporter` object.
- optimisation history can now be loaded into an `Optimiser`. Example use-case would be to warm-start
`BayesianOptimisation` from the history of the quicker `RandomSearch`.

## Changed
- every `Reporter` instance has a `primary_metric` attribute, which is an argument to `__init__`.

## Fixed
- validation of `Domain` is not allowing for intervals with more than 2 numbers.
- minor bugs in tests.

## [0.3.1] - 2019-09-10
## Fixed
- `Optimiser.update()` now accepts evaluation arguments that are float, `EvaluationScore` or a dict
 with metric names and floats or `EvaluationScore`s. This is valid for all optimisers. 

## [0.3.0] - 2019-09-08
## Added
- `Job` can now be scheduled locally to run command line scripts with arguments.
- `BayesianOptimisation.run_step` can pass arguments to the backend for better customisation.

## Changed
- any `Reporter` object can be fed with data from a tuple of a 
`Sample` object and a score, which can be a float or an `EvaluationScore`.
- `BayesianOptimisation` optimiser can be updated with a `Sample` and 
a float or `EvaluationScore` objective evaluation types.
- a discrete/categorical `Domain` is defined with a set literal instead of a tuple.
- `Job` supports running functions from within a script by specifying 'script_path::func_name'.
- `batch_size` is no more an attribute of an `Optimiser` but an argument to `run_step`. 
- `minimise` is no more an attribute of `BayesianOptimisation` but an argument to `run_step`.

## [0.2.0] - 2019-08-28
## Added
- `Scheduler` to run jobs locally using joblib.
- `SlurmJob` and `Job` dataclasses defining the tasks to be scheduled.
- `Result` dataclass encapsulating the results from the tasks.
- `TableReporter` class for reporting results in tabular format.
- `Reporter` base class for extending reporters.

## Changed
- `Base`-prefix is removed from all base classes which reside 
 in `base.py` modules.
- `split_by_type` is now a method of the `Domain` class.
- `Optimiser` has a `batch_size` attribute accessible as a property.

## Removed
- `optimisation.bo` package has been removed. Instead a single `bo.py`
 module supports the only BO backend---GPyOpt, as of now.
- prefix for the file encoding (default is utf-8).
 
## [0.1.0] - 2019-07-27
### Added
- `TensorboardReporter` result logger using `HParams`.
- `GpyOpt` backend for `BayesianOptimisation`.
- `RandomSearch` optimiser.
- `GridSearch` optimiser.
- `Domain` and `Sample` classes as foundations for the optimisers.
