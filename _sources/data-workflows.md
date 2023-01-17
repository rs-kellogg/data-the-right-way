# Data Workflows

* We can roughly divide data workflow development into two phases:
  * Exploration
  * Deployment
* Each phase benefits from different tools. For exploration it pays to have a [REPL(https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) environment. [Jupyter notebooks](https://jupyter.org/) are particularly nice, but not required.
* Deployment benefits from tools that lend themselves to automation. Scripts (bash, python, R, or whatever else) that can be executed without any human interaction are the prototype.
* Deployment goes hand in hand with automated testing code to validate that nothing unexpected is happening. Tests give you increased confidence (though no guarantee) that you are not messing up.
* The workshop repository contains a [sample project](https://github.com/rs-kellogg/data-the-right-way/tree/main/comscore-project) to demonstrate these concepts.

![Data Workflow](images/data-automation.png)

* Open Science related issues -- data extracts/summaries
* Testing your workflow, modular workflow

![Data Workflow](images/reproducibility.png)


![Data Workflow](images/git-workflow.png)


![Data Workflow](images/unit-testing-puzzle.png)


