# Build Scripts Framework
---
### Work in progress
This project is not functional, contributors and ideas on how to improve it will be welcome.

I don't even have a `master` branch, so consider everything here completelly experimental.

## Motivation
While you can argue that there are loads of plugins performing a myriad of tasks for the main CI tools out there ([Jenkins](http://jenkins-ci.org), [Bamboo](http://atlassian.com), [ThoughtWorks Go](http://thoughtworks.com)...), there's still a lot of functionality that I miss (publish release notes or documentation to Confluence) and most plugins are not flexible enough (Artifactory plugin for Bamboo will allow me publish, but not promote my artifacts). On top of this, in my experience I've always had some CI tasks that are particular to my company, so there's no plugin option for this.

I could write my own plugins (in my case for Bamboo), but that will get me tied to my current CI tool, making any changes in the future really painful. 

On another hand, I would like developers builds and CI builds to be as similar as possible.

One last reason is having a 'CI tool agnostic' build script framework will make posible for people using different solutions to use and contribute to the tool.

## Intro
The build scripts framework is intended to provide an extendable, easy to understand,
framework to write build scripts in Python.

The primary goal is to run this from a CI server (Bamboo in my case) and the secondary goal
is to allow developers to run the **exact** same tasks from the command line.

The configuration for the tasks will be stored in a yaml file, so it is straight forward to see what steps will be run.

Tasks are divided in _steps_ and grouped in _runners_ (better naming ideas will be welcome) that can have common configuration settings.

Example `tasks.yml` file:

```yaml
buildcxx:   # This is a C++ build runner, that groups a few related C++ tasks
    config: # Configuration shared by all tasks
        build_folder: buildcxx
        output_folder: build_output
    tasks:
        debug:  # Task perfroming a debug c++ build
            config: # Configuration specific to debug task
                some_param: some_value
            steps:
                - clean_build_folders
                - cmake:
                    cmake_args: -DReleaseType=Debug
                - make_install
                - collect_artifacts
                    output: artifacts

release:    # All release related tasks are grouped here
    config:
        artifacts_location: artifacts
    tasks:
        publish:    # Task in charge of publishing an artifact
            config:
                properties:
                    foo: fee
                    moo: mee
            steps:
                - publish:
                    repo: some_repo
        promote:
            steps:
                - promote:
                    repo: another_repo
                    
```                    
                
There are 2 main reasons for having _runners_ (please, help me with a better name for this!) or 'groups of tasks':

* They can share configuration settings, so you do not have to repeat yourself, ie: `build_folder` for all `buildcxx` tasks
* They share requirements: the `release` runner above will require some _manager_ to interact with an artifact repository while some
other runner may require a _vcs_ manager in order to create a tag in our source code.

## How the project is structured
The main entry point `bsf` requires 2 arguments and, optionely, we can provide the location of the source code to 'build'

> bsf [-s SOURCE] RUNNER TASK

Using the example `tasks.yml` file above, we could run a c++ debug build by running:

> bsf -s path/to/source buildcxx debug

This will instantiate a `class BuildCXX` runner from the runners folder and will call the `do` method with the task `debug`. Doing so will sequentially run all the steps listed under the `debug` task in the `buildcxx` runner.

The runner class is resposible for configuring/initializing the required parts. In our example, the `buildcxx` runner will instantiate a `BuildCXXWorker`. This class should contain methods named exactly after the steps available for this task.

(not sure if my effort explaining what's going on makes sense or it's better for you to look at the code, so I'll stop now)

## Interesting links
Here you have some projects I have taken inspiration from

* [Aldebaran qibuild](https://github.com/aldebaran/qibuild): This guys have an awesome tool, but seems too complex for me (my level of Python programing is not **that** high). It also does not seem very straight forward to me how to extend it.
