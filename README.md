Build Scripts Framework
=======================

Work in progress, ideas on how to improve will be welcome.

The build scripts framework is intended to provide an extendable, easy to understand,
framework to write build scripts in Python.

The primary goal is to run this from a CI server (Bamboo in my case) and the secondary goal
is to allow developers to run the _exact_ same tasks from the command line.

The configuration for the tasks will be stored in a yaml file, so it's very straight forward
to see what steps each task will perform. Tasks are divided in _steps_. Tasks are grouped in
_runners_ (better naming ideas will be welcome) that can have common configuration settings.

Example

```yaml
buildcxx:   # This is a C++ buidl runner, that groups a few related C++ tasks
    config: # Configuration shared by all tasks
        build_folder: buildcxx
        output_folder: build_output
    tasks:
        debug:  # Task perfroming a debug c++ build
        config: # Configuration specific to this task
            some_param: some_value
        steps:
            - clean_build_folders
            - cmake:
                cmake_args: -DReleaseType=Debug
            - make_install
            - collect_artifacts
                output: artifacts
```                    
                
        