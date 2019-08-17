# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
## Added
- `SlurmScheduler` to perform distributed evaluation with slurm
- `LocalScheduler` to perform locally evaluations using joblib
- `Job` objects running on a `Scheduler` returning `Result` objects

## Changed
- `Base`-prefix is removed from all base classes which reside 
 in `base.py` modules.
- `split_by_type` is now a method of the `Domain` class.

## Removed
- `optimisation.bo` package has been removed. Instead a single `bo.py`
 module supports the only BO backend---GPyOpt, as of now.
 
## [0.1.0] - 2019-07-27
### Added
- `TensorboardReporter` result logger using `HParams`
- `GpyOpt` backend for `BayesianOptimisation`
- `RandomSearch` optimiser
- `GridSearch` optimiser
- `Domain` and `Sample` classes as foundations for the optimisers